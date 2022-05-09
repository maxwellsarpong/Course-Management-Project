from rest_framework import serializers
from .models import Delegate,CourseType,PaymentMethod,Employee,Course,CourseFee,Location,Booking,Invoice,Registration

#serializer  for the Delegate
class DelegateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegate
        fields = '__all__'

#serializer for the CourseType
class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = '__all__'

#serializer for the PaymentMethod
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

#serializer for the Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

#serializer for the Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

#serializer for the CourseFee
class CourseFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFee
        fields = '__all__'

#serializer for the Location
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

#serializer for the Booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

#serializer for the Invoice
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

#serializer for the registration
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
