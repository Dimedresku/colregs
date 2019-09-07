from django.shortcuts import render
from rest_framework import generics
from .serializers import SignalDetailsSerializer, SignalsListSerializer
from .models import Signals

class SignalsListView(generics.ListAPIView):
	serializer_class =SignalsListSerializer 
	queryset = Signals.objects.all()

class SignalDetailView(generics.ListAPIView):
	serializer_class = SignalDetailsSerializer
	
	def get_queryset(self):
		id = self.kwargs['pk']
		return Signals.objects.filter(id=id)

	
