from django.shortcuts import render, redirect, HttpResponse
from .models import Customer, Product, Cart, OrderPlaced
# from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.views import View
from django.contrib import messages
# from django.http import JsonResponse
# from django.db.models import Q
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
	def get(self, request):
		totalitem = 0
		jee = Product.objects.filter(category='je')
            
  
		neet = Product.objects.filter(category='nt')
		ncert = Product.objects.filter(category='nc')
        
        
  
		# if request.user.is_authenticated:
		# 	totalitem = len(Cart.objects.filter(user=request.user))
		return render(request, 'app/home.html', {'jee':jee, 'neet':neet, 'ncert':ncert, 'totalitem':totalitem})
  


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
	def get(self, request, pk):
		totalitem = 0
		product = Product.objects.get(pk=pk)
		print(product.id)
		# item_already_in_cart=False
		# if request.user.is_authenticated:
		# 	totalitem = len(Cart.objects.filter(user=request.user))
		# 	item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
		return render(request, 'app/productdetail.html', {'product':product})
                #  , 'item_already_in_cart':item_already_in_cart, 'totalitem':totalitem

         
def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# def mobile(request):
#  return render(request, 'app/mobile.html')

def mobile(request, data=None):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	if data==None :
			mobiles = Product.objects.filter(category='M')
	elif data == 'Redmi' or data == 'Samsung':
			mobiles = Product.objects.filter(category='M').filter(brand=data)
	elif data == 'below':
			mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
	elif data == 'above':
			mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
	return render(request, 'app/mobile.html', {'mobiles':mobiles, 'totalitem':totalitem})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
