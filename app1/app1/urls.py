from django.conf.urls import patterns, include, url

from django.contrib import admin

from app1.views import olaMundo, dataAtual, dataMais
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^olaMundo/', olaMundo),
    url(r'^dataAtual/', dataAtual),
    url(r'^$', olaMundo),
    url(r'^data/(\d+)/$', dataMais),
    url(r'^admin/', include(admin.site.urls)),
)
