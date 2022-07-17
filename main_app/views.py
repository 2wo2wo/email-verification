from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail as send_mail_from_user
# Create your views here.

from django.contrib.auth import get_user_model
from .forms import UserForm
from django_email_verification import send_email


def send_mailing(request):
    if request.method == 'GET':
        form = ContactForm()

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['messsage']
            recipient_list = ['zulfiqbobur@gmail.com']
            try:
                send_mail_from_user(subject, message, from_email, recipient_list, fail_silently=False)
                print('success')
            except Exception:
                print('fail')
                return HttpResponse('Smth went wrong?')
        return HttpResponse('form is not valid')
    return render(request, 'main_app/index.html', {'form':form})




def registration(request):
    if request.method == 'GET':
        form = UserForm()
        print('get method usedz')
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password1 = form.cleaned_data['password1']
            if password1 == password:

                user = get_user_model().objects.create(username=username, password=password, email=email)
                user.is_active = False
                send_email(user)
                print('mail sended')
                return render(request, 'main_app/email_send.html')
            else:
                return render(request, 'main_app/registration.html', {
                    'form': form,
                    'message': 'passwords do not match'
                })

    return render(request,  'main_app/registration.html', {
        'form': form
    })


#
#
#
