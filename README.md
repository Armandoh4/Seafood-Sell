# Seafood Sell
 ---
 ![Home](readme_assets/home.jpg)

 ![Static Badge](https://img.shields.io/badge/Web%20-%20HTML5-orange) ![Static Badge](https://img.shields.io/badge/CSS-blue) ![Static Badge](https://img.shields.io/badge/JavaScript-f7df1e) ![Static Badge](https://img.shields.io/badge/Python-ffde57) ![Static Badge](https://img.shields.io/badge/Django-092E20)

[View My Github Project - Regular User](https://armandoh4.pythonanywhere.com/)

[View My Github Project - Admin link](https://armandoh4.pythonanywhere.com/admin/)

 ## Introduction
'Seafood Sell' (Ssell) is an online company that offers the user a range of seafood to purchase. It is the demo/ proof of concept for a real business, similar to my previous project "Filmlab Productions." The site provides customers live prices and the ability to add various seafood items into a 'cart.' Once the customer wishes to proceed, they can edit and/ or finalise the order by entering their payment details.

Once a customer proceeds to the checkout, they will will be provided the option to edit their cart, offering full flexibility on the clients end. Once the customer is satisfied, they will have the opportunity to make a payment and checkout using 'Stripe.' They will also produce a response on wether or not the purchase was succesfully completed or not.

Ssell offers a fully adaptive display, from a range of devices, allowing more users online to purchase goods and services from the business. The app has a working navigation menu and a login/ sign-up button on the right, located by the nav bar.

### Superuser Account
Example of the display of the admin pannel:

![Example of the display of the admin pannel](readme_assets/adminpannel.png)

To login to the superuser account you must add "admin" to the end of the site url (EX. 'https://armandoh4.pythonanywhere.com/admin/')

    Deployed Version 'Superuser' Details:
        Username: superadmin
        Email address: superadmin@gmail.com
        Password: superadmin

            Note: 
                If running locally please create a new superuser with the following command
                (review "Deployment of Project"):
    
                    "python manage.py createsuperuser"
        
                Please note that when running on your local machine,
                you will need to add new products to the website by using as a superuser

### Regular Account
Upon checkout you will be required to login to the regular account. 
    
    Deployed Version 'Regular' Login Details:
        User: admin
        Email: admin@gmail.com
        Password: admin
Alternatively, you can also sign up an account for the demo by using the sign-up page: in the top right of the page

Once the user has registered an account, they will have the option to login. Note, a login will be required to purchase an item.

### Payment Method
To protect your card details, I am running this demo with the Stripe demo account. So please enter these details when making payments upon landing on the card payment page:

    Mock Payment Details:
        - Card Number: 4242 4242 4242 4242 
        (IMPORTANT - CARD NUMBER FOR STRIPE DEMO)

        - Date of expiry should be in the future

## Remote Deployment of Project

    1 - To run this project remotely, you would require the 'dotenv' module. You can install this module in the terminal with the following code:
            - pip install python-dotenv

        - Ensure you have a 'env.py' file in the root directory with the following information filled in:
                    
                    SECRET_KEY='...'
                    STRIPE_SECRET_KEY='...'
                    STRIPE_PUBLISHABLE_KEY='...'
                    WEBHOOK_SECRET_KEY='...'


    2 - Create a Virtual Environment, to isolate your project dependencies, using the following command:
            - python -m venv env
    
    3 - Activate the virtual environment:
            Windows:
            - .\env\Scripts\activate
            MacOs/Linux:
            - source env/bin/activate

    4 - Install all requirements and modules using the following:
        - pip install -r requirements.txt

    5 - Database Migrations:
        * Django uses migrations to manage database schema changes.
        * First, create initial migrations for your app(s):
            - python manage.py makemigrations
        * Apply the migrations to create database tables:
            - python manage.py migrate

    6 - Create a Superuser (Admin):
        - Enter the following code in your terminal: python manage.py createsuperuser

    7 - Run on local server:
        - Enter the following code in your terminal: python manage.py runserver
    
    8 - Time to open your server:
        * Visit http://127.0.0.1:8000/ in your browser to see your Django app.

 ---
 ## CONTENTS:
 ---

* [User Experience - UX](#user-experience) 
    * [First Time Visitor GOAL](#first-time-visitor-goal)
    * [Return Visitor GOAL](#returning-visitor-goal)

* [Design](#design)
    * [Features](#features)

* [Features](#features)
    * [Future Implementations](#future-implementations)

* [TESTING](#testing)

* [Acknowledgments](#acknowledgments)

---
## User Experience:

### First Time Visitor GOAL

    1 - To quickly find out what products Ssell is offering

    2 - To find out if Ssell is a legitimate business, does this webapp legitimise the company?

    3 - To find out information on the team behind Ssell, follow the latest news about the company, where the company is based, and to contact the company directly

    4 - What the company is about and where they source their items

### Returning Visitor GOAL
    1 - One user might be an admin or owner of the website. This user would require a way to list and describe new items, along with the ability to edit existing ones.
    2 - Look for discounts or sales at that time
    3 - Be able to contact the business regarding business enquiries


---
## Design:
The design of this project was simple. I wanted to keep this project focused on functio over form, and I would say that I have achieved that while managing to submit this as fast as I possibly could. However, I did take inspiration from the website 'Seafood Direct' 

![Seafood direct](readme_assets/exmp.png)

Here is my site to compare:
![Display](readme_assets/home.jpg)

## Database Model Structure

![ERD Diagram](readme_assets/erd.jpg)

- User
    - username
    - email
    - password

- Cart
    - product (ForeignKey to Product)
    - loged_user (ForeignKey to User)
    - quantity (Positive Integer)
- Product
    - product_name
    - price
    - description
    - category (ForeignKey to Category)
- Category
    - category
- Record
    - customer_email
    - amount_total
    - payment_intent
    - payment_id
    - status

## Relationships between entities:
- A User can have one Cart at a time.
- A Cart belongs to a User and a Product.
- A Product belongs to a Category.
- A Record is associated with a User through the customer_email field.


---
## Features:
---
The features are currently split between the edit functions of the Admin & the control over the cart for the regular user interface.

This is the admin pannel
![Admin pannel](readme_assets/adminpannel.png)

An example of the display of the homepage
![Here is an example of the display of the homepage](readme_assets/home.jpg)

Here is the cart image
![Cart image](readme_assets/cart.png)

Here is an example of the information required when making a purchase request
![Payment failed](readme_assets/required.png)

When a Payment goes through
![Payment success](readme_assets/success.png)

Here is what occurs if the payment does not go through, using the stripe interface
![Payment failed](readme_assets/payfail.png)



#### Below I have listed all of the features/functions available in this project:
    - User authentication and authorization
    - Product browsing by categories
    - Cart functionality
    - Stripe payment integration
    - Order history and management
    - vDatabase Schema
    - Models
    - Categorie

    - id (Primary Key)
    - categorie (CharField)
    - Products

    - id (Primary Key)
    - name (CharField)
    - description (TextField)
    - price (DecimalField)
    - Categorie (ForeignKey to Categorie)
    - Cart

    - id (Primary Key)
    vproduct (ForeignKey to Product)
    - loged_user (ForeignKey to User)
    - Record

    - id (Primary Key)
    - customer_email (EmailField)
    - amount_total (DecimalField)
    - payment_intent (CharField)
    - payment_id (CharField)
    - status (CharField)
    - CRUD Functionalities
    - Categories
    - Create: Admin can create a new category.
    - Read: Users can view all categories.
    - Update: Admin can update a category.
    - Delete: Admin can delete a category.
    - Products
    - Create: Admin can add new products.
    - Read: Users can view products by category.
    - Update: Admin can update product details.
    - Delete: Admin can delete a product.
    - Cart
    - Create: Users can add products to their cart.
    - Read: Users can view their cart.
    - Update: Not applicable.
    - Delete: Users can remove products from their cart.
    - Records
    - Create: Records are created upon successful payment.
    - Read: Admin can view payment records.
    - Update: Not applicable.
    - Delete: Admin can delete records if necessary.

### Future Implementations
    In the furture I will expand on the complexity of the website, by adding moreproducts, including a way to purchase products without a login. I would also like to include a live chat feature, or a chatbot to make communicating with potential business partners easier.

    One additional feature would include, having the site also aid in guiding users to the physical store, and offers insights into the operations of the business. This can be simply implemented using google maps and Iframes.

    I want to make further imporvements to my cart implementation, to do this I will incorperate stacking of cart items. Here is an image of how I would likely go about that in the future:
    ![cartcode](readme_assets/futureimplementation.png)

    I would like to fix the hover over products. Currently hovering over a product diplays the description of said product. However, the background no longer darkens to show text more clearly. I would like to fix this in future versions of the website. I would also like to make items stack in the cart automatically, currently this is a manual process. 


---
## Testing:
[Testing found here](TESTING.md) 

---
##  Acknowledgments:
I used the design at 'https://seafooddirect.co.uk' as a reference for what I want my website to look like. I also used Chat GPT to correct spelling and make item descriptions.


### Features:
        User authentication and authorization
        Product browsing by categories
        Cart functionality
        Stripe payment integration
        Order history and management
        Database Schema
        Models
        Categorie

        id (Primary Key)
        categorie (CharField)
        Product

        id (Primary Key)
        name (CharField)
        description (TextField)
        price (DecimalField)
        Categorie (ForeignKey to Categorie)
        Cart

        id (Primary Key)
        product (ForeignKey to Product)
        loged_user (ForeignKey to User)
        Record

        id (Primary Key)
        customer_email (EmailField)
        amount_total (DecimalField)
        payment_intent (CharField)
        payment_id (CharField)
        status (CharField)
        CRUD Functionalities
        Categories
        Create: Admin can create a new category.
        Read: Users can view all categories.
        Update: Admin can update a category.
        Delete: Admin can delete a category.
        Products
        Create: Admin can add new products.
        Read: Users can view products by category.
        Update: Admin can update product details.
        Delete: Admin can delete a product.
        Cart
        Create: Users can add products to their cart.
        Read: Users can view their cart.
        Update: Not applicable.
        Delete: Users can remove products from their cart.
        Records
        Create: Records are created upon successful payment.
        Read: Admin can view payment records.
        Update: Not applicable.
        Delete: Admin can delete records if necessary.