from django.db import models

from django.db import models
import datetime


def year_choices():
    return [(r, r) for r in range(1992, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start = models.IntegerField(default=2013)
    end = models.IntegerField(default=2018)
    image_url = models.URLField(max_length=1000)
    work_detail = models.TextField(max_length=4000)

    def __str__(self):
        if self.company == None:
            return "ERROR company NAME IS NULL"
        return self.company


class Project(models.Model):
    name = models.CharField(max_length=1000)
    project_detail = models.TextField(max_length=4000)

    def __str__(self):
        if self.name == None:
            return "ERROR NAME IS NULL"
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=100)

    def __str__(self):
        if self.name == None:
            return "ERROR NAME IS NULL"
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    blog_detail = models.TextField(max_length=400)
    link = models.URLField(max_length=100)

    def __str__(self):
        if self.name == None:
            return "ERROR NAME IS NULL"
        return self.name