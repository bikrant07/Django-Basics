from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def userList(request):
    users=[
        {"id":1,"name":"Bikrant","age":22},
        {"id":2,"name":"Suman","age":21},
        {"id":3,"name":"Sujan","age":23},
        {"id":4,"name":"Sushil","age":24},
    ]
    return JsonResponse(users,safe=False)
