from django.contrib import admin
from BaseApp.models import *

# Register your models here.

admin.site.register(ItemList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(Feedback)
admin.site.register(BookTable)
admin.site.register(Offer)

# chatgpt
admin.site.register(Cart)
admin.site.register(CartItem)

# shipping 
admin.site.register(shipping)