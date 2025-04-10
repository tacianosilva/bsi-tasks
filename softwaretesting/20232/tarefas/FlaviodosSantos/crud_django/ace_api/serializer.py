from rest_framework.serializers import ModelSerializer
from .models import Ace

class AceSerializer(ModelSerializer):
    class Meta:
        model = Ace
        # fields = ('nome', 'matricula', 'zona')
        fields = '__all__'