from django.shortcuts import render
from ninja import NinjaAPI, Schema
from ninja.responses import JsonResponse

api = NinjaAPI()


@api.get("/test")
def test(request):
    return JsonResponse({"message": "Hello, World!"})