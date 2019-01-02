import os
from .base import *

APP_ENV = os.getenv("APP_ENV", "local")
if APP_ENV == 'local':
    from .local import *
else:
    from .prod import *



