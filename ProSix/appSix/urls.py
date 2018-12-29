from django.conf.urls import url
from appSix import views


app_name = 'appSix'

urlpatterns = [
    url(r'^Register/',views.Register,name='Register'),

]
