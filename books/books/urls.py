from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.library import views

# router = routers.DefaultRouter()
# router.register(r'request', views.RequestViewSet, basename='request')

urlpatterns = [
    path('admin/', admin.site.urls),

    # path(r'request/<int:pk>', views.RequestDelete.as_view(), name='request-delete'),
    # path('request/<int:pk>', views.RequestViewSet.as_view({'get': 'retrieve'}), name='request-detail'),
    path('request/<int:pk>', views.request_view),
    path('request/<int:pk>/', views.request_view),
    path('request', views.request_view),
    path('request/', views.request_view),


    # path('', include(router.urls)),
]
