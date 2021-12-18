from django.db import models

class Portofolio(models.Model):
	image = models.FileField(upload_to = 'portofolios/')
	titre = models.CharField(max_length = 100)
	categorie = models.CharField(max_length = 100, choices = (
			('Shoot','Shooting photo'),
			('Design','Design'),
			('Web','Web'),
			('Logiciel','Logiciel'),
			('Application mobile','Application mobile'),
			('Conception des badges','Conception des badges'),
			('Conception CV professionnels','Conception CV professionnels'),
			('Formations à domicile','Formations à domicile'),
			('Autre ...','Autre ...'),
		))
	url = models.URLField(null = True, blank = True)
	description = models.TextField(null = True, blank = True)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '{} - {}'.format(self.titre, self.categorie)

class Contact(models.Model):
	nom = models.CharField(max_length = 50)
	email = models.EmailField(null = True, blank = True)
	tel = models.CharField(max_length = 30)
	objet = models.CharField(max_length = 30)
	texte = models.TextField()

	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f'{self.nom} - {self.objet}'