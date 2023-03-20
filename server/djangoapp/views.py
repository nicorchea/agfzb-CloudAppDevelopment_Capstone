from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from .restapis import get_dealers_from_cf
from .restapis import get_dealer_reviews_from_cf

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
#def contact(request):
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

def login_request(request):
        context = {}
        # Handles POST request
        if request.method == "POST":
            # Get username and password from request.POST dictionary
            username = request.POST['username']
            password = request.POST['psw']
            # Try to check if provide credential can be authenticated
            user = authenticate(username=username, password=password)
            if user is not None:
                # If user is valid, call login method to login current user
                login(request, user)
                return redirect('djangoapp/login.html')
            else:
                # If not, return to login page again
                return render(request, 'djangoapp/login.html', context)
        else:
            return render(request, 'djangoapp/login.html', context)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def logout_request(request):
        # Get the user object based on session id in request
        # Logout user in the request
        logout(request)
        # Redirect user back to course list view
        return redirect('djangoapp/logout.html')

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...
def registration_request(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships

def get_dealerships(request):
    context = {}
    if request.method == "GET":
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/c9d1715f-fd0a-4317-9161-5032ff1121c2/dealership-package/get-dealership"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        
        # Add dealerships to the context
        context['dealerships'] = dealerships
        
        # Render the template with the context
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...
def get_dealer_details(request, dealer_id):

    if request.method == "GET":
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/c9d1715f-fd0a-4317-9161-5032ff1121c2/dealership-package/get-review"
        # Get dealers from the URL
        dealerships = get_dealer_reviews_from_cf(url, dealer_id)
        # Find dealer with matching ID
        dealer = next((dealer for dealer in dealerships if dealer.id == dealer_id), None)
        if dealer:
            # Return details for matching dealer
            response_data = {
                'id': dealer.id,
                'name': dealer.name,
                'dealership': dealer.dealership,
                'review': dealer.review,
                'purchase': dealer.purchase,
                'another': dealer.another,
                'purchase_date': dealer.purchase_date,
                'car_make': dealer.car_make,
                'car_model': dealer.car_model,
                'car_year': dealer.car_year,
            }
            return JsonResponse(response_data)
        else:
            # Return error message if no matching dealer found
            return HttpResponse(f'Dealer with ID {dealer_id} not found')

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

