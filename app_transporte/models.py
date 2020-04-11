from django.db import models

class Cargo(models.Model):
    nome= models.CharField(max_length = 150, blank= True, null = True)
    sigla= models.CharField(max_length= 10, blank= True, null= True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.sigla)

class Departamento(models.Model):
    nome= models.CharField(max_length= 150, blank= True, null= True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome= models.CharField(max_length= 150, blank= True, null= True)
    matricula= models.CharField(max_length= 150, blank= True, null= True)
    departamento= models.ForeignKey(Departamento, on_delete = models.CASCADE, blank = True, null = True)
    
    def __str__(self):
        return '{} - {}'.format(self.nome, self.departamento)

class Veiculo(models.Model):
    descricao= models.CharField(max_length=150, blank= True, null= True)
    modelo= models.CharField(max_length= 150, blank= True, null= True)
    placa= models.CharField(max_length= 150, blank= True, null= True)

    def __str__(self):
        return '{} - {}'.format(self.modelo, self.placa)

class Solicitacao(models.Model):
    origem= models.CharField(max_length= 150, blank= True, null= True)
    destino= models.CharField(max_length= 150, blank= True, null= True)
    data_hora= models.DateTimeField()
    solicitacao= models.ForeignKey(Funcionario, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return '{} - {}'.format(self.destino, self.data_hora)

class Atendimento(models.Model):
    solicitacao= models.ForeignKey(Solicitacao, on_delete = models.CASCADE, blank = True, null = True)
    veiculo= models.ForeignKey(Veiculo, on_delete = models.CASCADE, blank = True, null = True)
    motorista= models.ForeignKey(Funcionario, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return '{} - {}'.format(self.motorista, self.veiculo)