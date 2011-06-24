from django import http
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import bleach
import jingo
import json

def index(request):
	products = ('Firefox', 'Thunderbird', 'Camino', 'SeaMonkey', 'Fennec') # Fake data
	return jingo.render(request, 'products/productlist.html', {'products' : products})
	
def product(request, product):
	graph_data = """{"startDate":"2011-06-16","endDate":"2011-06-23","count":4,"item1":"7.0a1","ratio1":[[1308812400000,2.4868815974845],[1308726000000,2.7080774404866],[1308639600000,2.6543899526139],[1308553200000,2.345039339858],[1308466800000,3.4251623900124],[1308380400000,2.3958861781119],[1308294000000,2.3244163911432]],"item2":"6.0a2","ratio2":[[1308812400000,2.7362225414287],[1308726000000,3.0394356067741],[1308639600000,2.7123127662498],[1308553200000,2.9857037479364],[1308466800000,3.2714486049773],[1308380400000,3.3353135873716],[1308294000000,2.9510993176649]],"item3":"5.0","ratio3":[[1308812400000,0.3832930181813],[1308726000000,0.58759180746639],[1308639600000,1.056119768708],[1308553200000,1.1782427317091],[1308466800000,1.3024199276653],[1308380400000,1.409000955477],[1308294000000,1.3583489162734]],"item4":"4.0.1","ratio4":[[1308812400000,1.484767910694],[1308726000000,1.4488247503231],[1308639600000,1.5225934131267],[1308553200000,1.534991990846],[1308466800000,1.7328108137323],[1308380400000,1.7637062033621],[1308294000000,1.606210583892]]}""" # Fake data
	versions = ['7.0a1', '6.0a2', '5.0', '4.0.1'] # Fake data
	data = {'graph_data' : graph_data, 'versions': versions, 'product' : product}
	return jingo.render(request, 'products/dashboard.html', data)
	
def productBuild(request):
	pass
	
def topChangers(request):
	pass

def productVersion(request):
	pass
	
def productVersionTopChangers(request):
	pass
	
	