from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    # path('', views.index),
    path('', views.PostListView.as_view()),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_details, name='post_details')
]
