from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Cart, CartItem, Product
from django.views import View


class CartView(View):
   def get(self, request):
      data = Product.objects.all()
      context = {'data': data}

      return render(request, 'cart/cart.html', context)


def view_cart(request):
   cart_items = CartItem.objects.filter(cart__user=request.user)
   total_price = sum(item.product.price * item.quantity for item in cart_items)
   context = {'cart_items': cart_items, 'total_price': total_price}
   return render(request, 'cart.html', context)


def update_item(request, item_id):
   item = CartItem.objects.get(id=item_id)
   item.quantity += int(request.GET.get('quantity'))
   item.save()
   return redirect('cart:view_cart')


def remove_item(request, item_id):
   CartItem.objects.filter(id=item_id).delete()
   return redirect('cart:view_cart')


def checkout(request):
   # code to handle checkout process
   return redirect('cart:view_cart')


