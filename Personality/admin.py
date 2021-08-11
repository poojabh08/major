from django.contrib import admin

# Register your models here.
from .models import clusterNum, user_answers, registration_details

admin.site.register(clusterNum)
admin.site.register(registration_details)
admin.site.register(user_answers)
