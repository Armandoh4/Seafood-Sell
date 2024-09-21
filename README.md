# seafoods
Features
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