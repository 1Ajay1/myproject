from django.contrib import admin
from django.contrib.admin.sites import site
# Register your models here.

from contact.models import sign_up,join_us,contact,python,questionAnswer,javaScript,pythonCoding,javaCoding

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(sign_up, AuthorAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(join_us, AuthorAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(contact, AuthorAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(python, AuthorAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(javaScript, AuthorAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(questionAnswer, AuthorAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(pythonCoding, AuthorAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(javaCoding, AuthorAdmin)