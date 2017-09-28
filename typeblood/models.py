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

	Doador_id = models.AutoField(primary_key=True, verbose_name = 'ID') 
	Nome = models.CharField(max_length = 100, verbose_name = 'Nome')
	Idade = models.PositiveSmallIntegerField(verbose_name = 'Idade')
	Email = models.CharField(max_length = 100, verbose_name = 'Email')
	Telefone = models.CharField(max_length = 50, verbose_name = 'Telefone')
	Tipo_Sanguineo = models.CharField(
		max_length = 4,
		choices=TIPO_CHOICES,
		verbose_name = 'Tipo de Sangue',
	)	
	Data_cadastro = models.DateTimeField(
		default=timezone.now, verbose_name = 'Data do Cadastro')
	Ultima_Doacao = models.DateTimeField(
		blank=True, null=True, verbose_name = 'Data da Última Doação')
	Situacao = models.CharField(
		max_length = 25,
		choices=SITUACAO_CHOICES,
		verbose_name = 'Situação da Última Doação',
	)
	Observacoes = models.TextField(verbose_name = 'Observações')

	def publish(self):
		self.Ultima_Doacao = timezone.now()
		self.save()

	def __str__(self):
		return u'%s   %s' % (self.Nome, self.Tipo_Sanguineo)