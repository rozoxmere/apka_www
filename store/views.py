from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Osoba, Druzyna
from .serializers import OsobaSerializer, DruzynaSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
def osoba_list(request):
    if request.method == "GET":
        persons = Osoba.objects.filter(wlasciciel = request.user).all()
        serializer = OsobaSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def osoba_detail(request, pk):
    try:
        person = Osoba.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        person = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(person)
        return Response(serializer.data)
@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_delete(request, pk):
    try:
        person = Osoba.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["PUT"])

def osoba_update(request, pk):
    try:
        person = Osoba.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = OsobaSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
