from django.urls import path
from .import views
urlpatterns=[
    path("",views.insert_home_page,name="insert_page"),
    path("insert",views.upload_home_data,name="upload_data"),
    path("fetch/",views.fetch_data_page,name="fetch"),
    path("edit/<int:pk>",views.edit_page,name="edit_link"),
    path("edit_upload/<int:pk>",views.edit_upload_page,name="upload_page"),
    path("edit_delete/<int:pk>",views.edit_delete_page,name="delete_page"),
    
    
]