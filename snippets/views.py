from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import status, viewsets
from rest_framework.decorators import action

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response

from .models import Snippet

# from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer


class SnippetViewset(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    lookup_field = "pk"

    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # It would be nice to reuse these views and support token handling.
    # Instead of reworking those classes to be ProtectedResourceView based,
    # the solution is much simpler than that.

    # The key is setting a class attribute to override the
    # default permissions_classes with something
    # that will use Django OAuth Toolkit's Access Token properly.
    permission_classes = [TokenHasReadWriteScope]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(
        methods=["get"], detail=True, renderer_classes=[StaticHTMLRenderer], url_path=r"highlight"
    )
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
