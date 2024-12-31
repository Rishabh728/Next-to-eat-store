from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from BaseApp.views import *
from . import views




urlpatterns = [

    path('',homeView, name="home"),
    path('about/',aboutView, name='about'),
    path('menu/',menuView,name='menu'),
    path('bookTable/',bookTableView,name='bookTable'),
    path('feedback/', feedbackView, name='feedback'),
    path('submit-feedback/', feedback_view, name='submit_feedback'),
    

    # cart
    # path('category/<int:category_id>/', views.category_items, name='category_items'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', views.cart_detail, name='cart_detail'),
    # path('cart/update/<int:cart_item_id>/<str:action>/', views.update_cart_item_quantity, name='update_cart_item_quantity'),

    # shiping and cart
    path('cart/', views.cart_and_shipping, name='cart_and_shipping'),
    

    # payment
    path('payment/', views.create_payment, name='payment'),
    path('create-payment-intent/', views.create_payment, name='create_payment_intent'),  # To create the payment intent

    # search
    path('search/',search_view, name = 'search_results'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),

 
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)