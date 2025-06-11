from django.db import models
from django.core.validators import RegexValidator

class Contato(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    telefone = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Formato inválido")],
        verbose_name="Telefone"
    )
    email = models.EmailField(unique=True, verbose_name="E-mail")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.nome} - {self.email}"
