from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('performers/', views.performer_index, name='performer-index'),
    path('performers/create', views.PerformerCreate.as_view(), name='performer-create'),
    path('performers/<int:performer_id>/', views.performer_detail, name='performer-detail'),
    path('performers/<int:pk>/update/', views.PerformerUpdate.as_view(), name='performer-update'),
    path('performer/<int:pk>/delete/', views.PerformerDelete.as_view(), name='performer-delete'),
    path('instructors/', views.InstructorList.as_view(), name='instructor-list'),
    path('instructors/create/', views.InstructorCreate.as_view(), name='instructor-create'),
    path('instructors/<int:pk>/', views.InstructorDetail.as_view(), name='instructor-detail'),
    path('instructors/<int:pk>/update/', views.InstructorUpdate.as_view(), name='instructor-update'),
    path('instructors/<int:pk>/delete/', views.InstructorDelete.as_view(), name='instructor-delete'),
    path('performers/<int:performer_id>/associate-instructor/<int:instructor_id>/', views.associate_instructor, name='associate-instructor'),
]
