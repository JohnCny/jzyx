
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *


def create_myfilter(request):
    form = myfilterForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = myfilterForm()

    t = get_template('webapp/create_myfilter.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_myfilter(request):
  
    list_items = myfilter.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('webapp/list_myfilter.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_myfilter(request, id):
    myfilter_instance = myfilter.objects.get(id = id)

    t=get_template('webapp/view_myfilter.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_myfilter(request, id):

    myfilter_instance = myfilter.objects.get(id=id)

    form = myfilterForm(request.POST or None, instance = myfilter_instance)

    if form.is_valid():
        form.save()

    t=get_template('webapp/edit_myfilter.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
