from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from plataforma.models import Plataforma
from .serializers import PlataformaSerializer

class PlataformaViewSet(ModelViewSet):
    serializer_class = PlataformaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        funcionario = self.request.query_params.get('funcionario', None)
        id_empresas = self.request.query_params.get('id_empresas', None)
        id_usuario = self.request.query_params.get('id_usuario', None)
        queryset = Plataforma.objects.all()
        if id:
            queryset = Plataforma.objects.filter(pk=id)

        if funcionario:
            queryset = queryset.filter(funcionario=funcionario)

        if id_empresas:
            queryset = queryset.filter(id_empresas=id_empresas)

        if id_usuario:
            queryset = queryset.filter(id_usuario=id_usuario)

        return queryset