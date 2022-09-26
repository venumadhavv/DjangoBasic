from django.urls import URLPattern, path
from . import views

urlpatterns=[
     path('',views.html,name="project1"),
     # path('1/<str:pk>/',views.project,name="project2"),
     path('2',views.create_project,name="create_project"),
     path('3/<str:pk>/',views.update_project,name="update_project"),
     path('4/<str:pk>',views.delete_project,name="delete_project")
]