from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Static file settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "blog/static",  # Tells Django where to find additional static files
]

# Templates settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'blog/templates'],  # Tells Django where to look for templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
