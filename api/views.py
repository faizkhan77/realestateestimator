from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
import numpy as np
import warnings


__locations = None
__transactions = None
__furnishing = None
__society = None
__data_columns = None
__model = None


# Create your views here.


# -------------------------------- Pages View --------------------------------
def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def predict(request):
    return render(request, "predict.html")


# ----------------------------------------------------------------


def get_location_names(request):
    load_saved_artifacts(request)
    return JsonResponse({"location names": __locations})


def get_transactions(request):
    # return __transactions
    load_saved_artifacts(request)
    return JsonResponse({"transaction": __transactions})


def get_furnishing(request):
    # return __furnishing
    load_saved_artifacts(request)
    return JsonResponse({"furnishing": __furnishing})


def get_society_names(request):
    # return __society
    load_saved_artifacts(request)
    return JsonResponse({"society names": __society})


# ---------------------------------------------------------


def get_estimated_price(
    pr,
    floor,
    bathroom,
    balcony,
    carpet,
    parking,
    bhk,
    location,
    transaction,
    furnish,
    society,
):

    try:
        loc_index = __data_columns.index(location.lower())
        tran_index = __data_columns.index(transaction.lower())
        fur_index = __data_columns.index(furnish.lower())
        soc_index = __data_columns.index(society.lower())
    except:
        loc_index = -1
        tran_index = -1
        fur_index = -1
        soc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = pr
    x[1] = floor
    x[2] = bathroom
    x[3] = balcony
    x[4] = carpet
    x[5] = parking
    x[6] = bhk

    if loc_index >= 0:
        x[loc_index] = 1
    if tran_index >= 0:
        x[tran_index] = 1
    if fur_index >= 0:
        x[fur_index] = 1
    if soc_index >= 0:
        x[soc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts(request):
    warnings.filterwarnings("ignore")

    print("loading saved artifacts...start..")
    global __data_columns
    global __model
    global __locations
    global __transactions
    global __furnishing
    global __society

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[7:87]
        __transactions = __data_columns[87:89]
        __furnishing = __data_columns[89:91]
        __society = __data_columns[91:]

    with open("./artifacts/house_prices.pickle", "rb") as f:
        __model = pickle.load(f)

    # print(get_location_names))

    return HttpResponse("Artificats have been loaded")


@csrf_exempt
def predict_house_price(request):
    load_saved_artifacts(request)
    if request.method == "POST":
        pr = float(request.POST.get("pr"))
        floor = int(request.POST.get("floor"))
        bathroom = int(request.POST.get("bathroom"))
        balcony = int(request.POST.get("balcony"))
        total_sqft = float(request.POST.get("total_sqft"))
        num_of_parking = int(request.POST.get("num_of_parking"))
        bhk = int(request.POST.get("bhk"))
        location = request.POST.get("location")
        transaction = request.POST.get("transaction")
        furnishing = request.POST.get("furnishing")
        society = request.POST.get("society")

        estimated_price = get_estimated_price(
            pr,
            floor,
            bathroom,
            balcony,
            total_sqft,
            num_of_parking,
            bhk,
            location,
            transaction,
            furnishing,
            society,
        )

    return JsonResponse({"estimated_price": estimated_price})
