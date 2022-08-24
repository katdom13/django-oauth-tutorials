from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView


# You have an authorization server and we want it to provide an API
# to access some kind of resources. We don’t need an actual resource,
# so we will simply expose an endpoint protected with OAuth2:
# let’s do it in a class based view fashion!
class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2')
