from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from app import resources

v1_api = Api(api_name='v1')

v1_api.register(resources.OutletResource())
v1_api.register(resources.WifiResource())
v1_api.register(resources.UserResource())
v1_api.register(resources.LocationResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freeG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
