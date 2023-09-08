from rest_framework.viewsets import ModelViewSet
from .serializer import AceSerializer
from .models import Ace

# Create your views here.
class AceViewSet(ModelViewSet):
    queryset = Ace.objects.all()
    serializer_class = AceSerializer