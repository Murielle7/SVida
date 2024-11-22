from django.urls import path
from .views import register, edit_patient, user_login, user_logout, add_patient, add_vital_sign, vital_sign_history, menu
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_patient/', add_patient, name='add_patient'),
    path('add_vital_sign/<int:patient_id>/', views.add_vital_sign, name='add_vital_sign'),
    path('vital_sign_history/<int:patient_id>/', vital_sign_history, name='vital_sign_history'),  # Histórico de sinais vitais
    path('menu/', menu, name='menu'),
    path('success/', views.success_page, name='success_page'),
    path('save_edit_patient/<int:patient_id>/', views.save_edit_patient, name='save_edit_patient'),
    path('patient/edit/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('patients/', views.patient_list, name='patient_list'),
    path('select_patient_for_vital_signs/', views.select_patient_for_vital_signs, name='select_patient_for_vital_signs'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),

]
