# this file contains the views in the product app
# And it even contains API's to request product details from MongoDB

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.models import Profile
from django.contrib import messages
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from pprint import pprint

class ProductListView(ListView):
	model = Product
	template_name = 'products/home.html'
	context_object_name = 'products'
	paginate_by = 5

class UserCartProductListView(LoginRequiredMixin, ListView):
	model = Product
	template_name = 'products/user_cart_products.html'	# <app>/<model>_<viewtype>.html
	context_object_name = 'products'
	paginate_by = 5

	def get_queryset(self):
		user_profile = Profile.objects.get(user=self.request.user)
		return user_profile.cart.all()

class UserPurchasedProductListView(LoginRequiredMixin, ListView):
	model = Product
	template_name = 'products/user_purchased_products.html'	# <app>/<model>_<viewtype>.html
	context_object_name = 'products'
	paginate_by = 5

	def get_queryset(self):
		user_profile = Profile.objects.get(user=self.request.user)
		return user_profile.purchased.all()

@login_required
def addToCart(request, product):
	user_profile = Profile.objects.get(user=request.user)
	try:
		addedToCart = user_profile.cart.add(product)
		if not addedToCart:		#this is weird because this line is little confusing but it's correct
			messages.success(request, f'Item added')
		else:
			messages.warning(request, f'Could not add item')
	except Exception as e:
		messages.success(request, f'Item already present in the cart. \n Sorry but you can\'t buy more than one')
	return redirect('cart-products')

@login_required
def removeFromCart(request, product):
	user_profile = Profile.objects.get(user=request.user)
	if not user_profile.cart.remove(product):
		messages.success(request, f'Item removed')
	else:
		messages.warning(request, f'Could not remove item')
	return redirect('cart-products')


# API's
from bson.json_util import dumps
import json

# the following API requests products of requested category from DB
@api_view(['GET'])
def categoryProduct(request, category, format=None):
	if request.method == 'GET':
		products = Product.objects.mongo_find({ 'type' : category })
		if products:
			return Response(json.loads(dumps(products)))
		else:
			return Response(json.loads('{ "query" : "empty" }'))

# following API requests rating of a particular product
@api_view(['GET'])
def ratingOfProduct(request, product, format=None):
	if request.method == 'GET':
		products = Product.objects.mongo_find({ 'title' : product })
		if products:
			return Response(json.loads(dumps(products)))
		else:
			return Response(json.loads('{ "query" : "empty" }'))

# the followig API requests data for comparing two products
@api_view(['GET'])
def compareProducts(request, prod1, prod2, format=None):
	if request.method == 'GET':
		products = Product.objects.mongo_find({ 'title' : { '$in' : [prod1, prod2] } })
		if products:
			return Response(json.loads(dumps(products)))
		else:
			return Response(json.loads('{ "query" : "empty" }'))

# following API requests discount of a particular product
@api_view(['GET'])
def discountOfProduct(request, product, format=None):
	if request.method == 'GET':
		products = Product.objects.mongo_find({ 'title' : product})
		if products:
			return Response(json.loads(dumps(products)))
		else:
			return Response(json.loads('{ "query" : "empty" }'))

# @api_view(['POST'])
# def userCartItems(request, format=None):
# 	if request.method == 'POST':
# 		pprint(request.data['id'])
# 		user_profile = Profile.objects.mongo_find({ 'id' : request.data['id']})
# 		products = user_profile.cart.mongo_find()
# 		if products:
# 			return Response(json.loads(dumps(products)))
# 		else:
# 			return Response(json.loads('{ "query" : "empty" }'))

# @api_view(['POST'])
# def userPurchasedItems(request, format=None):
# 	if request.method == 'POST':
# 		user_profile = Profile.objects.get(user=request.user)
# 		products = user_profile.purchased.mongo_find()
# 		if products:
# 			return Response(json.loads(dumps(products)))
# 		else:
# 			return Response(json.loads('{ "query" : "empty" }'))

# @api_view(['POST'])
# def userProfile(request, format=None):
# 	if request.method == 'POST':
# 		user_profile = Profile.objects.get(user=request.user)
# 		if user_profile:
# 			return Response(json.loads(dumps(user_profile)))
# 		else:
# 			return Response(json.loads('{ "query" : "empty" }'))

# the following API requests for one product details
@api_view(['GET'])
def productDetails(request, product, format=None):
	if request.method == 'GET':
		products = Product.objects.mongo_find({ 'title' : product})
		if products:
			return Response(json.loads(dumps(products)))
		else:
			return Response(json.loads('{ "query" : "empty" }'))