from . import endpoints

# Django
from django.urls import path


urlpatterns = [
    path("users", endpoints.GetUsers.as_view(), name="login"),
	path("users/register", endpoints.RegisterUser.as_view(), name="register"),
	path("users/update", endpoints.UpdateUser.as_view(), name="update"),
]
