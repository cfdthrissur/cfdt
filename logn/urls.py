from django.conf.urls import url


from logn import views

urlpatterns = [
    url(r'^$',views.login_page),
    url(r'^login/$',views.login_page),
    url(r'^home/$', views.home_page),
]
