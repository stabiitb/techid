from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def send_email(template,subject,from_email,to_email,data):
	plaintext = get_template(template)
	d = Context(data)
	text_content = plaintext.render(d)
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	msg.send()