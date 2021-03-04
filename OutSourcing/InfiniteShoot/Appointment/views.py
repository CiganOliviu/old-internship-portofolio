from django.shortcuts import render

def appointment(request):

    template_name = 'appointment/appointment.html'

    return render(request, template_name)