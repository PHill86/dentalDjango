from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        # grab stuff from the form
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # email from
            ['pathill86@gmail.com'], # email to
            fail_silently=False, # True for production
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else: 
        # return the page
        return render(request, 'contact.html', {})