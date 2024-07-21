from django.urls import path
from . import views

urlpatterns = [
    # ------ Pages urls ------
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("predict/", views.predict, name="predict"),
    # ------ END ------
    path("load_artifacts/", views.load_saved_artifacts, name="load_artifacts"),
    path("get_location_names/", views.get_location_names, name="get_locations"),
    path("get_transactions/", views.get_transactions, name="get_transactions"),
    path("get_furnishing/", views.get_furnishing, name="get_furnishing"),
    path("get_society_names/", views.get_society_names, name="get_society"),
    path("predict_house_price/", views.predict_house_price, name="predict_house_price"),
]
