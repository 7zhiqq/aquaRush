
# AquaRush - Water Delivery Management Application

## Project Overview

AquaRush is a web-based application for managing water delivery orders and tracking their status. The application supports different user roles, including **Admin**, **Cashier**, **Staff**, and **Driver**, each with specific permissions and responsibilities. The **Admin** can manage users and view all orders, while **Cashiers** and **Staff** manage and update the status of orders. **Drivers** are assigned specific orders and can update the delivery status.

### Key Features:
- **Admin Dashboard**:
  - View a list of all users with their roles and statuses.
  - Filter orders by delivery status.
  - Add new orders and manage their statuses.

- **Staff & Cashier Dashboard**:
  - View orders and their statuses.
  - Filter orders by delivery status (e.g., Out for Delivery, Cancelled, Delivered).
  - Update order statuses, including marking orders as "Out for Delivery" or "Cancelled."

- **Driver Dashboard**:
  - View a list of orders assigned to the driver.
  - Update order status to "Delivered" when a delivery is completed.
  - View order details, including the customer’s address.

- **Responsive User Interface**:
  - The application is designed to be responsive, adapting for both desktop and mobile views.
  - Users can filter orders based on different delivery statuses.

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.x
- Django 3.x or higher
- MySQL (or an alternative database if preferred)

### Installation

1. **Create a virtual environment** (recommended but optional):

   ```bash
   python3 -m venv .venv
   .\.venv\Scripts\activate  # On Windows, use `.venv\Scripts\activate`
   ```

2. **Set up the database**:
   - Ensure MySQL is running on your system.
   - Create a MySQL database for the project, named `aquaRush`.
   - Then, run the following in the terminal to create the database:

     ```bash
     python mydb.py  # Assuming `mydb.py` contains the necessary database setup
     ```

3. **Update Database Configuration**:
   - Open `settings.py` in your project and find the `DATABASES` configuration section.
   - Modify it to use MySQL as follows:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'aquaRush',  # Database name
             'USER': 'root',      # MySQL username
             'PASSWORD': 'yourpassword',  # MySQL password
             'HOST': 'localhost',   # MySQL host
             'PORT': '3306',        # MySQL port
         }
     }
     ```

4. **Apply database migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for the Admin dashboard):

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create the superuser account.

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your browser to access the application.

### Configuration

1. **Role-based Permissions**:  
   - Admin users can view and manage all users and orders.
   - Staff and Cashiers can update order statuses, but cannot delete orders.
   - Drivers are assigned specific orders and can mark them as "Delivered."

2. **Database Configuration**:  
   - Ensure your MySQL database settings in `settings.py` are correct. For example:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'aquaRush',
             'USER': 'root',
             'PASSWORD': 'yourpassword',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

## Runtime Instructions

1. **Login as Admin**:
   - Admins can log in using the superuser credentials created during setup.
   - Admins can create, view, and manage all users and orders.

2. **Login as Staff or Cashier**:
   - Staff and Cashiers can manage orders and update their statuses, but they cannot delete orders.
   - They can filter orders based on delivery status and update them accordingly.

3. **Login as Driver**:
   - Drivers can view only the orders assigned to them.
   - They can mark orders as "Delivered" once completed.

## Assumptions Made During Development

1. **Database**:
   - The application assumes the use of MySQL (or an equivalent relational database). Adjustments may be needed for other databases.

2. **User Roles**:
   - The system assumes a role-based user management structure, where each user is assigned a role (Admin, Cashier, Staff, or Driver), each with specific permissions.

3. **Frontend**:
   - The application uses **Bootstrap 5** for styling and layout.
   - Icons (buttons, dropdowns, etc.) are implemented using **Font Awesome**.

4. **Filters**:
   - Orders can be filtered by status in the Admin and Driver dashboards.
   - Drivers can only see the orders assigned to them.

## Project Structure

The project follows a typical Django structure:

```
aquaRush/
│
├── aquaRush/                  # Main project folder
│   ├── settings.py            # Django settings configuration
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py                # WSGI configuration for deployment
│
├── yourapp/                   # Main application
│   ├── migrations/            # Database migrations
│   ├── models.py              # Database models
│   ├── views.py               # Views for handling HTTP requests
│   ├── urls.py                # URL routing for views
│   └── templates/             # HTML templates for the frontend
│       └── home.html          # Home page template
│
├── manage.py                  # Django's command-line utility
└── requirements.txt           # Project dependencies
```

## License

This project is open-source and available under the MIT License.

---

## Troubleshooting

1. **MySQL Connection Issues**:
   - Ensure MySQL is running and that your database configuration in `settings.py` is correct.
   - If you encounter a `ConnectionError`, verify the MySQL username, password, host, and port.

2. **Dependency Issues**:
   - If you receive errors related to missing dependencies, run:

     ```bash
     pip install -r requirements.txt
     ```

   - Ensure all required packages are installed.

3. **Migration Issues**:
   - If migrations fail, make sure your database is created and accessible. You can try to apply migrations manually:

     ```bash
     python manage.py migrate
     ```
