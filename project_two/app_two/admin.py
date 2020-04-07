from django.contrib import admin
from app_two.models import Documents, Headings, Images, States, SubHeadings, Texts, Relations

# Register your models here.
admin.site.register(Documents)
admin.site.register(Headings)
admin.site.register(Images)
admin.site.register(States)
admin.site.register(SubHeadings)
admin.site.register(Texts)
admin.site.register(Relations)
