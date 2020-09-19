from django.shortcuts import render
from django.views import generic
from .models import NewsLetter, Contact
from .forms import NewsLetterForm, ContactForm

class NewsletterView(generic.TemplateView):

    template_name = 'views/newsletter/newsletter.html'
    final_template_name = 'views/newsletter/post_newsletter.html'

    def get(self, request):

        form = NewsLetterForm()
        post = form.save(commit = False)

        args = { 'form' : form }

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if not database_name.objects.filter(email = database_object.email).exists():
            return True

        return False

    def post(self, request):

        form = NewsLetterForm(request.POST)

        if form.is_valid():

            post = form.save(commit = False)

            if self._validate_save(NewsLetter, post):
                form.save()

        return render(request, self.final_template_name)

class FormularContact(generic.TemplateView):

    template_name = 'views/formular/contact.html'
    final_template_name = 'views/formular/post_contact.html'

    def get(self, request):

        form = ContactForm()
        post = form.save(commit = False)

        args = { 'form' : form }

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if not database_name.objects.filter(title = database_object.title, message = database_object.message).exists():
            return True

        return False

    def post(self, request):

        form = ContactForm(request.POST)

        if form.is_valid():

            post = form.save(commit = False)

            if self._validate_save(Contact, post):
                form.save()

        return render(request, self.final_template_name)
