from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.users.serializers import UserSignUpSerializer


class UsersAPIView(APIView):

    def post(self, request: Request) -> Response:
        """Sign up a new user."""
        serializer = UserSignUpSerializer(data=request.data)
        if not serializer.is_valid():
            pass
        user = serializer.save()
        return user
