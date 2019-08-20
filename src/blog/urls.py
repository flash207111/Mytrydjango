from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update/', views.ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', views.ArticleDeleteView.as_view(), name='article-delete'),
    path('create/', views.ArticleCreateView.as_view(), name='article-create'),
]
