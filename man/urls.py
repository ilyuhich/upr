from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Morda.as_view(), name='morda'),
    path('district/all/', DistrictList.as_view(), name='district-list'),
    path('district/add/', DistrictCreate.as_view(), name='district-add'),
    path('district/<int:pk>/', DistrictDetail.as_view(), name='district-detail'),
    path('district/<int:pk>/update/', DistrictUpdate.as_view(), name='district-update'),
    path('district/<int:pk>/delete/', DistrictDelete.as_view(), name='district-delete'),
    path('opr/', OpenProblems.as_view(), name='opr'),
    path('problem/create/', ProblemCreate.as_view(), name='problem-create'),
    path('problem/<int:pk>/', ProblemDetail.as_view(), name='problem-detail'),
    path('apr/', AllProblems.as_view(), name='all_pr'),
    path('place/create/', PlaceCreate.as_view(), name='place-create'),
]
