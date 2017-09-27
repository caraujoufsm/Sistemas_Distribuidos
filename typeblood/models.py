from django.db import models
from django.utils import timezone

class Cadastro(models.Model):

	TIPO_CHOICES =  (
		('A-','A-'),
		('A+','A+'),
		('B-','B-'),
		('B+','B+'),
		('AB-','AB-'),
		('AB+','AB+'),
		('O-','O-'),
		('O+','O+'),
	)


	SITUACAO_CHOICES = (
		('Sem Problemas','Sem Problemas'),
		('Problemas Momentâneos','Problemas Momentâneos'),
		('Problemas Graves', 'Problemas Graves'),
	)

	Doador_id = models.AutoField(primary_key=True) 
	Nome = models.CharField(max_length = 100)
	Idade = models.PositiveSmallIntegerField()
	Email = models.CharField(max_length = 100)
	Telefone = models.CharField(max_length = 50)
	Tipo_Sanguineo = models.CharField(
		max_length = 4,
		choices=TIPO_CHOICES,
	)	
	Data_cadastro = models.DateTimeField(
		default=timezone.now)
	Ultima_Doacao = models.DateTimeField(
		blank=True, null=True)
	Situacao = models.CharField(
		max_length = 25,
		choices=SITUACAO_CHOICES,
	)
	Observacoes = models.TextField()

	def publish(self):
		self.Ultima_Doacao = timezone.now()
		self.save()

	def __str__(self):
		return u'%s   %s' % (self.Nome, self.Tipo_Sanguineo)