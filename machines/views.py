from .models import Modalitie
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ModalitieSerializer


# Create your views here.

class ModalitieListCreateView(ListCreateAPIView):
    queryset = Modalitie.objects.all()
    serializer_class = ModalitieSerializer


class ModalitieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Modalitie.objects.all()
    serializer_class = ModalitieSerializer
