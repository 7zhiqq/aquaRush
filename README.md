# README

## Project Overview

This project is a web-based application for managing orders and deliveries. It is designed for different types of users, such as admins, cashiers, staff, and drivers. The admin can view all users and their orders, while cashiers and staff can manage orders and update their statuses. Drivers are assigned specific orders and can update the delivery status.

### Key Features:
- **Admin Dashboard**:
  - View a list of all users with their roles and statuses.
  - Filter orders based on delivery status.
  - Add new orders and manage their status.
  
- **Staff & Cashier Dashboard**:
  - View orders and their statuses.
  - Filter orders by delivery status (Out for Delivery, Cancelled, Delivered).
  - Update order statuses, including marking orders as "Out for Delivery" or "Cancelled".
  
- **Driver Dashboard**:
  - View a list of orders assigned to the driver.
  - Update order status to "Delivered" when a delivery is completed.
  - View order details and the customer’s address.

- **Responsive User Interface**:
  - The application has a responsive design, which adapts for both desktop and mobile views.
  - Users can filter orders based on different delivery statuses.
  
## Setup Instructions

### Prerequisites

Before running this application, ensure that you have the following installed on your local machine:
- Python 3.x
- Django 3.x or higher
- PostgreSQL (or any other preferred database)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Ensure PostgreSQL (or the chosen database) is running.
   - Create a database for the project (if using PostgreSQL):
   
     ```bash
     createdb your_database_name
     ```

5. **Apply database migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (for the admin dashboard):

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create the superuser account.

7. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your web browser.

### Configuration

1. **Settings for Roles and Permissions**:  
   - Admin users can view and manage all users and orders.
   - Staff and Cashier roles can update order statuses.
   - Driver users are assigned orders and can mark them as delivered.

2. **Database Configuration**:  
   - Ensure your database settings in `settings.py` are correct. For example, for PostgreSQL:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_database_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

## Runtime Instructions

1. **Login as Admin**:
   - Admins can log in using the superuser credentials created during setup.
   - They will be able to see and manage all users and orders.
   
2. **Login as Staff or Cashier**:
   - Staff and cashiers can manage order statuses but cannot add or delete orders.
   - They can filter orders based on the delivery status and update them accordingly.

3. **Login as Driver**:
   - Drivers can view only the orders assigned to them.
   - They can mark orders as delivered once completed.

4. **Managing Orders**:
   - Users with the necessary permissions can update the status of orders from "Pending" to "Out for Delivery", "Delivered", or "Cancelled".
   - Admin users have full control over order management, while staff and drivers can only view and update their respective tasks.

## Assumptions Made During Development

1. **Database**:
   - It is assumed that a PostgreSQL database (or equivalent) is being used. Adjustments will be needed for other databases.
   
2. **User Roles**:
   - The system assumes a role-based user management structure where each user can be assigned specific roles like Admin, Cashier, Staff, or Driver.
   - Each role has specific permissions to access and modify the data.

3. **Frontend**:
   - The application uses basic Bootstrap 5 for styling and layout.
   - Some UI elements, such as buttons and dropdowns, are implemented using Font Awesome icons.

4. **Filters**:
   - Orders can be filtered by status in both the Admin and Driver dashboards.
   - The driver can only see their assigned orders based on their role.

## Project Structure

The project follows a typical Django structure:

```
yourproject/
│
├── yourapp/                  # Your main application
│   ├── migrations/           # Database migrations
│   ├── models.py             # Database models
│   ├── views.py              # Views for handling HTTP requests
│   ├── urls.py               # URL routing for views
│   └── templates/            # HTML templates for the frontend
│       └── home.html         # Home page template
├── yourproject/              # Main project folder
│   ├── settings.py           # Django settings configuration
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI configuration for deployment
├── manage.py                 # Django's command-line utility
└── requirements.txt          # Project dependencies
```

## License

This project is open-source and available under the MIT License.