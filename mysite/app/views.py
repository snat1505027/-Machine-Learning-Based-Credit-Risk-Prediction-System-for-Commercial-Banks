from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User



def index(request):
    context = {}
    if(request.user.username!=""):
        template = loader.get_template('app/form_wizards.html')
    else:
        template = loader.get_template('app/page_403.html') #access denied
    return HttpResponse(template.render(context, request))


def loan_app_success(request):
    print('loan_app_success entered')

    context = {}
    if(request.user.username!=""):
        template = loader.get_template('app/loan_app_success.html')
    else:
        template = loader.get_template('app/page_403.html') #access denied
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    '''
    if(request.user.username!=""):
        load_template = request.path.split('/')[-1]
        template = loader.get_template('app/' + load_template)
    else:
        template = loader.get_template('app/page_403.html')
    return HttpResponse(template.render(context, request))
    '''
    template = loader.get_template('app/page_404.html')
    return HttpResponse(template.render(context, request))

