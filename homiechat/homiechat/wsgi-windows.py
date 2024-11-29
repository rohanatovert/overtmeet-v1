# activate_this = 'C:/Users/myuser/Envs/my_application/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
# exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
# site.addsitedir('C:/Users/myuser/Envs/my_application/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:\inetpub\wwwroot\homiechat\homiechat')
sys.path.append('C:\inetpub\wwwroot\homiechat\homiechat\homiechat')

os.environ['DJANGO_SETTINGS_MODULE'] = 'homiechat.base'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homiechat.base")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()