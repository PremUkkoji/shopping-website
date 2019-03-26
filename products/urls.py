from django.urls import path
from . import views
from .views import (
	ProductListView,
# 	PostDetailView,
# 	PostCreateView,
# 	PostUpdateView,
# 	PostDeleteView,
	UserPurchasedProductListView,
    UserCartProductListView
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('', ProductListView.as_view(), name='products-home'),
	path('cart/', UserCartProductListView.as_view(), name='cart-products'),
	path('purchased/', UserPurchasedProductListView.as_view(), name='purchased-products'),
	path('remove/<product>/', views.removeFromCart, name='remove-from-cart'),
	path('add/<product>/', views.addToCart, name='add-to-cart'),
	# path('', PostListView.as_view(), name='blog-home'),
    # path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

	## API's
	path('categoryProducts/<str:category>/', views.categoryProduct, name='category-product'),
	path('ratingOfProduct/<str:product>/', views.ratingOfProduct, name='rating-product'),
	path('compareProducts/<str:prod1>/<str:prod2>/', views.compareProducts, name='compare-products'),
	path('discountOfProduct/<str:product>/', views.discountOfProduct, name='discount-product'),
	# path('userCartItems/', views.userCartItems, name='user-cart'),
	# path('userPurchasedItems/', views.userPurchasedItems, name='user-purchased'),
	# path('userProfile/', views.userProfile, name='user-profile'),
	path('productDetails/<str:product>/', views.productDetails, name='product-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
