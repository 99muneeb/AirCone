# New file
from django.shortcuts import render, redirect
from .models import Service, Team, Contect
from django.contrib import messages

from .forms import ContactForm, AppointmentForm
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def Home(request):
    services = Service.objects.all()
    data = {
        'services': services
    }
    return render(request, 'pages/home.html', data)


def About_us(request):
    return render(request, 'pages/about.html')


def Services(request):
    services = Service.objects.all()
    data = {
        'services': services
    }
    return render(request, 'pages/services.html', data)


def Single_Service(request):
    # services=Service.objects.all()
    # data={
    #     'services':services
    # }
    return render(request, 'pages/single_service.html')


def Teams(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/team.html', data)


def Appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            body = f"name: {form.cleaned_data['name']}\nemail: {form.cleaned_data['email']}\naddress: {form.cleaned_data['address']}\ndate: {form.cleaned_data['email']}\ntime: {form.cleaned_data['time']}\nmessage: {form.cleaned_data['message']}"
            form.save()

            try:
                msg = EmailMessage('Website Inquiry Appointment Details',
                                   body, to=['muneeb9166@gmail.com', 'f19040015@orbit.edu.pk'])
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            # Success message
            messages.add_message(request, messages.SUCCESS, 'Contact details sent successfully!')
            return render(request, 'pages/success_message.html')

    form = AppointmentForm()
    return render(request, 'pages/appointment.html', {'form': form})


def Contect_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = f"name: {form.cleaned_data['name']}\nemail: {form.cleaned_data['email']}\nmessage: {form.cleaned_data['message']}"
            form.save()

            try:
                msg = EmailMessage('Website Inquiry Contect Details',
                                   body, to=['muneeb9166@gmail.com', 'f19040015@orbit.edu.pk'])
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            # Success message
            messages.add_message(request, messages.SUCCESS, 'Contact details sent successfully!')
            return render(request, 'pages/success_message.html')

    form = ContactForm()
    return render(request, 'pages/contect.html', {'form': form})
