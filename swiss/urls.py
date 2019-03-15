from . import views
from django.conf.urls import *

urlpatterns=[
	url(r'^index/',views.index,name="index"),
	url(r'^getram/',views.ram,name="ram"),
	url(r'^sendmessage/',views.sendmessage,name="sendmessage"),
	url(r'^ls/',views.ls,name="ls"),
]
