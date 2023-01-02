from audioop import reverse
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




choice_list = [('Coading','Coading'),('Sports','Sports'),('Food','Food'),('Fashion','Fashion'),('Lifestyle','Lifestyle'),('Travel','Travel')]


class post(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    category=models.CharField(choices=choice_list, max_length=250,default="Coding")
    likes=models.ManyToManyField(User,related_name='blog_post')
    post_image=models.ImageField(null=True, blank=True, upload_to="images/post_images/")
    date_created=models.DateTimeField(auto_now_add=True)


    def total_likes(self):
        return self.likes.count()
        

    def __str__(self):
        return self.title +  str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class comment(models.Model):
    post=models.ForeignKey(post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    body=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s'%(self.post.title,self.name)

class categorys(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return '%s '%(self.name)
    
class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
	website_url = models.CharField(max_length=255, null=True, blank=True)
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	twitter_url = models.CharField(max_length=255, null=True, blank=True)
	instagram_url = models.CharField(max_length=255, null=True, blank=True)
	pinterest_url = models.CharField(max_length=255, null=True, blank=True)


	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')

