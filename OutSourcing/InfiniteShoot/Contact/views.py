from django.shortcuts import render
from django.views import generic

from Contact.form import NewsletterForm, ContactForm
from Contact.models import Newsletter, Contact


class ContactView(generic.TemplateView):
    template_name = 'contact/contact_view.html'
    final_template_name = 'contact/post_contact.html'

    def get(self, request):
        form = ContactForm()
        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name, args)

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            if self._validate_save(Contact, post):
                form.save()

        return render(request, self.final_template_name)

    def _validate_save(self, database_name, database_object):

        if not database_name.objects.filter(title=database_object.title, message=database_object.message).exists():
            return True

        return False


class NewsletterView(generic.TemplateView):
    template_name = 'newsletter/newsletter_view.html'
    final_template_name = 'newsletter/post_newsletter.html'

    def get(self, request):
        form = NewsletterForm()
        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name,  args)

    def post(self, request):

        form = NewsletterForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            if self._validate_save(Newsletter, post):
                form.save()

        return render(request, self.final_template_name)

    def _validate_save(self, database_name, database_object):

        if not database_name.objects.filter(email=database_object.email).exists():
            return True

        return False
