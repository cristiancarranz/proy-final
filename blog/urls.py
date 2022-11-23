from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
	path('Post/new/', BlogCreateView.as_view(),name= 'post_new'),
	path('Post/<int:pk>/', BlogDetailView.as_view(),name='post_detail'),
	path('', BlogListView.as_view(), name='home'),
]
