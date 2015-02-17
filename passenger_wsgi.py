import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), '/var/www'))
os.environ['DJANGO_SETTINGS_MODULE'] = "cpc.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
