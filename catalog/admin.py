from django.contrib import admin

# Register your models here.
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    def body_short(self, obj: Car):
        # return '{obj.body}'.format(obj.body)
        out_str = obj.description[:15] + '...'
        # return ''.join(obj.description[:15])
        return out_str

    list_display = ['id', 'title', 'tipe', 'body_short']
