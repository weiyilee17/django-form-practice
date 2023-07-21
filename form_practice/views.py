from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

from .forms import ApplicationForm
from .models import Applicant


# Create your views here.
def index(request):
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST)

        if application_form.is_valid():
            first_name = application_form.cleaned_data['first_name']
            last_name = application_form.cleaned_data['last_name']
            email = application_form.cleaned_data['email']
            date = application_form.cleaned_data['date']
            occupation = application_form.cleaned_data['occupation']

            Applicant.objects.create(first_name=first_name, last_name=last_name, email=email, date=date,
                                     occupation=occupation)

            email_body = f'Thank you for your submission, {first_name}. Here are your data: \n' \
                         f'{first_name}\n' \
                         f'{last_name}\n' \
                         f'{date}\n' \
                         f'{occupation}\n' \
                         'Thank you!'

            email_message = EmailMessage('New Form Submission', email_body, to=[email])
            email_message.send()

            messages.success(request, 'Form submitted successfully!')
            return redirect('index')
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
