from django.urls import path
from . import views


app_name = 'courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses-list'),
    path('create/', views.CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/', views.CourseView.as_view(), name='courses-detail'),
    path('<int:id>/update', views.CourseUpdateView.as_view(), name='courses-update'),
    path('<int:id>/delete', views.CourseDeleteView.as_view(), name='courses-delete'),
    # path('', views.my_vbf, name='courses-list' ),
]
