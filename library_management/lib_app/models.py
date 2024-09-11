from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    available_copies = models.IntegerField(default=1)
    total_copies = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_date = models.DateField(auto_now_add=True)
    membership_type = models.CharField(max_length=50, choices=[('regular', 'Regular'), ('premium', 'Premium')])

    def __str__(self):
        return self.user.username
    
class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=30, unique=True)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('on_loan', 'On Loan')], default='available')
    due_back = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.unique_id} ({self.book.title})'

class Loan(models.Model):
    book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.book_instance.book.title} to {self.member.user.username}'


class Fine(models.Model):
    loan = models.OneToOneField(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Fine for {self.loan.book_instance.book.title} ({self.loan.member.user.username})'

