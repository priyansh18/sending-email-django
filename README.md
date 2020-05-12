# sending-email-django# EmailSendingDjango

Sending emails is one of the important parts of the website in fact almost all websites needs this part if they are going to have users login to their site for things such as account activation through the user email, password reset and other activities. If you are building a website with django framework this tutorial will show you how to send emails to your users.
To send emails from your website you need to have the email host server and in this case we are going to use google SMTP server. In order for this to work you need to have a working gmail account and in your account you need to enable allow less secure app feature under account security settings. Login to your google account through your browser and enable ;ess secured app . This feature is specifically for securing your google account from the apps that are less secure to use it in order to prevent hackers from hacking into your account through these apps.
configuring django for Gmail SMTP server.
under your settings.py file you need to add the following settings.

EMAIL_BACKEND = ‘django.core.mail.backends.smtp.EmailBackend’
EMAIL_HOST = ‘smtp.gmail.com’
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ‘your_account@gmail.com’
EMAIL_HOST_PASSWORD = ‘your account’s password’

the settings above are used by django to make sending emails through your email host server possible. EMAIL_BACKEND specifies the django backend that will work with the host email server specified at EMAIL_HOST part to send emails to our user, as you may have noticed the value of EMAIL_HOST is the link to the google’s smtp server as specified by google, you can find more knowledge on that here. EMAIL_USE_TLS tells django what secure protocol should be used to connect to the server, you can use TLS as we have used here or you could use SSL by replacing that part with EMAIL_USE_SSL and set them to true. Note that you can not use both of them at once. If you use TLS the EMAIL_PORT value is 587 but if you use SSL the port value will have to be 465. The following two parts are self explanatory, put your working gmail account with allow less secure app feature enabled and put your password on the host password variable, note that the password is visible here and someone can just see it and use it so it will have to be encrypted when you want to host your website. That will be all for preparing django for sending emails to the users email account.
defining a view function
this part will depend on your purpose of wanting to send emails to the user, for simplicity of this tutorial i will assume you want to thank them for registering to your website and it means a world to you. I will write onether tutorial on how to activate the user accounts on your site by using email verification. To send emails you have to import the following into your views.py file

from django.core.mail import send_mail
from django.conf import settings

send_mail is the function that will send emails to our users, it uses our new added settings in the settings.py file. It takes in several parameters but for simplicity i will use the minimum parameters that will enable us to send an email that makes sense for purposes such as sending account verification link or password verification link. In your view file your functions will look like this

def email(request):
subject = 'Thank you for registering to our site'
message = ' it means a world to us '
email_from = settings.EMAIL_HOST_USER
recipient_list = ['receiver@gmail.com',]
send_mail( subject, message, email_from, recipient_list )
return redirect('redirect to a new page')

That is the simplest function one can write to send emails in the django world, if you are doing something complex you probably will have extra stuff there like taking the users email from the form, or if it is for account activation you will probably have some functions to generate an encrypted key that will be sent to the user’s email and when they click it their accounts will be activated and stuff like that but for simplicity i decided to put it like that. The email function is what is going to be called from the url file when the action to send email is triggered. The send_mail function takes much more parameters than the ones i have used above, you can learn more about this at django documentation on this link .

subject: an email subject string
message: a string of the actual message yo want to send
email_from: your email and that is the reason i had to import the settings file into views file but you don’t have to do it like this, you can write your email there as a string and it will work but that will help to avoid errors due to mistakes like having a typo on your email.
recipient_list: A list of strings, each an email address.
