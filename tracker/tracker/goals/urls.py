from django.urls import path

from . import views

urlpatterns = [
    # path('api-values/', views.ListGeneric.as_view()),
    # path('api-values/<int:pk>/', views.DetailGeneric.as_view()),

    path('values/', views.ListValue.as_view()),
    path('values/<int:pk>/', views.ValueDetail.as_view()),
    path('values/add/', views.ValueAdd.as_view()),

    path('goals/', views.ListGoal.as_view()),
    path('goals/<int:pk>/', views.DetailGoal.as_view()),
    path('goals/add', views.AddGoal.as_view()),

    path('tasks/', views.ListTask.as_view()),
    path('tasks/<int:pk>/', views.DetailTask.as_view()),
    path('tasks/add', views.AddTask.as_view()),

    path('tracker/', views.ListTracker.as_view()),
    path('tracker/<int:pk>/', views.DetailTracker.as_view()),
    path('tracker/add', views.AddTracker.as_view()),


]
