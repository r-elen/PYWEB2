from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View


class ViewCart(View):
   def get(self, request):
       return render(request, 'blog/blog.html')

class ViewBlogSingle(View):
   def get(self, request):
       return render(request, 'blog/blog-single.html')
