from rest_framework import serializers
from store.models import Osoba, Druzyna, Months, Product
import datetime
class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=Months.choices, default=Months.choices[0][0])
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all(), allow_null=True)


    def validate_imie(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Nazwa imienia powinna zaczynac sie z duzej litery!")
        return value

    def validate_data_dodania(self, value):
        if value > datetime.today():
            raise serializers.ValidationError("Miesiac dodania nie moze byc z przyszlosci")
        return value
    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get("imie", instance.imie)
        instance.nazwisko = validated_data.get("nazwisko", instance.nazwisko)
        instance.miesiac_urodzenia = validated_data.get("miesiac_urodzenia", instance.miesiac_urodzenia)
        instance.druzyna = validated_data.get("druzyna", instance.druzyna)
        instance.save()
        return instance

class DruzynaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True)
    kraj = serializers.CharField(required=True)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get("nazwa", instance.nazwa)
        instance.kraj = validated_data.get("kraj", instance.kraj)
        instance.save()
        return instance

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "amount", "price"]
        read_only_fields = ["id"]