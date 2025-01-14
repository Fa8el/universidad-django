from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar(request):  # Indentación corregida aquí
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["fa82el@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)  # Cambiado 'false' a 'False'
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")
