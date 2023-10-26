from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .forms import ContactForm
from constants import EMAIL

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],
                f"Nombre: {form.cleaned_data['first_name']}\n"
                f"Apellido: {form.cleaned_data['last_name']}\n"
                f"Correo electrónico: {form.cleaned_data['email_address']}\n"
                f"Mensaje: {form.cleaned_data['message']}",
                form.cleaned_data['email_address'],
                [EMAIL],
                fail_silently=False,
            )
            return redirect('portfolio')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})