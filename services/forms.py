from django.forms import *
from .models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = [
			'nom',
			'email',
			'tel',
			'objet',
			'texte'
		]