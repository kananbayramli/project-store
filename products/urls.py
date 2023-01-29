from django.urls import path

from .views import ProductsListView, basket_add, basket_remove

# from django.views.decorators.cache import cache_page ##cache_page(30)


app_name = 'products'

urlpatterns = [
    path('', (ProductsListView.as_view()), name='index'),
    path('category/<int:category_id>', ProductsListView.as_view(), name='category'),
    path('page/<int:page>', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]