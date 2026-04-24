from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class Student(models.Model):

    DEPARTMENT_CHOICES = [

        ('CSE','CSE'),
        ('IT', 'IT'),
        ('ECE', 'ECE'),
        ('EEE','EEE'),
        ('CIVIL', 'CIVIL'),
        ('MECH', 'MECH'),
        ('B.COM','B.COM'),
        ('BCA', 'BCA'),
        ('BA.ENG', 'BA.ENG'),
        ('BSC.CHEMISTRY','BSC.CHEMISTRY'),

    ]


    YEAR_CHOICES = [

        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),

    ]


    student_id = models.CharField(max_length=20, unique=True)

    name = models.CharField(max_length=100)

    dob = models.DateField()

    email = models.EmailField(unique=True)


    phonenumber = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='Phone number must be exactly 10 digits'
            )
        ]
    )


    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES
    )


    year = models.CharField(
        max_length=20,
        choices=YEAR_CHOICES
    )


    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )


    def __str__(self):
        return self.name