from django.shortcuts import redirect, render, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import contactForm

# Create your views here.

def index(request):
    if request.method == 'GET':
        form = contactForm()

    else:
        form = contactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            subject = form.cleaned_data.get('subject')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
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
            
            try:
                send_mail(data['subject'], message, 'ashenafi.teressa@gmail.com', ['ashenafi.teressa@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('/')
    return render(request, 'index.html', {'form' : form})