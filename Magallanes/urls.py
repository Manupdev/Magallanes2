
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE, name="base"),
    path('',views.HOME, name="home"),
    path('products/', views.PRODUCT, name="products"), #falta paginacion y talles(en el models, y el orden en productos)
    path('products/<str:id>', views.PRODUCT_DETAIL_PAGE, name="product_detail"),
    path('search/', views.SEARCH, name="search"),
    path('contact/', views.Contact_page, name="contact"),
    path('register/', views.HandleRegister, name="register"),
    path('login/', views.HandleLogin, name="login"),
    path('logout/', views.HandleLogout, name="logout"),
    


    #cart
    path('cart/add/<int:id>/', views.cart_add,name="cart_add"),
    path('cart/item_clear/<int:id>/', views.item_clear,name="item_clear"),
    path('cart/item_increment/<int:id>/',
            views.item_increment, name="item_increment"),
    path('cart/item_decrement/<int:id>/', views.item_decrement,name="item_decrement"),
    path('cart/cart_clear/', views.cart_clear,name= "cart_clear"),
    path('cart/cart-detail/', views.cart_detail,name="cart_detail"),
    path('cart/checkout', views.Check_out, name="checkout"), 
    path('cart/checkout/placeorder', views.PLACE_ORDER,name="place_order"),
    path('cart/mptest', views.mptest, name="mptest")


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
