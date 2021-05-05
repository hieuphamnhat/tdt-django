from django.urls import path
from . import views

urlpatterns = [
    path('', views.testapi, name="test-api"),
    path('company-list/', views.companyList, name="company-list"),
    path('company-detail/<str:pk>/', views.companyDetail, name="company-detail"),
    path('company-create/', views.companyCreate, name="company-create"),
    path('company-update/<str:pk>', views.companyUpdate, name="company-update"),
    path('company-delete/<str:pk>', views.companyDelete, name="company-delete"),
    path('list-companies/', views.view_company, name="list-companies"),
    path(r'^company/$', views.companyApi),
    path(r'^company/([0-9]+)$', views.companyApi)
]
