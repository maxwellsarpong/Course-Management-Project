from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('api/delegate/', DelegateList.as_view()),
    path('api/delegate/<int:pk>/', DelegateDetail.as_view()),
    path('api/course-type/', CourseTypeList.as_view()),
    path('api/course-type/<int:pk>/', CourseTypeDetail.as_view()),
    path('api/payment-method/', PaymentMethodList.as_view()),
    path('api/payment-method/<int:pk>/', PaymentMethodDetail.as_view()),
    path('api/employee/', EmployeeList.as_view()),
    path('api/employee/<int:pk>/', EmployeeDetail.as_view()),
    path('api/course/', CourseList.as_view()),
    path('api/course/<int:pk>/', CourseDetail.as_view()),
    path('api/course-fee/', CourseFeeList.as_view()),
    path('api/course-fee/<int:pk>/', CourseFeeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)