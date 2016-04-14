from django.shortcuts import render, render_to_response
from django.core.mail import mail_admins, send_mail

# Create your views here.
def test(request):
	# send_mail('Subject here', 'Here is the message.', 'a.bubub@i.ua',['to@example.com'], fail_silently=False)
	return render_to_response('index.html')