# eshop-backend

## Django 'create()':

### when used on the User model, it doesn't handle password hashing properly, making it insecure for user creation.

## Django 'create_user()':

### It takes arguments for username, email, and password, and importantly, it hashes the password before saving it to the database, ensuring security.

Scope:
null=True affects the database schema, while blank=True affects form validation.
Value:
null=True allows a field to be NULL in the database, while blank=True allows an empty string ("") in forms.

Rating for a product is determined by the reviews.
