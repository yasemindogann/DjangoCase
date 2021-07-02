from django.urls import path
from pages.views import *


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('contact/', contactView, name="contact"),
    path('form_sorgula/', formSorgulaView, name="form_sorgula"),
    # path('selectlanguage/', selectlanguage, name="selectlanguage"),
]
