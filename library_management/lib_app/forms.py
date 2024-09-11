from django import forms
from .models import Book,Member,Loan,BookInstance
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'author', 'publisher', 'genre', 'language', 'publication_date', 'description', 'available_copies', 'total_copies']

class MemberForm(forms.ModelForm):
    membership_type = forms.ChoiceField(choices=[('regular', 'Regular'), ('premium', 'Premium')], required=True)
    class Meta:
        model = Member
        fields = ['membership_type']
class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, help_text='Required.')
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book_instance','member','due_date','return_date']


class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book','unique_id','status','due_back']
