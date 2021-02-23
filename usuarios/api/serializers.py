from rest_framework.serializers import ModelSerializer
from usuarios.models import Usuario
from empresas.api.serializers import EmpresaSerializer

class UsuarioSerializer(ModelSerializer):
    empresa = EmpresaSerializer(many=True)
    class Meta:
        model = Usuario
        fields = ('id', 'usuario', 'nome', 'empresa', 'empresa')