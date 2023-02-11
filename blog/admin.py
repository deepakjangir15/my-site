from django.contrib import admin
from .models import Post,Author,Tag, Comment, Certificate
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author','tags','date',)
    list_display = ('title','date','author',)
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name','post')

class CertificateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('certificate_credential_id'.lower(),)}


admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Certificate,CertificateAdmin)