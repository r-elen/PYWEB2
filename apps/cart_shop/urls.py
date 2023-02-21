from django.urls import path
from .views import ViewCart, ViewWishlist, ViewCartBuy, ViewCartDel, ViewWishlistDel, ViewCartAdd, ViewWishlistAdd

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('add/<int:item_id>', ViewCartAdd.as_view(), name='add_to_cart'),
   path('buy/<int:item_id>', ViewCartBuy.as_view(), name='buy'),
   path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),

   path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
   path('wishlist/del/<int:item_id>/', ViewWishlistDel.as_view(), name='del_from_wishlist'),
   path('wishlist/add/<int:item_id>/', ViewWishlistAdd.as_view(), name='add_to_wishlist'),

]
