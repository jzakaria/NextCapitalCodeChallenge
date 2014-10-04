from django.shortcuts import render
from django.http import HttpResponseRedirect
from todo.models import Item
from todo.forms import ItemForm
import time

def index(request):
	if request.method == "POST":
		new_item = ItemForm(request.POST)
		if new_item.is_valid():
			data = new_item.cleaned_data
			item = Item()
			item.title = data['title']
			item.due = data['due'] 
			item.save();
			return HttpResponseRedirect('/todo')
		else:
			return HttpResponseRedirect(new_item.errors)
	else:
		try:
			item_list = sort_items_by_date()
		except Item.DoesNotExist:
			raise Http404
		return render(request, 'index.html', {'item_list':item_list, 'new_item_form':ItemForm()})

def sort_items_by_date():
	dt = dict()
	unique_dates = []
	item_list = Item.objects.all()
	
	for item in item_list:
		unique_dates.append(item.due)
	unique_dates = set(unique_dates)
	
	for date in unique_dates:
		dt[date] = Item.objects.filter(due=date)
	
	return dt