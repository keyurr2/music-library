from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'(?P<name>\w+)/$', views.dirLevelOne, name='dirLevelOne'),
	url(r'(?P<name>\w+)/(?P<dirname>[\w-]+)', views.dirLevelTwo, name='dirLevelTwo')
	# url(r'(?P<name>\w+)/(?P<dirname>\w+)$', views.dirLevelTwo, name='dirLevelTwo')	
]