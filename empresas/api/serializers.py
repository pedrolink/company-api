from rest_framework.serializers import ModelSerializer
from empresas.models import Empresa

class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'nome', 'cnpj')