import requests
import json
from .models import CarDealer
from .models import DealerReview


from requests.auth import HTTPBasicAuth




# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Create a CarDealer object with values in `dealer` dictionary
            dealer_obj = CarDealer(address=dealer["address"], city=dealer["city"], full_name=dealer["full_name"],
                                   id=dealer["id"], lat=dealer["lat"], long=dealer["long"],
                                   short_name=dealer["short_name"],
                                   st=dealer["st"], zip=dealer["zip"], state=dealer["state"])
                                   
            results.append(dealer_obj)

    return results




# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_reviews_from_cf(url, dealer_id, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, dealerId=dealer_id)
    print(json_result)  # Add this line to print out the value of json_result
    if json_result:
        # Get the dealer object from JSON
        dealer = json_result["review"]
        print(dealer)
        # Create a CarDealer object with values in `dealer` dictionary
        dealer_obj = DealerReview( name=dealer["name"], dealership=dealer["dealership"], purchase=dealer["purchase"],
                           review=dealer["review"], purchase_date=dealer["purchase_date"], car_make=dealer["car_make"],
                           car_model=dealer["car_model"],
                           car_year=dealer["car_year"], id=dealer["id"])
        results.append(dealer_obj)
        print(results)

    return results


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative


