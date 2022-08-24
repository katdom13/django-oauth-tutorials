from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework import viewsets

from users.serializers import UserSerializer

from .models import User


# You have an authorization server and we want it to provide an API
# to access some kind of resources. We don’t need an actual resource,
# so we will simply expose an endpoint protected with OAuth2:
# let’s do it in a class based view fashion!
class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, OAuth2")


# The authentication backend will run smoothly with,
# for example, login_required decorators,
# so that you can have a view like this in your views.py module:
@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse("Secret contents!", status=200)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
