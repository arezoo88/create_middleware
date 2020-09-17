from django.contrib import admin
from .models import Person


@admin.register((Person))
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'is_adult')

    def is_adult(self, obj):
        if obj.age > 18:
            return True
        else:
            return False

    is_adult.boolean = True
