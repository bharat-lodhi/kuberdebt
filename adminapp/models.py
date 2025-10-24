from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class LoanConsultation(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    total_loan_amount = models.CharField(max_length=100, blank=True, null=True)
    LOAN_TYPE_CHOICES = [
        ('secured', 'Secured Loan'),
        ('unsecured', 'Unsecured Loan'),
        ('both', 'Both Secured & Unsecured'),
    ]
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPE_CHOICES, blank=True, null=True)
    LEGAL_NOTICE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    legal_notice = models.CharField(max_length=3, choices=LEGAL_NOTICE_CHOICES)
    preferred_timing = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    problem_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"
