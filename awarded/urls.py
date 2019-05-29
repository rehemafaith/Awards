from django.conf.urls import url
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^new_project',views.new_project,name='new_project'),
    url('^profile/$',views.profile,name='profile'),
    url('^project/$',views.full_project,name='project')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
