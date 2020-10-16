from django.conf.urls import url

urlpatterns = [url(r'^hello/', 'myapp.views.hello', name='hello')]
