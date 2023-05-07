from django.contrib import admin
from django.urls import path,include
from .import views
# from .views import home, add_book,show_data

from django.urls import path
# from .views import home, add_book, show_data

# urlpatterns = [
#     path('', home),
#     path('add_book/', add_book, name='add_book'),
#     path('show_data/', show_data, name='show_data'),
# ]

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('show',views.show_data),
    path('add_data',views.add_data),
    path('delete',views.delete),
    path('edit',views.edit),
    path('RecordEdited',views.RecordEdited),
    path('search', views.search_book, name='book_search'),
]



