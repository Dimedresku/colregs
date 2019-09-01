from rest_framework import serializers
from .models import Flags

class FlagsListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flags
		fields = ('id', 'symbol')

class FlagDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flags
		fields = '__all__'