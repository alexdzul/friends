from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('friends.apps.phonebook.urls', namespace='phonebook')),
    url(r'^admin/', include(admin.site.urls)),
]
