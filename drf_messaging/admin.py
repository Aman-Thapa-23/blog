from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Messages)
admin.site.register(Attachment)
admin.site.register(UserTechInfo)
admin.site.register(BlackList)
admin.site.register(ReportedMessages)
