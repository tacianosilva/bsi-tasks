from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
from oauth2_provider.models import AccessToken
from django_oauth.chat.models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from django.http import HttpResponse

class RoomListView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    required_scopes = ['read']

    def get(self, request):
        print("User:", request.user)
        print("Scopes:", getattr(request, 'scopes', None))
        token_str = str(request.auth)
        token = AccessToken.objects.get(token=token_str)
        print("AccessToken.scope:", token.scope)
        print("request.scopes:", getattr(request, 'scopes', None))
        rooms = Room.objects.all()
        data = RoomSerializer(rooms, many=True).data
        return Response(data)

class MessageListView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Message.objects.filter(room__id=room_id)

class MessageCreateView(CreateAPIView):
    serializer_class = MessageSerializer

class DebugOAuthView(APIView):
    authentication_classes = [OAuth2Authentication]

    def get(self, request):
        return Response({
            'user': str(request.user),
            'auth': str(request.auth),
            'scopes': getattr(request, 'scopes', None),
        })

def oauth_callback(request):
    code = request.GET.get('code')
    return HttpResponse(f"Authorization code: {code}")
