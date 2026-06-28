from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # path para sa get_cars
    path('get_cars', views.get_cars, name='getcars'),
    
    # # path para sa registration
    # path(route='register', view=views.registration, name='register'),

    # # path para sa login
    # path(route='login', view=views.login_user, name='login'),

    # # path para sa dealer reviews view

    # # path para sa add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)