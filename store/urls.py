from django.urls import path, include
from store import views

urlpatterns = [
    path('persons/', views.ListUsers.as_view()),
    path('persons/<int:pk>', views.OsobaDetail.as_view()),
    path('persons/filter/<str:name>', views.osoba_filter),
    path('team/<int:pk>', views.druzyna_detail),
    path('team/', views.druzyna_list)

]
#