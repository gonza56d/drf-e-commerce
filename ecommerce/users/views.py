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

    @extend_schema(
        request=UserSignUpSerializer,
        responses={201: UserSignUpSerializer, 400: None},
    )
    def create(self, request: Request) -> Response:
        """Sign up a new user."""
        serializer = UserSignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=400,
                data={
                    k: [
                        {
                            'message': str(error_detail).capitalize(),
                            'code': error_detail.code,
                        } for error_detail in v
                    ] for k, v in serializer.errors.items()
                }
            )
        serializer.save()
        request.data['password'] = '***'
        return Response(request.data, status=201)
