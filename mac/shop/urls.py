from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="aboutUs"),
    path('contact/',views.contact,name="contactUs"),
    path('tracker/',views.tracker,name="TrackingStatus"),
    path('search/',views.search,name="search"),
    path('product/<int:id>',views.productview,name="ProductView"),
    path('checkout/',views.checkout,name="CheckOut"),
]
