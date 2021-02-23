from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from empresas.models import Empresa
from .serializers import EmpresaSerializer

class EmpresaViewSet(ModelViewSet):
    serializer_class = EmpresaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        cnpj = self.request.query_params.get('cnpj', None)
        queryset = Empresa.objects.all()
        if id:
            queryset = Empresa.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome=nome)

        if cnpj:
            queryset = queryset.filter(cnpj=cnpj)

        return queryset
