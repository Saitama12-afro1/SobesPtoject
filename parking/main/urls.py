from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('order', views.IndexList.as_view(), name= "index"),
    path('order/<int:pk>', views.IndexDetail.as_view(), name= "index_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)