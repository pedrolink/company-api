from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from usuarios.models import Usuario
from plataforma.models import Plataforma
from .serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'usuario'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        usuario = self.request.query_params.get('usuario', None)
        nome = self.request.query_params.get('nome', None)
        empresa = self.request.query_params.get('empresa', None)
        queryset = Usuario.objects.all()
        if id:
            queryset = Usuario.objects.filter(pk=id)

        if usuario:
            queryset = queryset.filter(usuario=usuario)

        if nome:
            queryset = queryset.filter(nome=nome)

        if empresa:
            queryset = queryset.filter(empresa=empresa)
        return queryset