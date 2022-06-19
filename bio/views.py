from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
# Create your views here.


def index1(request):
    return render(request, 'index.html')


def probase(request):
    return render(request, 'probase.html')


def bioDcornea(request):
    return render(request, 'bioDcornea.html')


def bioDvaginal(request):
    return render(request, 'bioDvaginal.html')


def bioDskin(request):
    return render(request, 'bioDskin.html')


def about(request):
    return render(request, 'about.html')


def join(request):
    return render(request, 'join.html')


def contact(request):
    return render(request, 'contact.html')


def send1(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        message1 = request.POST.get('message')
        print(name1, email1, message1)
        send_mail(
            name1,
            "Name : " + name1 + "\n Email Address  " +
            email1 + " \n Message typed " + message1,
            email1,
            ['harijkk@gmail.com'],
            fail_silently=False,
        )

        return HttpResponseRedirect('contact')
    else:
        return HttpResponse("INVALID REQUEST")


def send_attach(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        email_req = EmailMessage(
            name1,
            "Name : " + name1 + "\n Email Address  " + email1,
            email1,
            ['harijkk@gmail.com']

        )
        file = request.FILES['upload']
        email_req.attach(file.name, file.read(), file.content_type)
        email_req.send()
        return HttpResponseRedirect('join')
    else:
        return HttpResponse("INVALID REQUEST")
