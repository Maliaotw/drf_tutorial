"""
WSGI config for drf_tutorial project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

import sys

sys.path.append('/Users/maliao/anaconda3/envs/drf/python3.6/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_tutorial.settings')

application = get_wsgi_application()



# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()