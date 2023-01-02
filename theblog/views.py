from genericpath import exists
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import add_post_form,Edit_settings_Form,password_change_form,ProfilePage_Form,SignUpForm
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import  reverse_lazy,reverse
from django.http import HttpResponseRedirect

from .models import comment, post,Profile


class homeview(ListView):
    model = post
    template_name = 'home.html'

class artical_detailview(DetailView):
    model=post
    template_name='artical_detail.html'


    def get_context_data(self, **kwargs): 
        context= super(artical_detailview,self).get_context_data(**kwargs)
        
        like=get_object_or_404(post,id=self.kwargs['pk'])
        
        liked=False
        if like.likes.filter(id=self.request.user.id).exists():
            liked=True
        total_likes= like.total_likes()
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context
        


class commentview(CreateView):
    model=comment
    fields=('name','body')
    template_name='registration/create_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url=reverse_lazy('home')
        

class add_postview(CreateView):
    model=post
    form_class= add_post_form
    template_name ='add_post.html'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
       

class upadte_post_view(UpdateView):
    model=post
    template_name = 'update_post.html'
    fields= ("title","body","author")

class delete_post_view(DeleteView):
    model=post
    template_name='delete_post.html'
    success_url = reverse_lazy('home')


class UserRegisterView(CreateView):
	form_class = SignUpForm
	template_name = 'regester.html'
	success_url = reverse_lazy('login')

    

def LikeView(request, pk):
    Post=get_object_or_404(post, id = request.POST.get('post_id'))
    liked=False
    if Post.likes.filter(id=request.user.id).exists():
        Post.likes.remove(request.user)
        liked=False
    else:
        Post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('detail_view', args=[str(pk)]))


class edit_user_settings(UpdateView):
    form_class=Edit_settings_Form 
    template_name='registration/edit_user_settings.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user


class Password_change_view(PasswordChangeView):
    form_class=password_change_form
    template_name='registration/password_change.html'
    success_url=reverse_lazy('home')


class Create_ProfilePage_View(CreateView):
	model = Profile
	form_class = ProfilePage_Form
	template_name = "registration/create_user_profile_page.html"
	#fields = '__all__'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)



class Show_ProfilePage_View(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		
		context = super(Show_ProfilePage_View, self).get_context_data(*args, **kwargs)
		
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context

class upadte_profile_view(UpdateView):
    model=Profile
    template_name = 'registration/update_profile.html'
    form_class=ProfilePage_Form


def categoryview(request, cat):
    Post=post.objects.filter(category=cat)
    context={'Post':Post}
    return render(request,'Category_post_List.html',context)