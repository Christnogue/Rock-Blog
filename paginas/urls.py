from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPages, name='page_list'),
    path('create', views.createPage, name='create_page'),
    path('<int:page_id>', views.getPage, name='get_page'),
    path('<int:page_id>/update', views.updatePage, name='update_page'),
    path('<int:page_id>/delete', views.deletePage, name='delete_page'),
]