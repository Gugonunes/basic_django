from django.urls import path
from blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.blog, name='home'),
    path('<int:post_id>/', blog_views.post, name='post'),
    path('exemplo/', blog_views.exemplo, name='exemplo')
]
