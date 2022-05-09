# Generated by Django 4.0.4 on 2022-05-09 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.TextField(blank=True, max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('max_delegate', models.IntegerField(max_length=100)),
                ('confirmed', models.BooleanField(default='No')),
            ],
            options={
                'verbose_name_plural': 'Course',
                'ordering': ['course_no'],
            },
        ),
        migrations.CreateModel(
            name='CourseFee',
            fields=[
                ('course_fee_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('fee_description', models.TextField(max_length=500)),
                ('fee', models.IntegerField()),
                ('course_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
            options={
                'verbose_name_plural': 'CourseFee',
                'ordering': ['course_fee_no'],
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('course_type_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_type_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'CourseType',
                'ordering': ['course_type_no'],
            },
        ),
        migrations.CreateModel(
            name='Delegate',
            fields=[
                ('delegateNo', models.BigAutoField(primary_key=True, serialize=False)),
                ('delegateTitle', models.CharField(max_length=50)),
                ('delegateFName', models.CharField(max_length=100)),
                ('delegateLName', models.CharField(max_length=100)),
                ('delegateStreet', models.TextField(blank=True, max_length=100)),
                ('delegateCity', models.CharField(blank=True, max_length=100)),
                ('delegateState', models.CharField(blank=True, max_length=100)),
                ('delegateZipCode', models.CharField(blank=True, max_length=100)),
                ('attTelNo', models.IntegerField(max_length=10)),
                ('attFaxNo', models.IntegerField(max_length=10)),
                ('attEmailAddress', models.CharField(blank=True, max_length=100)),
                ('clientNo', models.IntegerField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Delegate',
                'ordering': ['delegateNo'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('employee_fname', models.CharField(max_length=100)),
                ('employee_lname', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Employee',
                'ordering': ['employee_no'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=50)),
                ('max_size', models.IntegerField(max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Location',
                'ordering': ['location_no'],
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('payment_method_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('payment_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'PaymentMethod',
                'ordering': ['payment_method_no'],
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('registration_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('registration_date', models.DateField()),
                ('delegate_no', models.IntegerField()),
                ('course_fee_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coursefee')),
                ('course_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('register_employee_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
            options={
                'verbose_name_plural': 'Registration',
                'ordering': ['registration_no'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_raised', models.DateField()),
                ('date_paid', models.IntegerField()),
                ('credit_card_no', models.IntegerField(max_length=12)),
                ('holders_name', models.CharField(max_length=100)),
                ('expiry_date', models.DateField()),
                ('resgistration_no', models.IntegerField()),
                ('p_method_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.paymentmethod')),
            ],
            options={
                'verbose_name_plural': 'Invoice',
                'ordering': ['invoice_no'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='course_type_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coursetype'),
        ),
        migrations.AddField(
            model_name='course',
            name='deliverer_employe_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_employee_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
                ('course_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('location_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location')),
            ],
            options={
                'verbose_name_plural': 'Booking',
                'ordering': ['booking_no'],
            },
        ),
    ]
