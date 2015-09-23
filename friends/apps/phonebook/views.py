from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, View
from friends.apps.phonebook.models import Contact
from friends.apps.phonebook.forms import ContactForm
# Create your views here.


class ContactList(ListView):
    model = Contact
    paginate_by = 20
    template_name = 'contact_list.html'


class ContactDelete(View):
    form = ContactForm

    def get(self, request, contact_id):
        contacto = Contact.objects.get(id=contact_id)
        contacto.delete()
        return HttpResponseRedirect(reverse('phonebook:list'))


class ContactNew(View):
    template_name = "contact_new.html"
    form = ContactForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form()})

    def post(self, request):
        my_form = self.form(request.POST)
        if my_form.is_valid():
            my_form.save()
            return HttpResponseRedirect(reverse('phonebook:list'))
        else:
            return render(request, self.template_name, {'form': my_form})


class ContactEdit(View):
    template_name = "contact_new.html"
    form = ContactForm

    def get(self, request, contact_id):
        contacto = Contact.objects.get(id=contact_id)
        return render(request, self.template_name, {'form': self.form(instance=contacto)})

    def post(self, request, contact_id):
        contacto = Contact.objects.get(id=contact_id)
        my_form = self.form(request.POST, instance=contacto)
        if my_form.is_valid():
            my_form.save()
            return HttpResponseRedirect(reverse('phonebook:list'))
        else:
            return render(request, self.template_name, {'form': my_form})