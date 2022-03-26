from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('inventorysnippets/', views.InventorySnippetList.as_view()),
    path('inventorysnippet/<int:pk>', views.InventorySnippetDetail.as_view()),
    path('mechanicsnippets/', views.MechanicViewSet.as_view({'get': 'list'})),
    path('mechanicpostnippets/', views.MechanicViewSet.as_view({'post': 'create'})),
    path('servicesnippets/', views.ServicesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)