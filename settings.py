# ... existing code

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'blog_db',
        'USER': 'blog_user',
        'PASSWORD': 'blog_password',
        'HOST': 'localhost',
        'PORT': '5434',
    }
}

# Custom User Model
AUTH_USER_MODEL = 'users.User'

# ... rest of the file ...