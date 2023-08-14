from django.urls import path
from . import views

urlpatterns = [
    path('crews/', views.list_crew_members, name='crew_list'),
    path('crews/<int:id>/', views.crew_detail, name='crew_detail'),
    path('crews/new/', views.create_crew_member, name='create_crew'),
    path('crews/<int:id>/edit/', views.update_crew_member, name='update_crew'),
    path('crews/<int:id>/delete/', views.delete_crew_member, name='delete_crew'),

    path('ships/', views.list_ships, name='ship_list'),
    path('ships/<int:id>/', views.ship_detail, name='ship_detail'),
    path('ships/new/', views.create_ship, name='create_ship'),
    path('ships/<int:id>/edit/', views.update_ship, name='update_ship'),
    path('ships/<int:id>/delete/', views.delete_ship, name='delete_ship'),

    path('assignments/', views.list_assignments, name='assignment_list'),
    path('assignments/<int:id>/', views.assignment_detail, name='assignment_detail'),
    path('assignments/new/', views.create_assignment, name='create_assignment'),
    path('assignments/<int:id>/edit/', views.update_assignment, name='update_assignment'),
    path('assignments/<int:id>/delete/', views.delete_assignment, name='delete_assignment'),

    path('schedules/', views.list_schedules, name='schedule_list'),
    path('schedules/<int:id>/', views.schedule_detail, name='schedule_detail'),
    path('schedules/new/', views.create_schedule, name='create_schedule'),
    path('schedules/<int:id>/edit/', views.update_schedule, name='update_schedule'),
    path('schedules/<int:id>/delete/', views.delete_schedule, name='delete_schedule'),
]