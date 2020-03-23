from django.conf.urls import url
from .import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout
import blog.scripts.insert_books as books

urlpatterns=[
	url(r'^$',views.home),
	url(r'^login/$', LoginView.as_view(template_name='blog/login.html'), name='login'),
	url(r'^logout/$', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
	url(r'^register/$',views.register,name='register'),
	url(r'^profile/$',views.profile,name='profile'),
	url(r'^search/$',views.search,name='search'),
]

# ------ Put all the starting scripts here -----------#

# inserting books into the books models
books.insert_books()
