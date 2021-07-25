from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.utils.translation import gettext as _
from django.conf.urls.i18n import i18n_patterns



from eptSN import views

urlpatterns = [
    url(r'^ept_admin/', admin.site.urls),    
]

urlpatterns += i18n_patterns(
    url(r'^', include(('eptSN.urls', 'eptSN'),namespace='eptSN')),
    #prefix_default_language=False
)




admin.site.site_header=_("EPT_SN ADMINISTRATION")
admin.site.site_title=_("EPT_SN")
admin.site.index_title=_("Interface d'administration EPT_SN")