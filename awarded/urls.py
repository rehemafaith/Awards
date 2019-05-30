from django.conf.urls import url
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^new_project',views.new_project,name='new_project'),
    url('^profile/',views.profile,name='profile'),
    url(r'^project/(\d+)',views.full_project,name='project'), 
    url(r'^api/project/$',views.ProjectList.as_view()),
    url(r'^api/profile/$',views.ProfileList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
