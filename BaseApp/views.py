from django.shortcuts import render, redirect
from BaseApp.models import ItemList, Items, AboutUs, Feedback, BookTable, Offer
from django.http import JsonResponse
# Create your views here.



def homeView(request, ):
    items = Items.objects.all()
    list = ItemList.objects.all()
    offer = Offer.objects.all()
    feedback = Feedback.objects.all()
    return render(request,'home.html', {'items' : items, 'list' : list, 'offer':offer, 'feedback':feedback})

def aboutView(request):
    return render(request,'about.html')

# feedback start
def feedbackView(request):
    feedback = Feedback.objects.all()
    return render(request,'feedback.html', {'feedback':feedback})



def feedback_view(request):
    if request.method == "POST":
        # Get data from the form
        User_name = request.POST.get('name')
        Email = request.POST.get('email')
        Rating = request.POST.get('rating')
        Description = request.POST.get('feedback')
        print(User_name, Email, Description, Rating)  # Debugging: Check the captured values
        # Save the data to the database
        Feedback.objects.create(User_name=User_name, Email=Email, Description=Description, Rating=Rating)


        # Redirect to a success page or send a response
        return redirect('home')  # Redirect to success page (create this URL)
    return render(request, 'feedback.html')  # Render your feedback template

# feedback end
# bookTable start
def bookTableView(request):
    return render(request,'bookTable.html')
# bookTable end


# menu start

def menuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request,'menu.html', {'items' : items, 'list' : list})
    



# custom chatgpt cart

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ItemList, Items, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from BaseApp.models import shipping


# # cart and  shipping




# # View cart details
# @login_required
# def cart_detail(request):
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_items = cart.items.all()
#     total_price = sum(item.get_total_price() for item in cart_items)
#     return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

# # increase decrease cart quantity
# from django.http import JsonResponse

# @login_required
# def update_cart_item_quantity(request, cart_item_id, action):
#     cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    
#     if action == "increase":
#         cart_item.quantity += 1
#     elif action == "decrease" and cart_item.quantity > 1:
#         cart_item.quantity -= 1
    
#     cart_item.save()
#     total_price = sum(item.get_total_price() for item in cart_item.cart.items.all())
    
#     return JsonResponse({
#         "quantity": cart_item.quantity,
#         "item_total_price": cart_item.get_total_price(),
#         "cart_total_price": total_price,
#     })

# # Add an item to the cart
@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_and_shipping')
# custom chatgpt cart

# menu end

# shipping address start



# @login_required
# def shipping_add(request):
#     if request.method == 'POST':
        
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         zip_code = request.POST.get('zip_code')
#         city = request.POST.get('city')
#         state = request.POST.get('state')

#         # Basic validation
        
#         if not all ([first_name,last_name,address,phone,zip_code,city,state]):
#             messages.error(request,'All field required.')
#         else:
#             # save to database
#             shipping.objects.create(
#                 user = request.user,
#                 first_name = first_name,
#                 last_name = last_name,
#                 address_1 = address,
#                 phone = phone,
#                 zipcode = zip_code,
#                 city = city,
#                 state = state,
#             )
#             messages.success(request,'Adress saved sucessfully')
#             return redirect('payment.html')       
#     return render(request,'cart_detail.html')

# @login_required
# def autoName(request, user_id):
#     user = request.user
#     auto_Name = get_object_or_404(shipping,id=user_id)
#     return render(request,'cart_detail.html',autoName=autoName)


# shipping address end


# payment stripe

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Configure Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_payment(request):
    if request.method == "POST":
        try:
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=5000,  # Amount in cents (e.g., $50.00)
                currency='usd',
                automatic_payment_methods={"enabled": True},
            )
            return JsonResponse({'clientSecret': intent['client_secret']})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'payment.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    })


# stripe payment end


# combo shipping and cart start

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Cart, CartItem, shipping

@login_required
def cart_and_shipping(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total_price = sum(item.get_total_price() for item in cart_items)

    if request.method == "POST":
        # Handle shipping form submission
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        zip_code = request.POST.get('zip_code')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')

        if not all([first_name, last_name, address, phone, zip_code, city, state, country]):
            messages.error(request, 'All fields are required.')
        else:
            shipping.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                address_1=address,
                phone=phone,
                zipcode=zip_code,
                city=city,
                state=state,
                country=country,
            )
            messages.success(request, 'Address saved successfully.')
            return redirect('payment')  # Replace 'payment' with your payment page URL name

    elif request.method == "GET" and 'cart_item_id' in request.GET:
        # Handle cart item updates
        cart_item_id = request.GET.get('cart_item_id')
        action = request.GET.get('action')
        cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)

        if action == "increase":
            cart_item.quantity += 1
        elif action == "decrease" and cart_item.quantity > 1:
            cart_item.quantity -= 1

        cart_item.save()
        total_price = sum(item.get_total_price() for item in cart_item.cart.items.all())

        return JsonResponse({
            "quantity": cart_item.quantity,
            "item_total_price": cart_item.get_total_price(),
            "cart_total_price": total_price,
        })

    return render(request, 'cart_and_shipping.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


# combo shipping and cart end


# Search

from django.shortcuts import render
from fuzzywuzzy import process
from .models import Items  # Replace with your model

def search_view(request):
    query = request.GET.get('q', '').strip()  # Get the search term
    results = []
    suggestions = []

    if query:
        # Perform the main search (exact match)
        results = Items.objects.filter(Item_name__icontains=query)

        # If no results, use fuzzy matching for suggestions
        if not results:
            # Fetch all item names to compare
            all_items = Items.objects.values_list('Item_name', flat=True)
            suggestions = process.extract(query, all_items, limit=5)  # Top 5 fuzzy matches

            # Convert suggestion tuples (name, score) into a list of Item objects
            suggestions = [Items.objects.filter(Item_name=s[0]).first() for s in suggestions if s[1] > 50]  # Use a score threshold to filter out low matches

    return render(request, 'item_detail.html', {
        'results': results,
        'suggestions': suggestions,
        'query': query,
    })

def item_detail(request, id):
    item = get_object_or_404(Items, pk=id)
    return render(request, 'item_detail.html', {'item': item})



    