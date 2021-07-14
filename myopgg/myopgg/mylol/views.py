from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import tier
from . import odds
from . import ingame

from django.db.models import Q

# Create your views here.
# 실제적인 api와 같은 기능으로 특정 url로 들어왔을 때 views.py를 호출하여 views.py가 사용자에게 해당하는 내용을 보여줍니다

class getTier(APIView):
    def get(self, request, format=None):
        summoner_name = request.query_params.get('summoner_name', None)
        if summoner_name is not None:
            api_key = models.Riot.objects.get().api_key
            summoner_tier = tier.getTier(api_key,summoner_name)
            response_data = {}
            response_data['tier'] = summoner_tier
            return Response(data=response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class getRate(APIView):
    def get(self, request, format=None):
        summoner_name = request.query_params.get('name', None)
        if summoner_name is not None:
            api_key = models.Riot.objects.get().api_key
            summoner_rate = odds.getOdds(api_key,summoner_name)
            response_data = {}
            response_data['rate'] = summoner_rate
            return Response(data=response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class getIngame(APIView):
    def get(self, request, format=None):
        summoner_name = request.query_params.get('summoner_name', None)
        if summoner_name is not None:
            api_key = models.Riot.objects.get().api_key
            summoner_ingame = ingame.getStatus(api_key,summoner_name)
            response_data = {}
            response_data['ingame'] = summoner_ingame
            return Response(data=response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
