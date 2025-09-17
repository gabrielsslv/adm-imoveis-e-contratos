from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome

class Imovel(models.Model):
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.endereco} - {self.cidade}"

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contratos')
    imovel = models.ForeignKey(Imovel, on_delete=models.PROTECT, related_name='contratos')
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    arquivo_pdf = models.FileField(upload_to='contratos/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo')

    def __str__(self):
        return f"Contrato: {self.cliente.nome} - {self.imovel.endereco}"
