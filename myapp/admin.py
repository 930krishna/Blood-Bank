from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Bloodbank)
admin.site.register(Donor)
admin.site.register(Receiver)
admin.site.register(Complaint)
