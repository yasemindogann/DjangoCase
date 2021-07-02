import secrets
from django.contrib import messages
from django.shortcuts import render
from django.utils import translation
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . forms import ContactForm
from django.urls import reverse_lazy
from django.http import request

from .models import Contact


class IndexView(TemplateView):
    template_name = 'index.html'


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=True)
            code = secrets.token_urlsafe(32)
            p.code = code
            p.save()
            messages.success(request,'Başarılı bir şekilde gönderildi. Sizin için oluşturulan kod : '+code)
    form = ContactForm()
    return render(request, 'contact.html', {'form':form})



def formSorgulaView(request):
    form = None
    if request.method =='POST':
        kod = request.POST.get('code')
        if Contact.objects.filter(code=kod):
            form = Contact.objects.filter(code=kod).first()
            messages.success(request, 'Kayıt Bulundu')
        else:
            messages.warning(request, 'Girilen kod sistemde bulunamadı')
    return render(request, 'form-sorgula.html', {'form': form})



# def selectlanguage(request):
#     if request.method == 'POST':
#         cur_language = translation.get_language()
#         lasturl = request.META.get('HTTP_REFERER')
#         lang = request.POST['language']
#         translation.active(lang)
#         request.session[translation.LANGUAGE_SESSION_KEY]=lang
#         return HttpResponsiveRedirect("/"+lang+lasturl)

    