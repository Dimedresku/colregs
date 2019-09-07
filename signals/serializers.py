from rest_framework import serializers
from .models import Signals

class SignalsListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Signals
		fields = ('id', 'img')

class SignalDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Signals
		fields = '__all__'