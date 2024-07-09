from .models import Modalitie
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ModalitieSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ModalitieListCreateView(ListCreateAPIView):
    queryset = Modalitie.objects.all()
    serializer_class = ModalitieSerializer
    # permission_classes = [IsAuthenticated]


class ModalitieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Modalitie.objects.all()
    serializer_class = ModalitieSerializer
    # permission_classes = [IsAuthenticated]
