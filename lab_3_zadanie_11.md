#1
>>> store.models.Osoba.objects.all();        
<QuerySet [<Osoba: michal Adamczyk>, <Osoba: Adam Nowak>, <Osoba: Damian Zręba>]>

#2 
>>> store.models.Osoba.objects.get(id=3);             
<Osoba: Damian Zręba>
 
#3

>>> store.models.Osoba.objects.get(imie__regex=r'^A') 
<Osoba: Adam Nowak>

#4 
>>> store.models.Osoba.objects.order_by("druzyna").values("druzyna").distinct()                      
<QuerySet [{'druzyna': None}, {'druzyna': 1}, {'druzyna': 2}]>

#5 
>>> store.models.Druzyna.objects.order_by("-nazwa")      
<QuerySet [<Druzyna: Wilki (DE)>, <Druzyna: Red Tigers (PL)>]>

