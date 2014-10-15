from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from todo.models import Item
from todo.forms import ItemForm, NewUserForm, UserForm
import time
import collections
import logging

@login_required
def todos(request, user_id):
	#this should never happen, but if it does, sign out the 
	# user immediately
	if int(user_id) != request.user.id:
		return HttpResponseRedirect('/users/sign_out/')
	if request.method == "POST":
		new_item = ItemForm(request.POST)
		if new_item.is_valid():
			data = new_item.cleaned_data
			item = Item()
			item.title = data['title']
			item.date = data['date']
			item.user_id = request.user.id
			item.save();
			return HttpResponseRedirect('')
		else:
			return HttpResponseRedirect(new_item.errors)
	else:
		try:
			item_list = sort_items_by_date(user_id)[0]
		except Item.DoesNotExist:
			raise Http404
		return render(request, 'index.html', {'item_list':item_list, 'new_item_form':ItemForm()})

def archives(request, user_id):
	if int(user_id) != request.user.id:
		return HttpResponseRedirect('/users/sign_out/')
	try:
		archives = sort_items_by_date(request.user.id)[1]
	except Item.DoesNotExist:
		raise Http404
	return render(request, 'archives.html', {'item_list':archives })

def sort_items_by_date(usr_id):
	dt = dict()
	archive = dict()
	unique_dates = []
	item_list = Item.objects.filter(user_id=usr_id)
	
	for item in item_list:
		unique_dates.append(item.date)
	unique_dates = set(unique_dates)
	
	for date in unique_dates:
		dt[date] = Item.objects.filter(date=date)
		if is_day_complete(dt[date]):
			archive[date] = dt[date]
			dt.pop(date, None)
	
	dt = collections.OrderedDict(sorted(dt.items()))
	return (dt, archive)

def item_mark(request):
	if request.method == "POST":
		item_id = request.POST['item_id']
		Item.objects.filter(id=item_id).update(completed=True)
		import ipdb; ipdb.set_trace()

		url = "/users/%d/todos" % request.user.id
    	return HttpResponseRedirect(url)


def is_day_complete(item_list):
	ct = 0;
	for item in item_list:
		if item.completed:
			ct+=1;
	if ct == len(item_list):
		return True
	return False


def register(request):
    context = RequestContext(request)
    login_form = UserForm()
    error = ""

    if request.user.is_authenticated():
    	url = "%d/todos" % request.user.id
    	return HttpResponseRedirect(url)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        user_form = NewUserForm(data=request.POST)

        # If form is valid...
        if user_form.is_valid():
			user_data = user_form.clean()

			# Save the user's form data to the database.
			user = User()
			user.username = user_data['email']

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user_data['password1'])
			user.save()

			# Update our variable to tell the template registration was successful.
			registered = True

			user = authenticate(username=user_data['email'], password=user_data['password1'])
			login(request, user)

			return HttpResponseRedirect("/users/sign_in/")

        # Print problems to the terminal. They'll also be shown to the user.
        else:
            error = user_form.errors

    # Not a HTTP POST, so we render our form.
    # This form will be blank, ready for user input.
    else:
        user_form = NewUserForm()

    # Render the template depending on the context.
    return render(request, 'register.html', {'user_form': user_form, 'login_form':login_form,'registered': registered, "login_errors":error, "signup_errors":""})


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    user_form = NewUserForm()
    error = ""

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        email = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=email, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				url = "/users/%d/todos" % request.user.id 
				return HttpResponseRedirect(url)
            else:
                # An inactive account was used - no logging in!
                error = "Your account is disabled. Please contact jzakaria@uchicago.edu to get it reactivated."
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(email, password)
            error = "Invalid login details supplied."

    else:
        if request.user.is_authenticated():
			url = "/users/%d/todos" % request.user.id 
			return HttpResponseRedirect(url)

    return render(request, 'register.html', {'login_form': UserForm, 'user_form':user_form, "login_errors":error, "signup_errors":""})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/users')