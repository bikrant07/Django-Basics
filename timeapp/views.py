from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def showTime(request):
    current_time = datetime.datetime.now()
    # return HttpResponse(f"<h1>{current_time}<h1>")
    context = {
        "current_time": current_time
    }
    return render(request, "showTime.html", context)