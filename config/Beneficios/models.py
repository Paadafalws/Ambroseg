from django.db import models

class Cliente(models.Model):
    escolhasstatus =(
        ('Concluido (Externo)', 'Concluido (Externo)'),
        ('Concluido', 'Concluido'),
        ('Atendimento (Externo)', 'Atendimento (Externo)'),
        ('Cancelado','Cancelado'),
        ('Atendimento','Atendimento')
    )

    canal = models.CharField(max_length=100)
    data_solicitacao = models.DateField()
    data_finalizacao = models.DateField()

    nivel = models.CharField(max_length=15, choices=escolhasstatus, blank=False, null=False,default=' ')
    nome_beneficiario = models.CharField(max_length=100)

    data_nascimento = models.DateField()

    cartao_cpf = models.CharField(max_length=20)
    empresa = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    convenio = models.CharField(max_length=100)
    atendimento = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    especialidade_exame = models.CharField(max_length=100)
    doutor = models.CharField(max_length=100)
    data_procedimento = models.DateField()
    data_lembrete = models.DateField()
    data_cirurgia3 = models.DateField()
    data_cirurgia4 = models.DateField()
    status_lembrete = models.CharField(max_length=100)
    horario_procedimento = models.CharField(max_length=100)
    local_procedimento = models.CharField(max_length=100)
    protocolo = models.CharField(max_length=100)
    observacoes = models.TextField()


    def __str__(self):
        return self.nome_beneficiario