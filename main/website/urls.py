from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('new_order/', views.new_order, name='new_order'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/mark_delivered/', views.mark_order_delivered, name='mark_order_delivered'),
    path('order/<int:order_id>/mark_out/', views.mark_order_out, name='mark_order_out'),
    path('order/<int:order_id>/update_status/<str:new_status>/', views.update_order_status, name='update_order_status'),
    path('order/edit/<int:order_id>/', views.edit_order, name='edit_order'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
