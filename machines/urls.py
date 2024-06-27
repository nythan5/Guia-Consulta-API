from django.urls import path
from .views import ModalitieListCreateView, ModalitieRetrieveUpdateDestroyView

app_name = 'machines'

urlpatterns = [
    path('modalities/', ModalitieListCreateView.as_view(),
         name='modalitie_create_list'),
    path('modalities/<int:pk>', ModalitieRetrieveUpdateDestroyView.as_view(),
         name='modalitie_retrieve_update_destroy'),
]
