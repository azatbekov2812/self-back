from django.contrib.auth.models import User
# Create your views here.
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import UserSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class CustomObtainJwtIin(ObtainJSONWebToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            username = data.get('username')
            password = data.get('password')

            user = User.objects.filter(username=username).first()
            if not user:
                user = User.objects.create_user(username=username, password=password)
            else:
                if not user.check_password(password):
                    return Response({'success': False,
                                     'token': 'Incorrect password',
                                     'user': username},
                                    status=status.HTTP_200_OK)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            user = UserSerializer(user).data
            return Response({'success': True,
                             'token': token,
                             'user': user},
                            status=status.HTTP_200_OK)
        except Exception as e:
            # send_mail('error: ecp', str(e) + '------' + str(request.data), settings.EMAIL_HOST_USER,
            #          [settings.EMAIL_HOST_USER])
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
