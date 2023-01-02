from django.contrib import admin
from .models import post,comment,categorys,Profile

admin.site.register(post)
admin.site.register(comment)
admin.site.register(categorys)
admin.site.register(Profile)
