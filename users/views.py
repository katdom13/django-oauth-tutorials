from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.http import HttpResponse
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import GroupSerializer, UserSerializer


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
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]

    def create(self, request, *args, **kwargs):
        request.data["password"] = make_password(self.request.data["password"])
        return super().create(request, *args, **kwargs)


class GroupList(generics.ListAPIView):
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ["groups"]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
