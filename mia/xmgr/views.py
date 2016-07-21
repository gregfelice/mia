

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Person

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'people'

    def get_queryset(self):
        return Person.objects.all()


class DetailView(generic.DetailView):
    model = Person
    template_name = 'detail.html'

