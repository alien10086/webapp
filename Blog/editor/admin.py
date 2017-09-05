# -*- coding: utf-8 -*-

from django.contrib import admin


from .models import  Author, Entry

#用普通方法需要分开注册







admin.site.register(Author)
admin.site.register(Entry)
