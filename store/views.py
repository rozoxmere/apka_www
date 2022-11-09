from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Osoba, Druzyna
from .serializers import OsobaSerializer, DruzynaSerializer


class ListUsers(APIView):
    def get(self, request):
        persons = Osoba.objects.all()
        serializer = OsobaSerializer(persons, many=True)
        return Response(serializer.data)


class OsobaDetail(APIView):
    person = None
    def __init__(self, request, pk):
        try:
            person = Osoba.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        person = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = OsobaSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def osoba_filter(request, name):
    try:
        persons = Osoba.objects.filter(imie__contains=name)
        print(persons)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = OsobaSerializer(persons, many=True)
        return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def druzyna_detail(request, pk):
    try:
        team = Druzyna.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        team = Druzyna.objects.get(pk=pk)
        serializer = DruzynaSerializer(team)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = DruzynaSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def druzyna_list(request):
    if request.method == "GET":
        teams = Druzyna.objects.all()
        serializer = DruzynaSerializer(teams, many=True)
        return Response(serializer.data)
