<!-- Home Furniture E-commerce Product API -->

A RESTful backend API built with Django and Django Rest Framework (DRF) for managing home furniture products.
This project was developed as a Backend Engineering Capstone Project.

<!-- Project Overview -->

The Home Furniture E-commerce API allows authenticated users to manage furniture products categorized into:

Living Room

Bedroom

Office

The API supports full CRUD operations, search, filtering, pagination, and authentication.

<!-- Features -->

- Product Management

Create,
read,
update,
and delete products

Product attributes:

Name
Description
Price
Category
Stock Quantity
Image URL
Created Date

- User Authentication

User registration and login

Only authenticated users can create, update, or delete products

Public users can view and search products

- Search & Filtering

Search products by:
Name (partial match)
Category

Filter products by:
Category
Price range
Stock availability

Pagination for large datasets


<!-- Tech Stack -->

-Backend: Django, Django REST Framework
-Database: SQLite (default, can be extended)
-Authentication: Django authentication / Token-based auth
-Deployment: PythonAnywhere
-Tools: Git, GitHub, Postman


<!-- Project Structure -->

home-furniture-ecommerce-api/
│ecommerce_api
├── config/                 
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── products/               
├── users/                  
├── manage.py
├── requirements.txt
└── README.md


<!-- API Endpoints (Sample) -->

-Authentication
Method	Endpoint	        Description

POST	/api/auth/register/	Register a new user
POST	/api/auth/login/	Login user

-Products
Method	Endpoint	         Description

GET	    /api/products/	     List all products
POST	/api/products/	     Create a product (auth required)
GET	    /api/products/{id}/	 Product detail
PUT	    /api/products/{id}/	 Update product (auth required)
DELETE	/api/products/{id}/	 Delete product (auth required)


<!-- Search & Filter -->

/api/products/?search=chair
/api/products/?category=Living Room
/api/products/?min_price=100&max_price=500
/api/products/?in_stock=true

<!-- Deployment -->

https://birukbarba.pythonanywhere.com/

<!-- Testing -->

-API tested using Postman
-All CRUD, authentication, search, and filtering endpoints tested successfully

<!-- Author -->

Biruk Barba Edao
Back-End Web Development Student in Alxafrica
Capstone Project – 2026

<!-- License -->

This project is for educational purposes.