from rest_framework import serializers as srz
from mainApp.models import User

class UserSerializer(srz.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'email',
			'password',
			'last_name',
			'first_name',
		]

class EthSettingsSerializer(srz.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'eth_token',
			'eth_adress',
		]

class EthDataSerializer(srz.Serializer):
	ethRate = srz.CharField(max_length=200)
	balance = srz.CharField(max_length=200)
	lastBlockData = srz.DictField(child=srz.CharField())