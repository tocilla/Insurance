import os
from .base import *
# you need to set "ENVIROMENT = 'production'" as an environment variable
# in your OS (on which your website is hosted)
enviroment = os.environ.get('ENVIROMENT', 'development')
if enviroment == 'production':
    from .production import *
elif enviroment == 'travis':
    from .travis import *
else:
    from .local import *
