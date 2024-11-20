from django.shortcuts import render
import numpy as np
import pandas as pd
import joblib as jb

# Create your views here.
def main(request):
    return render(request, "main/index.html", context={})
