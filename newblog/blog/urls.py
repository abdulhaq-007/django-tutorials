from django.urls import path
from .views import PostListView, PostTemplateView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list_view'),
]