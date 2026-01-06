from django.urls import path
from . import views

 

urlpatterns = [
    path('wishes/', views.wishes, name='aup_wishes'),
    path('send_wish/<int:user_id>/', views.send_wish, name='aup_send_wish'),
    path('cs/', views.current_shedule, name='aup_cs'),
    path('fs/', views.future_shedule, name='aup_fs'),
    path('fs/hny/', views.future_shedule_hny, name='aup_fs_hny'),
    path('ct/', views.current_tasks, name='aup_ct'),
    path('ft/', views.future_tasks, name='aup_ft'),
    path('cs/edit/<int:user_id>', views.edit_current_shedule, name='aup_edit_cs'),
    path('fs/edit/<int:user_id>', views.edit_future_shedule, name='aup_edit_fs'),
    path('fs_hny/edit/<int:user_id>', views.edit_future_shedule_hny, name='aup_edit_fs_hny'),
    path('profile/', views.profile, name='aup_profile'),
    path('profile/edit/', views.edit_profile, name='aup_edit_profile'),
    path("profile/edit/<int:user_id>/", views.update_profile, name='aup_update_profile'),
    path('employers/', views.employers, name='aup_employers'),
    path('employers/<int:pk>', views.Employer_Detail_View.as_view(), name='aup_employer_info'),
    path('employers/add', views.add_employer, name='aup_add_employer'),
    path('employers/register', views.register_employer, name='aup_register_employer'),
    path("employers/<int:user_id>/delete", views.delete_employer, name='aup_delete_employer'),
    path("employers/<int:user_id>/edit", views.edit_employer, name='aup_edit_employer'),
    path("employers/<int:user_id>/update/", views.update_employer, name='aup_update_employer'),
    path("fs/<int:division_id>/stop/", views.stop_future, name='aup_stop_future'),
    path("fs/<int:division_id>/update/", views.update_shedule, name='aup_update_shedule'),
    path("export_to_excel/", views.export_to_excel, name='export_to_excel'),
    path("export_to_excel_future/", views.export_to_excel_future, name='export_to_excel_future'),
    path("import_from_excel/", views.import_from_excel, name='import_from_excel'),
]