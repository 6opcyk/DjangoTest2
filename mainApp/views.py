from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from mainApp.models import User
from mainApp.serializers import UserSerializer, EthSettingsSerializer, EthDataSerializer
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
import requests
import re

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserSerializer

class UserUpdateAPIView(UpdateAPIView):
	serializer_class = EthSettingsSerializer
	queryset = User.objects.all()

class UserGetEthAPIView(APIView):
	def get(self, request, pk):
		user = User.objects.get(pk = pk)

		url = f"https://api.etherscan.io/api?module=stats&action=ethprice&apikey={user.eth_token}"
		ethRate = requests.get(url).json()["result"]["ethusd"]

		url = f"https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey={user.eth_token}"
		lastBlockNum = requests.get(url).json()["result"]

		url = f"http://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={lastBlockNum}&boolean=true&apikey={user.eth_token}"
		lastBlockData = requests.get(url).json()["result"]
		lastBlockData.pop("transactions")
		lastBlockData.pop("uncles")

		url = f"http://api.etherscan.io/api?module=account&action=balance&address={user.eth_adress}&tag=latest&apikey={user.eth_token}"
		balance = requests.get(url).json()["result"]

		data = {
		"ethRate": ethRate,
		"balance": balance,
		"lastBlockData": lastBlockData
		}

		serializer = EthDataSerializer(data=data)
		serializer.is_valid()
		return Response(serializer.validated_data)
		
		

		
