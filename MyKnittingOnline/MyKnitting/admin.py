from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Yarn)
admin.site.register(Needles)

admin.site.register(YarnsForProject)
admin.site.register(NeedlesForProject)

admin.site.register(Photo)
admin.site.register(Pattern)