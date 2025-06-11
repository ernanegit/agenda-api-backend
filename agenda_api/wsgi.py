import os
from django.core.wsgi import get_wsgi_application

# Usar production settings por padrão
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agenda_api.production_settings')

application = get_wsgi_application()
