from django.shortcuts import render
from .serializers import BlogSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from blogapp.models import Blog
# Create your views here.


@csrf_exempt
def blog_list(request):
    if request.method == "GET":
        blogs = Blog.objects.all()
        ser = BlogSerializer(blogs, many=True)
        return JsonResponse(ser.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        ser = BlogSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)


@csrf_exempt
def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BlogSerializer(blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        blog.delete()
        return HttpResponse(status=204)
