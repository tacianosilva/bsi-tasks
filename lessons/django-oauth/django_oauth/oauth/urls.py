from django.urls import path
from .views import RoomListView, MessageListView, MessageCreateView, DebugOAuthView, oauth_callback

urlpatterns = [
    path('api/rooms/', RoomListView.as_view(), name='api_rooms'),
    path('api/rooms/<int:room_id>/messages/', MessageListView.as_view(), name='api_room_messages'),
    path('api/messages/new/', MessageCreateView.as_view(), name='api_create_message'),
    path('api/debug/', DebugOAuthView.as_view()),
    path('callback/', oauth_callback, name='oauth_callback'),
]
