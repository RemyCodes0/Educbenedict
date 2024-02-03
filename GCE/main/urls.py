from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name = "index"),
    path('ordinary/', views.ordinary, name = 'ordinary'),
    path("About/", views.about, name = 'about'),
    path('advanced/', views.advanced, name = 'advanced'),
    path('bac/', views.bac, name = 'bac'),
    path("scienceA/", views.scienceA, name ='scienceA'),
    path('artA/', views.artA, name = 'artA'),
    path("scienceO/", views.scienceO, name ='scienceO'),
    path('artO/', views.artO, name = 'artO'),
    path("year/<int:subject_id>", views.year, name= "year"),
    path("success/", views.success, name = "success"),
    path("ans/<int:year_id>", views.ans, name = 'ans'),
    path('paper/<int:year_id>', views.paper, name = 'paper'),
    path('paper1/<int:year_id>', views.paper1, name = 'paper1'), # type: ignore
    path('paper2/<int:year_id>', views.paper2, name = 'paper2'),
    path('paper3/<int:year_id>', views.paper3, name = 'paper3'),
    path('answer/', views.get_answer, name = "answer")

]