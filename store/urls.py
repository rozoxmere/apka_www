from django.urls import path, include
from store import views

urlpatterns = [
    path('persons/', views.osoba_list),
    path('persons/<int:pk>', views.osoba_detail),
    path('persons/<int:pk>/delete', views.osoba_delete),
    path('persons/<int:pk>/update', views.osoba_update),
    path('persons/filter/<str:name>', views.osoba_filter),
    path('team/<int:pk>', views.druzyna_detail),
    path('team/', views.druzyna_list)

]
#