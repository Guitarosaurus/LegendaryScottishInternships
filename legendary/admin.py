from django.contrib import admin
from legendary.models import Internship, Comment, Company, UserProfile

# Register your models here.
admin.site.register(Internship)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(UserProfile)