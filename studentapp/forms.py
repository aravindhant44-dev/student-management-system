from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    dob = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    YEAR_CHOICES = [
        ('', 'Select Year'),
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    ]

    DEPARTMENT_CHOICES = [
        ('', 'Select Department'),
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('MECH', 'MECH'),
        ('CIVIL', 'CIVIL'),
        ('IT', 'IT'),
    ]

    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model  = Student
        fields = [
            'student_id',
            'name',
            'dob',
            'email',
            'phonenumber',
            'department',
            'year',
            'cgpa'
        ]                        
        widgets = {
            'student_id': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'Enter Student ID'
            }),
            'name': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'Enter Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class':       'form-control',
                'placeholder': 'Enter Email'
            }),
            'phonenumber': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'Enter Phone Number',
                'maxlength':   '10'
            }),
            'cgpa': forms.NumberInput(attrs={
                'class':       'form-control',
                'min':         '0',
                'max':         '10',
                'step':        '0.01',
                'placeholder': 'Enter CGPA (0-10)'
            }),
        }

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if not student_id.isdigit():
            raise forms.ValidationError(
                'Student ID must be numbers only!')
        if len(student_id) != 12:
            raise forms.ValidationError(
                'Student ID must be 12 digits!')
        qs = Student.objects.filter(student_id=student_id)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                'Student ID already exists!')
        return student_id

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Student.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                'Email already exists!')
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError(
                'Name must not contain numbers!')
        if len(name) < 3:
            raise forms.ValidationError(
                'Name must be at least 3 characters!')
        return name

    def clean_cgpa(self):
        cgpa = self.cleaned_data.get('cgpa')
        if cgpa < 0 or cgpa > 10:
            raise forms.ValidationError(
                'CGPA must be between 0 and 10!')
        return cgpa