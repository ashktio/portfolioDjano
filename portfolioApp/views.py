from django.shortcuts import redirect, render, HttpResponse
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
load_dotenv()
# Create your views here.

def index(request):
    return render(request, 'index.html')

def message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = {
            'name' : name,
            'subject' : subject,
            'email' : email,
            'message': message
        }
        message = '''
        From {}
        Name {}
        New Message : {}
        '''.format(data['email'],data['name'],data['message'] )

        send_mail(data['subject'], message, '', [str(os.getenv('EMAIL_HOST_USER'))])
        return redirect('thanks')
    
    return redirect('index')

def thanks(request):
    return render(request, 'thank_you.html')