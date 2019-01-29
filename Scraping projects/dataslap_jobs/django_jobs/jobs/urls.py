from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('create/display_title/', views.TitleLabelGetCreate.as_view()),
    path('create/display_company/', views.CompanyLabelGetCreate.as_view()),

    path('label/expire/', views.ExpireJob.as_view()),
    path('label/apply_label/', views.LabelJob.as_view()),

    path('get/all_joined_jobs/', views.AllJobs.as_view()),
    path('get/titles/', views.TitleGet.as_view()),
    path('get/companies/', views.CompanyGet.as_view()),
    path('get/skills/', views.SkillsGet.as_view()),

    # path('create/', views.CreateValue.as_view()),
]
