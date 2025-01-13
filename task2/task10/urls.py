from django.urls import path
from django.contrib.auth import views


urlpatterns = [
    path("sign-in/", views.LoginView.as_view(template_name='my_custom_template.html'), name="sign-in"),
]

