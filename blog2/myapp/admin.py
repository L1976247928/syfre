from django.contrib import admin
from .models import Post,User,Author,Remark,category
# Register your models here.


admin.site.register(Remark)
admin.site.register(category)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Author)












