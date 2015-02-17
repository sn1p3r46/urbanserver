import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), '/var/www'))
os.environ['DJANGO_SETTINGS_MODULE'] = "UrbanServerApp_project.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
