from rest_framework.viewsets import ModelViewSet
from .serializer import AceSerializer
from .models import Ace
# from django import http
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework import mixins
# Create your views here.


class AceViewSet(ModelViewSet):
    queryset = Ace.objects.filter(is_active=True)
    serializer_class = AceSerializer

    def destroy(self, request, *args, **kwargs):
        ace = self.get_object()
        ace.is_active = False
        ace.save()

        # return http.HttpResponseRedirect(redirect_to='ace-list')
        return redirect('/api/v1/')


class AceListAllViewSet(ModelViewSet):
    queryset = Ace.objects.all()
    serializer_class = AceSerializer
