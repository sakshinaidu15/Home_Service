from django.contrib import admin
from .models import UserModel,Orders,ServiceMan,Services
# Register your models here.
admin.site.register(UserModel)
admin.site.register(Orders)
admin.site.register(ServiceMan)
admin.site.register(Services)