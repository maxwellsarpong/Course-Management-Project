from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

#views  for the delegate
class DelegateList(APIView):
    """
    List all delegate, or create a new delegate.
    """
    def get(self, request, format=None):
        delegate = Delegate.objects.all()
        serializer = DelegateSerializer(delegate, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DelegateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DelegateDetail(APIView):
    """
    Retrieve, update or delete a delegate instance.
    """
    def get_object(self, pk):
        try:
            return Delegate.objects.get(pk=pk)
        except Delegate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        delegate = self.get_object(pk)
        serializer = DelegateSerializer(delegate)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        delegate = self.get_object(pk)
        serializer = DelegateSerializer(delegate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        delegate = self.get_object(pk)
        delegate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###### views for the CourseType
class CourseTypeList(APIView):
    """
    List all delegate, or create a new delegate.
    """
    def get(self, request, format=None):
        course_type = CourseType.objects.all()
        serializer = CourseTypeSerializer(course_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseTypeDetail(APIView):
    """
    Retrieve, update or delete a course_type instance.
    """
    def get_object(self, pk):
        try:
            return CourseType.objects.get(pk=pk)
        except CourseType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course_type = self.get_object(pk)
        serializer = CourseTypeSerializer(course_type)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course_type = self.get_object(pk)
        serializer = CourseTypeSerializer(course_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course_type = self.get_object(pk)
        course_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###### views for the PaymentMethod
class PaymentMethodList(APIView):
    """
    List all payment_method , or create a new delegate.
    """
    def get(self, request, format=None):
        payment_method = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(payment_method , many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentMethodDetail(APIView):
    """
    Retrieve, update or delete a course_type instance.
    """
    def get_object(self, pk):
        try:
            return PaymentMethod.objects.get(pk=pk)
        except PaymentMethod.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        payment_method = self.get_object(pk)
        serializer = PaymentMethodSerializer(payment_method)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payment_method = self.get_object(pk)
        serializer = PaymentMethodSerializer(payment_method, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        payment_method = self.get_object(pk)
        payment_method.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###### views for the Employee
class EmployeeList(APIView):
    """
    List all employee , or create a new delegate.
    """
    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    """
    Retrieve, update or delete an employee instance.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###### views for the Course
class CourseList(APIView):
    """
    List all employee , or create a new delegate.
    """
    def get(self, request, format=None):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):
    """
    Retrieve, update or delete an employee instance.
    """
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###### views for the CourseFee
class CourseFeeList(APIView):
    """
    List all employee , or create a new delegate.
    """
    def get(self, request, format=None):
        course_fee = CourseFee.objects.all()
        serializer = CourseFeeSerializer(course_fee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseFeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseFeeDetail(APIView):
    """
    Retrieve, update or delete an employee instance.
    """
    def get_object(self, pk):
        try:
            return CourseFee.objects.get(pk=pk)
        except CourseFee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course_fee = self.get_object(pk)
        serializer = CourseFeeSerializer(course_fee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course_fee = self.get_object(pk)
        serializer = CourseFeeSerializer(course_fee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course_fee = self.get_object(pk)
        course_fee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)