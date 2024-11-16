from django.shortcuts import render
from ninja import NinjaAPI, Schema, Response
from ninja.responses import JSONResponse

api = NinjaAPI()


@api.get("/test")
def test(request):
    return JSONResponse({"message": "Hello, World!"})