from django.contrib import admin
from django.utils.translation import deactivate
from .models import *
admin.site.register(Department)
admin.site.register(Coordinator)
admin.site.register(Supervisor)
admin.site.register(Student)
admin.site.register(Programme)
admin.site.register(SupervisorCharacteristics)
admin.site.register(StudentCharacteristics)
admin.site.register(CoordinatorRateLearning)
admin.site.register(CoordinatorRateSupervisor)
admin.site.register(testForm)