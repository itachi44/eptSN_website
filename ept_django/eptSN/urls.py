from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^contacts/itinerary$', views.ajax, name='ajax'),
    url(r'^switch_lang/(?P<lang_code>\w+)?/(?P<page>\w+)?$', views.switch_lang, name='switch_lang'),
    url(r'^logOut$', views.logOut, name='logOut'),
    url(r'^(?P<department>\w+)', views.goToDept, name='goToDept')
]
