from .base import *

SECRET_KEY = 'z%dedp_ymnd1m3oh&nhn*vrl5k11vw!-e=v$4e_!-7d95i3svc'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}