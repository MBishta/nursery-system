"""
URL configuration for nursery_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

from core.views import ( 
                        home, reports_dashboard, register_child, record_attendance, record_checkout, register_teacher, 
                        list_teachers, edit_teacher, delete_teacher, record_teacher_attendance, register_parent )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('reports/', reports_dashboard, name='reports'),
    path('register-child/', register_child, name='register_child'),
    path('record-attendance/', record_attendance, name='record_attendance'),
    path('record-checkout/', record_checkout, name='record_checkout'),
    path('register-teacher/', register_teacher, name='register_teacher'),
    path('teachers/', list_teachers, name='list_teachers'),
    path('teachers/edit/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('teachers/delete/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('record-teacher-attendance/', record_teacher_attendance, name='record_teacher_attendance'),
    path('register-parent/', register_parent, name='register_parent')
]
