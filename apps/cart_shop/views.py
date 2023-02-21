from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from .models import Wishlist, CartItemsNew, SingleProduct, CartUser


class ViewCart(View):
   def get(self, request):

        data = CartItemsNew.objects.all()
        context = {'data': data}
        return render(request, 'cart_shop/cart.html', context)


class ViewCartBuy(View):
   def get(self, request, product_id):
       product = get_object_or_404(SingleProduct, id=product_id)
       cart_user = get_object_or_404(CartUser, user=request.user)
       cart_item = CartItemsNew(cart=cart_user, product=product)
       cart_item.save()

class ViewCartDel(View):
   def get(self, request, item_id):
       cart_item = get_object_or_404(CartItemsNew, id=item_id)
       cart_item.delete()
       return redirect('cart_shop:cart')

class ViewCartAdd(View):
   def get(self, request, product_id):
       product = get_object_or_404(SingleProduct, id=product_id)
       cart_user = get_object_or_404(CartUser, user=request.user)
       cart_item = CartItemsNew(cart=cart_user, product=product)
       cart_item.save()
       return redirect('home:index')



def view_cart_total(request):
   cart_items = Wishlist.objects.filter(cart__user=request.user)
   total_price = sum(item.product.price * item.quantity for item in cart_items)
   context = {'cart_items': cart_items, 'total_price': total_price}
   return render(request, 'cart_shop/wishlist.html', context)


def update_item(request, item_id):
   item = Wishlist.objects.get(id=item_id)
   item.quantity += int(request.GET.get('quantity'))
   item.save()
   return redirect('cart_shop:view_cart_wishlist')



def checkout_cart(request):
   # code to handle checkout process
   return redirect('cart_shop:view_cart_wishlist')



class ViewWishlist(View):
   def get(self, request):
       data = Wishlist.objects.all()
       context = {'data': data}

       return render(request, 'cart_shop/wishlist.html', context)



class ViewWishlistDel(View):
   def get(self, request, item_id):
       cart_item = get_object_or_404(Wishlist, id=item_id)
       cart_item.delete()
       return redirect('cart_shop:wishlist')


class ViewWishlistAdd(View):
   def get(self, request, item_id):
       cart_item = get_object_or_404(CartItemsNew, id=item_id)
       cart_item.add()
       return redirect('cart_shop:wishlist')
