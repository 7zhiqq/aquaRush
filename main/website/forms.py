import random
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from website.models import Order
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.models import Group
from django.utils import timezone


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(
        label="", max_length="100", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        label="", max_length="100", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') 

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'shipping_address', 'phone_number', 'quantity', 'delivery_datetime', 'driver', 'amount_to_pay']  # includes amount_to_pay

    customer_name = forms.CharField(
        max_length=100, 
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'})
    )
    
    shipping_address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address'}), 
        max_length=500, 
        label=""
    )
    
    phone_number = forms.CharField(
        max_length=15, 
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'})
    )

    quantity = forms.IntegerField(
        min_value=1, 
        required=True, 
        label="",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'})
    )
    
    delivery_datetime = forms.DateTimeField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control flatpickr-datetime', 'placeholder': 'Select Delivery Date & Time'}),
    )

    driver = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name="Driver"),  # Get users from the 'Driver' group
        empty_label="Assign Driver",  
        required=True,
        label="",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    amount_to_pay = forms.DecimalField(
        max_digits=10, decimal_places=2, required=False, label="Amount to Pay", widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if not quantity:
            raise forms.ValidationError('Quantity cannot be null.')
        return quantity

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        pattern = re.compile(r'^(?:\+63|0)[9|8|7]\d{9}$')  # Validate Philippine phone numbers
        if not pattern.match(phone_number):
            raise ValidationError("Please enter a valid Philippine phone number (e.g., +639171234567 or 09171234567).")
        return phone_number

    def clean_delivery_datetime(self):
        delivery_datetime = self.cleaned_data.get('delivery_datetime')
        
        current_time = timezone.now() 
        
        if not delivery_datetime:
            raise ValidationError('This field is required.')
        
        if delivery_datetime < current_time:
            raise ValidationError("Delivery date must be in the future.")
        
        return delivery_datetime

    def generate_order_number(self):
        # Generates a unique order number
        order_number = "AQTN" + str(random.randint(1000, 9999))
        return order_number

    def to_pay(self):
        # Calculate the amount to pay 
        quantity = self.cleaned_data.get('quantity')
        if quantity:
            return quantity * 15  # 15 pesos per galloon
        return 0

    def save(self, commit=True):
        order = super(OrderForm, self).save(commit=False)
        order.order_number = self.generate_order_number()

        order.amount_to_pay = self.to_pay()

        # Save to the database
        if commit:
            order.save()

        return order 