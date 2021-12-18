from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Portofolio
import requests
from django.conf import settings
from .forms import ContactForm

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from datetime import datetime

date_now = datetime.now()

date_now = date_now.strftime("%d, %b %Y à %Hh:%M:%S")


def home(request):

	shoot = Portofolio.objects.filter(categorie = 'Shoot').order_by('-id')[:8]
	design = Portofolio.objects.filter(categorie = 'Design').order_by('-id')[:8]
	web = Portofolio.objects.filter(categorie = 'Web').order_by('-id')[:8]
	logiciel = Portofolio.objects.filter(categorie = 'Logiciel').order_by('-id')[:8]

	template = 'services/index.html'
	context = {
		'shoot' : shoot,
		'design' : design,
		'web' : web,
		'logiciel' : logiciel,
	}
	return render(request, template, context)


def portofolio(request):

	shoot = Portofolio.objects.filter(categorie = 'Shoot').order_by('-id')
	design = Portofolio.objects.filter(categorie = 'Design').order_by('-id')
	web = Portofolio.objects.filter(categorie = 'Web').order_by('-id')
	logiciel = Portofolio.objects.filter(categorie = 'Logiciel').order_by('-id')

	template = 'services/portofolio.html'
	context = {
		'shoot' : shoot,
		'design' : design,
		'web' : web,
		'logiciel' : logiciel,
	}
	return render(request, template, context)

def about(request):
	template = 'services/about.html'
	context = {}
	return render(request, template, context)

def contact(request):

	if request.method == 'POST':

		nom = request.POST.get('nom')
		email_ = request.POST.get('email')
		tel = request.POST.get('tel')
		objet = request.POST.get('objet')
		texte = request.POST.get('texte')

		form = ContactForm(request.POST)
		data = request.POST
	

		if form.is_valid():

			recaptcha_response = request.POST.get('g-recaptcha-response')
			data = {
				'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response' : recaptcha_response
				}

			r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
			result = r.json()

			if result: #result['success']
				form.save()

				#envoie de mail
				# send_mail(
				# 	'Depuis le site de GAB : «'+objet+'»',
				# 	'Par '+nom+' (son téléphone : '+tel+') et son message " '+texte+' ".',
				# 	email_,
				# 	['exaucengango2@gmail.com'],
				# 	fail_silently=False,
				# )

				content = {
					'nom' : nom,
					'email' : email_,
					'tel' : tel,
					'objet' : objet,
					'texte' : texte,
				}

				html_content = render_to_string("services/mail.html", content)
				text_content = strip_tags(html_content)
				email = EmailMultiAlternatives(
					#objet
					'Depuis la page contact de GAB : «'+objet+'»  ({})'.format(date_now),

					#content
					text_content,

					#from email
					settings.EMAIL_HOST_USER,

					#rec
					['ex.developpeur.web@gmail.com', 'alguemel7@gmail.com']
				)
				email.attach_alternative(html_content, "text/html")
				email.send()

				messages.success(request, "Message envoyé avec succès, nous vous contacterons sous peu !")
				return redirect('contact')
			else:
				messages.error(request, "Une erreur s'est produite. Veuillez réessayer ...")
				return redirect('contact')

	form = ContactForm()



	template = 'services/contact.html'
	context = {}
	return render(request, template, context)