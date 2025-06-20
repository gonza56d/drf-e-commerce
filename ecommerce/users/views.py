from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from ecommerce.users.models import User
from ecommerce.users.serializers import UserSerializer, UserSignUpSerializer


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSignUpSerializer
        return UserSerializer

    @extend_schema(
        request=UserSignUpSerializer,
        responses={201: UserSignUpSerializer, 400: None},
    )
    def create(self, request: Request) -> Response:
        """Sign up a new user."""
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            pass
        serializer.save()
        return Response(serializer.data, status=201)
