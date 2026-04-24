from django .urls  import path
from . import views
urlpatterns = [
   
 path('home/', views.home, name='home'),
 path('students/', views.student_list, name='student_list'),
 path('add/', views.add_student, name='add_student'),
 path('update/<int:pk>/', views.update_student, name='update_student'),
 path('delete/<int:pk>/', views.delete_student, name='delete_student'),
 path('search/', views.search_student, name='search_student'),
 path('logout/', views.logout_view, name='logout'),

]