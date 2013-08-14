from django.conf.urls import patterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from index.views import index


urlpatterns = patterns('',
    ('^index/+', index),

    # Examples:
    # url(r'^$', 'dangoTest.views.home', name='home'),
    # url(r'^dangoTest/', include('dangoTest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
