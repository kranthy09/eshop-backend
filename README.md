# eshop-backend

## Django 'create()':

### when used on the User model, it doesn't handle password hashing properly, making it insecure for user creation.

## Django 'create_user()':

### It takes arguments for username, email, and password, and importantly, it hashes the password before saving it to the database, ensuring security.
