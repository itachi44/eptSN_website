from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from .api import etudiantViewSet,etudiantClasseViewSet


#API ROUTER FOR ENDPOINTS

router= DefaultRouter()
router.register(r'etudiants',etudiantViewSet,'Etudiant')
router.register(r'infosetudiants',etudiantClasseViewSet,'Etudiant')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^contacts/itinerary$', views.ajax, name='ajax'),
    url(r'^switch_lang/(?P<lang_code>\w+)?/(?P<page>\w+)?$', views.switch_lang, name='switch_lang'),
    url(r'^logOut$', views.logOut, name='logOut'),
    url(r'departements/(?P<department>\w+)', views.goToDept, name='goToDept')
]
