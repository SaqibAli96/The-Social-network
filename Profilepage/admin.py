from django.contrib import admin
from Profilepage.models import Post,Profile,Following,Like,Public
# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Public)
admin.site.register(Following)
admin.site.register(Like)
