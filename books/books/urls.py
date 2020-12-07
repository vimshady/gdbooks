from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books.library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('request/', views.BookRequestList.as_view()),
    path('request/<int:pk>/', views.BookRequestList.as_view()),

    path('request', views.BookRequestCreate.as_view({'post': 'post'})),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)