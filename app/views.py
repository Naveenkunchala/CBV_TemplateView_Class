from typing import Any, Dict
from django.shortcuts import render

from django.http import HttpResponse
from app.forms import *

from django.views.generic import TemplateView

# Create your views here.

# class cbv_html(TemplateView):
#     template_name='cbv_html.html'


class cbv_context(TemplateView):
    template_name='cbv_context.html'
    def get_context_data(self, **kwargs):
        EDCO=super().get_context_data(**kwargs)
        EDCO['name']='Naveencharan'
        EDCO['age']=21
        return EDCO
    
   
class cbv_data(TemplateView):
    template_name='cbv_data.html'
    def get_context_data(self, **kwargs):
        EDCO=super().get_context_data(**kwargs)
        
        TFO=TopicForm()
        EDCO['TFO']=TFO
        return EDCO
        
    def post(self,request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('inserted data')
        