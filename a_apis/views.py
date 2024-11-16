from django.shortcuts import render
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/test")
def test(request):
    return {"message": "Hello, World!"}