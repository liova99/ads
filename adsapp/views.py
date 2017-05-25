from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View  # normal template
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # create, update, delete object
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views import generic
from .models import Adds
from django.template import loader
from django.urls import reverse

from .forms import UserForm  # UserForm class that we created

# Create your views here.

class HomePageView(generic.ListView):

    template_name = 'adsapp/index.html'

    def get_context_data(self, **kwargs):
        """insert variables to Html"""
        context = super(HomePageView,self).get_context_data(**kwargs)
        context['name'] = 'Index'
        return  context

    # load from DB
    def get_queryset(self):
        return Adds.objects.all()

class AboutPageView(TemplateView):
    template_name = 'adsapp/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView,self).get_context_data(**kwargs)
        context['name'] = 'About'
        return  context

class DetailPageView(generic.DetailView):
    template_name = 'adsapp/detail.html'
    model = Adds  # we create an

    Adds.article_name = 'John'

class ArticleCreate(CreateView):
    model = Adds # we create Ads

    #spesify witch data can user import
    fields = ['article_name', 'price', 'city', 'category', 'details', 'photo']


    def get_context_data(self, **kwargs):
        context = super(ArticleCreate,self).get_context_data(**kwargs)
        context['name'] = 'Add Product'
        return  context


class ArticleUpdate(UpdateView):
    model = Adds # we create Ads

    #spesify witch data can user import
    fields = ['article_name', 'price', 'city', 'category', 'details', 'photo']


    def get_context_data(self, **kwargs):
        context = super(ArticleUpdate,self).get_context_data(**kwargs)
        context['name'] = 'Add Product'
        return  context


class ArticleDelete(DeleteView):
    model = Adds
    # where you wont to redirect after delete
    success_url = reverse_lazy('adsapp:index')


class UserFormView(View):

    # blueprint for this class
    form_class = UserForm
    template_name = 'adsapp/registration_form.html'

    # this function means if request == GET
    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'name': 'Registration'})


    # this function means if request == Post
    # process form to DB
    def post(self, request):
        form = self.form_class(request.POST)  # means everything that is in the post request

        if form.is_valid():  # django make the data validation
            user = form.save(commit = False)  #  create a object but not save it to DB yet.
            # clean (normolized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # password is encrypted by django so if we want to change users password we use this funtion
            user.set_password(password)
            user.save()  # send data to DB

            # returns User objects if credentials are correct, check the DB if this user exists
            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:  # not Baned or something
                    login(request, user)  # now they log't in
                    return redirect('adsapp:index')

            # if they didn't log in, try again:
        return render(request, self.template_name, {'form': form, 'name': 'Registration'})
