from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from TTRS import settings
from tourist import views

urlpatterns = [
    path('get_tourism_data', views.get_tourism_data, name="get_tourism_data"),
    path('list_tourism_data', views.list_tourism_data, name="list_tourism_data"),
    path('category_filter', views.category_filter, name="category_filter"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('user_dashboard', views.user_dashboard, name="user_dashboard"),

    path('sign_up', views.sign_up, name="sign_up"),
    path('login', views.login, name="login"),
    path('signout', views.signout, name="signout"),

    path('', views.index, name="index")
]
if settings.DEBUG:
   urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_URL)
   urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

