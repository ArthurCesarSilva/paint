from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Color

def index(request): 
        return HttpResponse('')

def curtidas(request, ):
    the_entire_list = Color.objects.all()
    template = loader.get_template('paint-templates/index.html')
    context = {
        'the_entire_list':the_entire_list
    }
    return HttpResponse(template.render(context ,request))

def colorpage (request,color_name):
      name_your_color = Color.objects.get(color_name = color_name)
      template = loader.get_template('paint-templates/colorpage.html')
      context = {
        'X':name_your_color
        }
      return HttpResponse(template.render(context , request))

    