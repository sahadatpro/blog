from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name='post_list'),
    path('tag/<str:tag_slug>/', views.index, name='posts_list_by_tag'),
    # path('', views.PostListView.as_view()),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_details, name='post_details')
]
