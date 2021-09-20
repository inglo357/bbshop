from django.urls import include, path
from product import views

urlpatterns = [
    path('categories/', views.CategoriesList.as_view()),
    path('products/search/', views.search),
    path('latest-products/', views.LatestProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]