from django.urls import path, include
from store import views

urlpatterns = [
    path('persons/', views.osoba_list),
    path('persons/<int:pk>', views.osoba_detail),
    path('persons/delete/<int:pk>/', views.osoba_delete),
    path('persons/update/<int:pk>/', views.osoba_update),
    path('persons/filter/<str:name>', views.osoba_filter),
    path('team/<int:pk>', views.druzyna_detail),
    path('team/<int:pk>/czlonkowie', views.druzyna_members),
    path('team/', views.druzyna_list)

]
#