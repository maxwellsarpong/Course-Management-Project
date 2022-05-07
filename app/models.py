from django.db import models

#model for the Delegate
class Delegate(models.Model):
    delegateNo = models.BigAutoField(primary_key=True)
    delegateTitle = models.CharField(max_length=50, blank=False)
    delegateFName = models.CharField(max_length=100, blank=False)
    delegateLName = models.CharField(max_length=100, blank=False)
    delegateStreet = models.TextField(max_length=100, blank=True)
    delegateCity = models.CharField(max_length=100, blank=True)
    delegateState = models.CharField(max_length=100, blank=True)
    delegateZipCode = models.CharField(max_length=100, blank=True)
    attTelNo = models.IntegerField(max_length=10, blank=False)
    attFaxNo = models.IntegerField(max_length=10, blank=False)
    attEmailAddress = models.CharField(max_length=100, blank=True)
    clientNo = models.IntegerField(max_length=5, blank=False)

    class Meta:
        ordering = ['delegateNo']
        verbose_name_plural = 'Delegate'

#model for the CourseType
class CourseType(models.Model):
    course_type_no = models.BigAutoField(primary_key=True)
    course_type_description = models.TextField(blank=False)

    class Meta:
        ordering = ['course_type_no']
        verbose_name_plural = 'CourseType'

#model for the payment method
class PaymentMethod(models.Model):
    payment_method_no = models.BigAutoField(primary_key=True)
    payment_name = models.CharField(blank=False, max_length=50)

    class Meta:
        ordering = ['payment_method_no']
        verbose_name_plural = 'PaymentMethod'

#model for the Employee
class Employee(models.Model):
    employee_no = models.BigAutoField(primary_key=True)
    employee_fname = models.CharField(blank=False, max_length= 100)
    employee_lname = models.CharField(blank=False, max_length=100)

    class Meta:
        ordering = ['employee_no']
        verbose_name_plural = 'Employee'

#model for the Course
class Course(models.Model):
    course_no = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=50, blank=False)
    course_description = models.TextField(max_length=100, blank=True)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    start_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)
    max_delegate = models.IntegerField(max_length=100)
    confirmed = models.BooleanField(default="No")
    deliverer_employe_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    course_type_no = models.ForeignKey(CourseType, on_delete=models.CASCADE)

    class Meta:
        ordering = ['course_no']
        verbose_name_plural = 'Course'

#model for the course fee
class CourseFee(models.Model):
    course_fee_no = models.BigAutoField(primary_key=True)
    fee_description = models.TextField(max_length=500)
    fee = models.IntegerField()
    course_no = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['course_fee_no']
        verbose_name_plural = 'CourseFee'

#model for the Location
class Location(models.Model):
    location_no = models.BigAutoField(primary_key=True)
    location_name = models.CharField(max_length= 50, blank=False)
    max_size = models.IntegerField(max_length=8, blank=False)

    class Meta:
        ordering = ['location_no']
        verbose_name_plural = 'Location'

#model for the Booking
class Booking(models.Model):
    booking_no = models.BigAutoField(primary_key=True)
    booking_date = models.DateField(auto_now_add=True)
    location_no = models.ForeignKey(Location, on_delete=models.CASCADE)
    course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
    booking_employee_no = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        ordering = ['booking_no']
        verbose_name_plural = 'Booking'

#model for the invoice
class Invoice(models.Model):
    invoice_no = models.BigAutoField(primary_key=True)
    date_raised = models.DateField()
    date_paid = models.IntegerField()
    credit_card_no = models.IntegerField(max_length=12)
    holders_name = models.CharField(max_length=100)
    expiry_date = models.DateField()
    resgistration_no = models.IntegerField()
    p_method_no = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    class Meta:
        ordering = ['invoice_no']
        verbose_name_plural = 'Invoice'

#model for the registration
class Registration(models.Model):
    registration_no = models.BigAutoField(primary_key=True)
    registration_date = models.DateField()
    delegate_no = models.IntegerField()
    course_fee_no = models.ForeignKey(CourseFee, on_delete=models.CASCADE)
    register_employee_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    course_no = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['registration_no']
        verbose_name_plural = 'Registration'
