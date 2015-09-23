from django.conf.urls import patterns, url
from .views import ContactList, ContactNew, ContactDelete, ContactEdit


urlpatterns = patterns('',
                       url(r'^$', ContactList.as_view(), name="list"),
                       url(r'^new/$', ContactNew.as_view(), name="new"),
                       url(r'^delete/(?P<contact_id>.*)/$', ContactDelete.as_view(), name="delete"),
                       url(r'^edit/(?P<contact_id>.*)/$', ContactEdit.as_view(), name="edit"),
                       )
