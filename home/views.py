from django.shortcuts import render_to_response
import os

from . import models


def home(request):
    obj = {
            'experiences': models.Experience.objects.all(),
            'projects' : models.Project.objects.all(),
            'skills' : models.Skill.objects.all(),
            'blogs' : models.Blog.objects.all()
           }
    print(models)
    return render_to_response('index.html', obj)
