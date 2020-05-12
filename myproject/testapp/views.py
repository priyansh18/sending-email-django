from django.shortcuts import render
from django.conf import settings
from . import forms
from django.core.mail import send_mail
# Create your views here.


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to sendEmailUsingDjango'
        message = 'Hope you are enjoying this'
        email_from = settings.EMAIL_HOST_USER
        recepient = str(sub['email'].value())
        send_mail(subject,
                  message, email_from, [recepient], fail_silently=False)
        return render(request, 'testapp/sucess.html', {'recepient': recepient})
    return render(request, 'testapp/index.html', {'form': sub})
