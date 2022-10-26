# Model Osoba
```python
from store.models import Osoba, Druzyna
from store.serializers import OsobaSerializer, DruzynaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

#Model osoba
osoba = Osoba(imie = "Adam", nazwisko = "Bąk", miesiac_urodzenia = 1)
# <Osoba: Adam Bąk>
osoba.save()
#
serializer = OsobaSerializer(osoba)
serializer.data
# {'id': 5, 'imie': 'Adam', 'nazwisko': 'Bąk', 'miesiac_urodzenia': 1, 'druzyna': None}
content = JSONRenderer().render(serializer.data)
content
# b'{"id":5,"imie":"Adam","nazwisko":"B\xc4\x85k","miesiac_urodzenia":1,"druzyna":null}'
import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = OsobaSerializer(data = data)
deserializer.is_valid()
# True

deserializer.fields
# {'id': IntegerField(read_only=True), 'imie': CharField(required=True), 'nazwisko': CharField(required=True), 'mi
# esiac_urodzenia': ChoiceField(choices=[(1, 'Styczen'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecien'), (5, 'Maj'), 
# (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpien'), (9, 'Wrzesien'), (10, 'Pazdziernik'), (11, 'Listopad'), (12, 'G
# rudzien')], default=1), 'druzyna': PrimaryKeyRelatedField(allow_null=True, queryset=<QuerySet [<Druzyna: Red Tig
# ers (PL)>, <Druzyna: Wilki (DE)>]>)}
deserializer.validated_data
# OrderedDict([('imie', 'Adam'), ('nazwisko', 'Bąk'), ('miesiac_urodzenia', 1), ('druzyna', None)])
deserializer.save()
# <Osoba: Adam Bąk>
deserializer.data
# {'id': 7, 'imie': 'Adam', 'nazwisko': 'Bąk', 'miesiac_urodzenia': 1, 'druzyna': None}

```
# Model Druzyna
```python
from store.models import Osoba, Druzyna
from store.serializers import OsobaSerializer, DruzynaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

team = Druzyna(nazwa="Bialo Czerwoni", kraj="PL")
team.save()
serializer = DruzynaSerializer(team)
serializer.data
#{'id': 3, 'nazwa': 'Bialo Czerwoni', 'kraj': 'PL'}
content = JSONRenderer().render(serializer.data)
content
# b'{"id":3,"nazwa":"Bialo Czerwoni","kraj":"PL"}'
import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = DruzynaSerializer(data=data)
deserializer.is_valid()
# True
deserializer.validated_data
# OrderedDict([('nazwa', 'Bialo Czerwoni'), ('kraj', 'PL')])

deserializer.save()
deserializer.data
# {'id': 5, 'nazwa': 'Bialo Czerwoni', 'kraj': 'PL'}


```