from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from .forms import ContactForm


def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        comment = form.cleaned_data['Comment']
        name = form.cleaned_data['Name']
        subject = 'Message From Somewhere'
        message = '%s %s' % (comment, name)
        email_from = form.cleaned_data['Email']
        email_to = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [email_to], fail_silently=True)
        form = None
        title = 'Thanks'
        confirm_message = ' Thanks for the message'
    context = {'title': title, 'form': form, 'confirm_message': confirm_message}

    template = 'contact.html'
    return render(request, template, context)