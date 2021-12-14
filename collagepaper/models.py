from pyexpat import model
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Collage(models.Model):
    collage_id = models.AutoField(primary_key=True)
    collage_name = models.CharField(max_length=255)
    collage_code = models.CharField(max_length=25)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.collage_name


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=255)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.branch_name


class Paper(models.Model):
    paper_subject = models.CharField(max_length=100)
    collage = models.ManyToManyField(Collage)
    branch = models.ManyToManyField(Branch)
    paper_code = models.AutoField(primary_key=True)
    paper_year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1900), max_value_current_year])
    paper_semester = models.IntegerField(null=False)
    pdf_paper = models.FileField(upload_to='collagepaper/')
