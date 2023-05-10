from django.contrib import admin
from .models import Product,Cart,Cart_product,Orders
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import User,profile,Orders,student
admin.site.register(profile)
admin.site.register(student)

admin.site.register(User,UserAdmin)
UserAdmin.fieldsets+=('customer field set',{'fields':('phone',)}),

# class cartinline(admin.TabularInline):
#     model = Cart
# class productinline(admin.TabularInline):
#      model = Product
'''class useradmin(UserAdmin):
    model=User
    list_display = ('username','get_cart','is_staff','is_active')
    list_filter = ('username','is_staff','is_active')
    fieldsets = (
        ('userdetail',{'fields':('username','password')}),
        ('permissions',{'fields':('is_staff','is_superuser','is_active')}),
        ('important dates',{'fields':('last_login','date_joined')}),
        ('advanced options',{
            'classes':('collapse',),
            'fields':('user_permissions','groups')
        }),
    )
    add_fieldsets = (
        (None,{'classes':('wide',),
               'fields':('username','password1','password2','is_staff','is_superuser','is_active','groups'),
               }
         ),
    )
    # inlines = ('cartinline',)
    def get_cart(self,obj):
        return obj.cart
    search_fields = ('username',)

class cartadmin(admin.ModelAdmin):
    model=Cart
    list_display = ('user','created_on','staff')
    fieldsets = (
        (None,{'fields':('user','created_on')}),

    )
    # inlines = (
    #     'productinline',
    # )



    def staff(self,obj):
        return obj.user.is_staff

'''
# admin.site.unregister(User)
# admin.site.register(User,useradmin)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cart_product)
admin.site.register(Orders)
