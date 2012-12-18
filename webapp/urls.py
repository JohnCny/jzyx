
from django.conf.urls.defaults import *
from models import *
from views import *
 

urlpatterns = patterns('',
    (r'myfilter/create/$', create_myfilter),
    (r'myfilter/list/$', list_myfilter ),
    (r'myfilter/edit/(?P<id>[^/]+)/$', edit_myfilter),
    (r'myfilter/view/(?P<id>[^/]+)/$', view_myfilter),    
)
