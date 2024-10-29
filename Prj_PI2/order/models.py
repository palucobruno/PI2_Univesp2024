# Arquivo de modelo de Order 

from django.db import models
from django.urls import reverse

class Pedidos (models.Model):
    id_pedidos = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True, blank=False, help_text='Insira um nome valido: Nome e Sobrenomes')
    email = models.EmailField(max_length=254, null=True, blank=False, help_text='Insira um e-mail valido: usuario@dominio')
    telefone = models.CharField(max_length=11, null=True, blank=True)
    arquivo = models.ImageField(null=True, blank=True)
    mensagem = models.CharField(max_length=255, null=True, blank=True)
    criacao = models.DateTimeField(null=True, blank=False, auto_now_add=True)    
    cpf_pagamento = models.PositiveBigIntegerField(null=True, blank=False, help_text='Insira o CPF do pagador.')
    cpf_envio = models.PositiveBigIntegerField(null=True, blank=True, help_text='Insira o CPF do cliente.')
    endereco = models.CharField(max_length=255, null=True, blank=True, help_text='Insira o endereço do cliente.')
    valor_produto = models.FloatField(null=True, blank=False, help_text='Insira o valor do produto cotado.')
    anotacoes = models.CharField(max_length=255, null=True, blank=True, help_text='Insira as anotacoes da cotacao')
    envio_orcamento = models.DateField(null=True, blank=True, help_text='Insira a data do envio do orcamento.')
    pagamento = models.DateField(null=True, blank=True, help_text='Insira a data do pagamento.')
    conclusao = models.DateField(null=True, blank=True, help_text='Insira a data de conclusao.')

    class Meta:
        ordering =['criacao']
        verbose_name = 'Pedidos recebidos'

    def __str__(self):
        return f'[{self.id_pedidos}]{self.nome}'

    def get_absolute_url(self):
        return reverse('detalhes-pedido', args=[str(self.id_pedidos)])