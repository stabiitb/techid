import os
import sys	
sys.path.append('/var/www/event/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'events.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
