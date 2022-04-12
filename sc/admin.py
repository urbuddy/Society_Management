from django.contrib import admin
from .models import User, Notice, Complaint

admin.site.register(User)
# Register your models here.
admin.site.register(Notice)
admin.site.register(Complaint)
