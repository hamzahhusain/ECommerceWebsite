from django.urls import path
from shop import views as shop_views
 
urlpatterns = [
    path('',shop_views.home, name='shop-home'),
    path('test/',shop_views.test, name='test'),
    path('login/',shop_views.home,name='login'),
    path('logout/',shop_views.logout, name='logout')
]
