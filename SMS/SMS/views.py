from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from main.models import BlogPost, Game, Screenshots, LandingPageDetails



def listBlogs(request):
	landingPageDetails = LandingPageDetails.objects.all()[0]
	context = {
		'details': landingPageDetails,
		'posts': BlogPost.objects.all(),
	}
	return render (request, 'main/blogList.html', context)

def blog(request, single_slug):
	landingPageDetails = LandingPageDetails.objects.all()[0]
	recentPosts = BlogPost.objects.all().order_by('published')[:3]
	posts = [t.slug for t in BlogPost.objects.all()]
	if single_slug in posts:
		blog = BlogPost.objects.get(slug = single_slug)


		context = {
			'details': landingPageDetails,
			'title': blog.title,
			'content' : blog.content,
			'posts': recentPosts,
			'image': blog.image,
			'published': blog.published,
		}


		return render(request, 'blog.html', context)
	else:
		return redirect('/')


def landing(request):
	# return HttpResponse('Hello World')

	screenshotss = Screenshots.objects.all()
	aboutThumb = screenshotss[0]
	landingPageDetails = LandingPageDetails.objects.all()[0]
	user = request.user
	games = Game.objects.all()
	posts = BlogPost.objects.all().order_by('published')[:3]
	hello = 'hello world'
	context = {
		'aboutThumb': aboutThumb,
		'details': landingPageDetails,
		'screenshots':screenshotss,
		'games': games,
		'posts': posts,

	}
	
	return render(request, 'landing.html', context)




def register(request):
	landingPageDetails = LandingPageDetails.objects.all()[0]
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,  f"New Account Created: {username}")
			login(request, user)
			messages.info(request,  f"You are now logged in as {username}")
			return redirect('/login/')
		else:
			for msg in form.error_messages:
				messages.error(request, f"Something Went Wrong! Password Don't Match or Username/Email already Exists!")

	


	form = NewUserForm
	context = {
		'details':landingPageDetails,
		'form': form,
	}

        
	if request.user.is_authenticated:
		return redirect(app + '/login/')
	else:
		return render(request, 'main/register.html', context )
	
def logout_request(request):
	logout(request)
	messages.info(request, f"Logged Out Successfully!")
	return redirect('/')

def login_request(request):
	landingPageDetails = LandingPageDetails.objects.all()[0]
        
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if (user is not None):
				login(request, user)
				messages.info(request,  f"You are now logged in as {username}")
				return redirect('/forums/')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")



	form = AuthenticationForm()
	context = {
		'details':landingPageDetails,
		"form": form,
	}
	if request.user.is_authenticated:
		return redirect('/forums/')
	else:
		return render(request, "main/login.html", context)

	
