from django.shortcuts import render
from rest_framework import generics
from .serializers import FlagDetailsSerializer, FlagsListSerializer
from .models import Flags

class FlagsListView(generics.ListAPIView):
	serializer_class = FlagsListSerializer 
	queryset = Flags.objects.all()

class FlagDetailView(generics.ListAPIView):
	serializer_class = FlagDetailsSerializer
	
	def get_queryset(self):
		id = self.kwargs['pk']
		return Flags.objects.filter(id=id)

	
