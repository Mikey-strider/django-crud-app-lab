from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('/', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('instructors/', views.instructor_index, name='instructor-index'),
    path('performers/', views.performer_index, name='performer-index'),

]
