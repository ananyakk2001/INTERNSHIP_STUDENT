from django.urls import path
from studentdetails.views import *

urlpatterns =[
     path('student/list',student_list,name='student_list'),
     path('batch/list',batch_list,name='batch_list'),
    path('school/list',school_list,name='school_list'),
    path('student/add', student_add, name='student-add'),
    path('batch/add', batch_add, name='batch-add'),
    path('school/add', school_add, name='school-add'),
    path('student/<int:student_id>/delete/', student_delete, name='student-delete'),
    path('student/<int:student_id>/edit/', student_edit, name='student-edit'),
    path('student/<int:student_id>/update/', student_update, name='student-update'),     
    path('student/<int:student_id>/batch/', StudentWithBatch.as_view(), name='student-with-batch'),
    path('school/<int:school_id>/Batch/',SchoolWithBatch.as_view(),name='School-With-Batch'),
    
]
