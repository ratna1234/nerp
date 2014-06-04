from django.contrib import admin
from training.models import Participant, Training, Category, File, Organization, ResourcePerson, TargetGroup

admin.site.register(Participant)
admin.site.register(Training)
admin.site.register(Category)
admin.site.register(File)
admin.site.register(Organization)
admin.site.register(ResourcePerson)
admin.site.register(TargetGroup)
