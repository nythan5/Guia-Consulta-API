from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

app_name = 'users'

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_create_list'),
    path('<int:pk>', UserRetrieveUpdateDestroyView.as_view(),
         name='user_retrieve_update_destroy')

]
