from django.contrib import admin
from django.forms import models
from collagepaper.models import Collage, Paper, Branch

# for configuration of Ctegory admin


class CollageAdmin(admin.ModelAdmin):
    list_display = ('collage_name', 'add_date')
    search_fields = ('collage_name',)


# for configuration of Post admin


class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'add_date')
    search_fields = ('branch_name',)


class PaperAdmin(admin.ModelAdmin):
    list_display = ('paper_subject', 'paper_semester', 'paper_year')
    search_field = ('branch', 'year')


# Register your models here.
admin.site.register(Collage, CollageAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Paper, PaperAdmin)
