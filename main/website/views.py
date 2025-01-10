from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, OrderForm
from django.contrib.auth.decorators import login_required
from website.models import Order
from django.contrib.auth.models import User

# Views

def home(request):
    # Get the logged-in user
    user = request.user
    is_cashier = False
    is_staff = False
    is_driver = False
    orders = Order.objects.all() 

    # Check if the user is authenticated
    if user.is_authenticated:
        is_cashier = user.groups.filter(name='cashier').exists()
        is_staff = user.groups.filter(name='staff').exists()
        is_driver = user.groups.filter(name='driver').exists()  

        if is_driver:
            orders = orders.filter(driver=user)

        if request.user.is_superuser:
            # Fetch all users for superuser
            users = User.objects.all()

    status_filter = request.GET.get('status_filter', None)  # Get status_filter
    if status_filter:
        # Filter orders by the selected status
        orders = Order.objects.filter(status=status_filter)
    else:
        # Show all orders if no filter is selected
        orders = Order.objects.all()

    # Count orders by status
    out_for_delivery_count = orders.filter(status='Out for Delivery').count()
    delivered_count = orders.filter(status='Delivered').count()
    cancelled_count = orders.filter(status='Cancelled').count()
    pending_count = orders.exclude(status__in=['Out for Delivery', 'Delivered', 'Cancelled']).count()

    # POST request for login attempt
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect('home')  # Stay on the same page if login fails

    context = {
        'user': user,
        'orders': orders,
        'is_cashier': is_cashier,
        'is_staff': is_staff,
        'is_driver': is_driver,  
        'out_for_delivery_count': out_for_delivery_count,
        'delivered_count': delivered_count,
        'cancelled_count': cancelled_count,
        'pending_count': pending_count,
    }
    return render(request, 'home.html', context)

        
def logout_user(request):
    # Logout user
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == "POST":  # Register
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save user first
            role = request.POST.get('role')  # Get the selected role (from the form)
            
            # Define roles 
            try:
                group = Group.objects.get(name=role)
                user.groups.add(group)  # Add the user to the group/role
            except Group.DoesNotExist:
                messages.error(request, "The selected role does not exist.")
                return redirect('register')  

            # Authenticate and Log In the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Successfully Registered. Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

@login_required
def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('order_confirmation') 
    else:
        form = OrderForm()

    return render(request, 'new_order.html', {'form': form})

def order_confirmation(request):
    return render(request, 'order_confirmation.html')

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})

@login_required
def mark_order_delivered(request, order_id):
    # Retrieve order by its ID
    order = get_object_or_404(Order, id=order_id)

    # Check if the logged-in user is the driver assigned to this order
    if order.driver == request.user:
        # Mark the order as delivered
        order.status = 'Delivered'
        order.save()

        # Show a success message
        messages.success(request, f"Order {order.order_number} marked as delivered!")
    else:
        messages.error(request, "You are not authorized to mark this order as delivered.")

    return redirect('home')

@login_required
def mark_order_out(request, order_id):
    # Retrieve the order by its ID
    order = get_object_or_404(Order, id=order_id)

    # Check if the logged-in user is in the 'staff' group
    if request.user.groups.filter(name='staff').exists():
        # Mark the order as 'Out for delivery'
        order.status = 'Out for delivery'
        order.save()
        messages.success(request, f"Order {order.order_number} marked as out for delivery!")
    else:
        messages.error(request, "You are not authorized to mark this order as out for delivery.")

    return redirect('home')

@login_required
def update_order_status(request, order_id, new_status):
    # Retrieve the order by its ID
    order = get_object_or_404(Order, id=order_id)

    # Check if the user is staff
    if request.user.groups.filter(name='staff').exists():
        # Update the order status
        order.status = new_status
        order.save()
        messages.success(request, f"Order {order.order_number} status updated to '{new_status}'!")
    else:
        messages.error(request, "You are not authorized to update the order status.")

    return redirect('home')

@login_required
def edit_order(request, order_id):
    # Retrieve the order by its ID
    order = get_object_or_404(Order, id=order_id)

    if request.user.groups.filter(name='staff').exists() or order.driver == request.user:
        if request.method == 'POST':
            form = OrderForm(request.POST, instance=order) 
            if form.is_valid():
                form.save()  # Save the updated order
                messages.success(request, f"Order {order.order_number} has been updated successfully!")
                return redirect('order_detail', order_id=order.id)  # Redirect to the order detail page
        else:
            form = OrderForm(instance=order)  # Create the form with existing order data
        return render(request, 'edit_order.html', {'form': form, 'order': order})
    else:
        messages.error(request, "You are not authorized to edit this order.")
        return redirect('home')

def order_list(request):
    status_filter = request.GET.get('status_filter')
    if status_filter:
        orders = Order.objects.filter(status=status_filter)
    else:
        orders = Order.objects.all()  

    return render(request, 'your_template.html', {'orders': orders})