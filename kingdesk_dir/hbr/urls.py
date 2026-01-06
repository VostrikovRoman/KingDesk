from django.urls import path
from . import views

urlpatterns = [
    path('mcs/', views.my_current_shedule, name='hbr_mcs'),
    path('ocs/', views.our_current_shedule, name='hbr_ocs'),
    path('fs/', views.future_shedule, name='hbr_fs'),
    path('fs/happy_new_year/', views.future_shedule_hny, name='hbr_fs_hny'),
    path('profile/', views.profile, name='hbr_profile'), 
    path('profile/edit/', views.edit_profile, name='hbr_edit_profile'),
    path("profile/edit/<int:user_id>/", views.update_profile, name='hbr_update_profile'),
    path('employers/', views.employers, name='hbr_employers'),
    path('employers/<int:pk>', views.Employer_Detail_View.as_view(), name='hbr_employer_info'),
    path("fs/edit/<int:user_id>/", views.edit_shedule, name='hbr_fs_edit'),
    path("fs_hny/edit/<int:user_id>/", views.edit_shedule_hny, name='hbr_fs_edit_hny'),
    path('abra/<int:division_id>/', views.abra, name='abra'),
    path('send_wish/<int:user_id>/', views.send_wish, name='hbr_send_wish'),
    path('wishes/', views.wishes, name='hbr_wishes')
]