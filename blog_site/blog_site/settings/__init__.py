import os
from .base import *

DJANGO_ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'production')
print(f"Using environment : {DJANGO_ENVIRONMENT}")

if DJANGO_ENVIRONMENT in ('development', 'dev'):
    from .development import *
else:
    from .production import *
