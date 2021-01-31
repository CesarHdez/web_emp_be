from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviar Correo y direccionar
            #EmailMessage(asunto, cuerpo, e_mail origen, email destino replyto=[])
            email = EmailMessage(
                "La Caffettiera: Mensaje de Contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["cesar.hernandez.19@alumnos.uda.cl"],
                reply_to=[email]
            )
            try:
                email.send()
                #todo bien redirección a ok
                return redirect(reverse('contact')+"?ok")
            except:
                #Hubo algunproblema
                return redirect(reverse('contact')+"?fail")
            
    
    return render(request, "contact/contact.html",{'form':contact_form})
