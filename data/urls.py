from django.conf.urls import url


from data import views

urlpatterns = [
    url(r'^test/$', views.test_page),
]
