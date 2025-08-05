# Blog Platform Backend

A Django REST API backend for a blog platform with user authentication, blog creation, and commenting features.

## Features

- User registration and authentication
- Blog creation and management
- Commenting system with nested replies
- PostgreSQL database integration
- RESTful API endpoints

## Requirements

- Python 3.8+
- Django 5.2+
- PostgreSQL 12+

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd blog_project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL database:
   - Install PostgreSQL
   - Create a database named `blog_db`
   - Create a user with appropriate permissions

5. Update database settings in `blog_project/settings.py` with your PostgreSQL credentials.

6. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Users
- `POST /api/users/register/` - Register a new user
- `POST /api/users/login/` - User login
- `POST /api/users/logout/` - User logout
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/update/` - Update user profile

### Blogs
- `GET /api/blogs/` - List all published blogs
- `POST /api/blogs/create/` - Create a new blog
- `GET /api/blogs/my-blogs/` - List blogs of the current user
- `GET /api/blogs/<id>/` - Get a specific blog
- `PUT /api/blogs/<id>/` - Update a specific blog
- `DELETE /api/blogs/<id>/` - Delete a specific blog

### Comments
- `POST /api/comments/create/` - Create a new comment
- `GET /api/blogs/<blog_id>/comments/` - Get comments for a blog
- `GET /api/comments/<comment_id>/replies/` - Get replies to a comment
- `PUT /api/comments/<comment_id>/update/` - Update a comment
- `DELETE /api/comments/<comment_id>/delete/` - Delete a comment

## Database Configuration

The project is configured to use PostgreSQL. Update the following settings in `blog_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## RESULTS

![alt text](<Screenshot 2025-08-05 204227.png>) ![alt text](<Screenshot 2025-08-05 204320.png>)

## License
This project is licensed under the [MIT License](./LICENSE).