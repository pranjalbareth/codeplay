from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog, Application
import math

# Create your views here.
def home(requests):
	#return HttpResponse("this is home")
	return render(requests, 'index.html')

def blog(requests):
	no_of_posts = 4 
	page = requests.GET.get('page')
	if page is None:
		page = 1
	else:
		page = int(page)
	print(page)


	blogs = Blog.objects.all()
	length = len(blogs)
	blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]
	if page>1:
		prev = page - 1
	else:
		prev = None
	if page<math.ceil(length/no_of_posts):
		nxt = page + 1
	else:
		nxt = None


	context = {'blogs' : blogs, 'prev' : prev, 'nxt': nxt}
	return render(requests, 'bloghome.html', context)

def blogpost(request, slug):
	blog = Blog.objects.filter(slug=slug).first()
	context = {'blog' : blog}
	return render(request, 'blogpost.html', context)

def resources(requests):
	return render(requests, 'resources.html')

def projects(requests):
	return render(requests, 'projects.html')

def error_404(request, exception):
	return render(request, '404.html')

def join(requests):
	if requests.method == 'POST':
		name = requests.POST.get("name")
		email = requests.POST.get("email")
		desc = requests.POST.get("desc")
		phone = requests.POST.get("phone")
		position = requests.POST.get("position")
		instance = Application(name=name, email=email, desc=desc, phone=phone, position=position)
		instance.save()

	return render(requests, 'join.html') 
