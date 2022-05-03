from django.contrib import admin
from users.models import UserInfo, VerifyCode


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(VerifyCode)
class UserInfoAdmin(admin.ModelAdmin):
    pass


admin.site.site_title = 'LL装机平台'
admin.site.site_header = 'LL装机平台'
admin.site.index_title = 'LL装机平台'
