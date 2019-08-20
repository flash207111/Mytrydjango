from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.product_detail_view ),
    path('create/', views.product_create_view ),
    path('update/', views.product_update_view ),
    path('initial/', views.render_initial_data ),
    path('<int:my_id>/', views.dynamic_lookup_view, name='lookup'),
    path('<int:my_id>/delete/', views.product_delete_view, name='delete'),
    path('list/', views.product_list_view, name='list'),
]
