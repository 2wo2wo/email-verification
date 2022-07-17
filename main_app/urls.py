from django.urls import path,include
from . import views
from django_email_verification import urls as email_urls
print(include(email_urls))
urlpatterns = [
    # path('contacts/', views.send_mailing, name='email'),
    path('registration/', views.registration, name='registration'),
    path('registration/email/', include(email_urls)),
]