from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Contato
from .serializers import ContatoSerializer, ContatoListSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ContatoListSerializer
        return ContatoSerializer
    
    def get_queryset(self):
        queryset = Contato.objects.all()
        nome = self.request.query_params.get('nome', None)
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    @action(detail=False, methods=['get'])
    def buscar(self, request):
        termo = request.query_params.get('q', '')
        if not termo:
            return Response({'erro': 'Parâmetro q é obrigatório'}, status=400)
        
        contatos = Contato.objects.filter(
            Q(nome__icontains=termo) | Q(telefone__icontains=termo) | Q(email__icontains=termo)
        )
        serializer = ContatoListSerializer(contatos, many=True)
        return Response(serializer.data)
