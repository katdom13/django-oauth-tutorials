"""secure_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewset
from users.views import ApiEndpoint, GroupList, UserViewset, secret_page

router = DefaultRouter()

router.register("users", UserViewset, basename="user")
router.register("snippets", SnippetViewset, basename="snippet")

urlpatterns = [
    path("admin/", admin.site.urls),
    # This will make available endpoints to authorize, generate token and create OAuth applications.
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    # If you're intending to use the browsable API,
    # you'll probably also want to add REST framework's login and logout views.
    path("api-auth/", include("rest_framework.urls")),
    # an example resource endpoint
    path("api/hello", ApiEndpoint.as_view()),
    path("api/secret", secret_page, name="secret"),
    # Groups url
    path("groups/", GroupList.as_view(), name="group-list"),
]

urlpatterns += router.urls
