from django import http
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import bleach
import jingo

def index(request):
	products = ('Firefox', 'Thunderbird', 'Camino', 'SeaMonkey', 'Fennec')
	return jingo.render(request, 'products/productlist.html', {'products' : products})
	
def product(request, product):
	return HttpResponse("The product requested was " + product)
	
def productBuild(request):
	pass
	
def topChangers(request):
	pass

def productVersion(request):
	pass
	
def productVersionTopChangers(request):
	pass
	
	