from rest_framework.serializers import ModelSerializer
from plataforma.models import Plataforma
from empresas.api.serializers import EmpresaSerializer
from usuarios.api.serializers import UsuarioSerializer

class PlataformaSerializer(ModelSerializer):
    id_empresas = EmpresaSerializer(many=True)
    id_usuario = UsuarioSerializer()
    class Meta:
        model = Plataforma
        fields = ('id', 'funcionario', 'id_empresas', 'id_usuario')