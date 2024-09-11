from django.views.generic import ListView,UpdateView,CreateView,DeleteView,DetailView,TemplateView
from .models import Book,Member,Loan,BookInstance
from django.urls import reverse_lazy
from .forms import BookForm,MemberForm,LoanForm,BookInstanceForm,UserCreationForm
from django.shortcuts import render, redirect,get_object_or_404


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = context['books']
        
        # Prepare a list with book instances and their availability counts
        book_availability = []
        for book in books:
            available_copies = book.bookinstance_set.filter(status='available').count()
            book_availability.append({
                'book': book,
                'available_copies': available_copies
            })
        
        context['book_availability'] = book_availability
        return context




class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html' 
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm  
    template_name = 'books/book_form.html'  
    success_url = reverse_lazy('book-list') 

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_update.html' 
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'  
    success_url = reverse_lazy('book-list') 

class MemberListView(ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'

class MemberDetailView(DetailView):
    model = Member
    template_name = 'members/member_detail.html'
    context_object_name = 'member'

class MemberCreateView(CreateView):
    template_name = 'members/member_form.html'
    
    def get(self, request, *args, **kwargs):
        user_form = UserCreationForm()
        member_form = MemberForm()
        return self.render_to_response({'user_form': user_form, 'member_form': member_form})

    def post(self, request, *args, **kwargs):
        user_form = UserCreationForm(request.POST)
        member_form = MemberForm(request.POST)

        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            print(user)
            member = member_form.save(commit=False)
            member.user = user
            member.save()
            return redirect('member-list')

        return self.render_to_response({'user_form': user_form, 'member_form': member_form})

class MemberUpdateView(UpdateView):
    template_name = 'members/member_form.html'

    def get(self, request, *args, **kwargs):
        member = get_object_or_404(Member, pk=kwargs['pk'])
        user_form = UserCreationForm(instance=member.user)
        member_form = MemberForm(instance=member)
        return self.render_to_response({'user_form': user_form, 'member_form': member_form})

    def post(self, request, *args, **kwargs):
        member = get_object_or_404(Member, pk=kwargs['pk'])
        user_form = UserCreationForm(request.POST, instance=member.user)
        member_form = MemberForm(request.POST, instance=member)

        if user_form.is_valid() and member_form.is_valid():
            user_form.save()
            member_form.save()
            return redirect('member-list')

        return self.render_to_response({'user_form': user_form, 'member_form': member_form})

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'members/member_confirm_delete.html'
    success_url = reverse_lazy('member-list')

class LoanListView(ListView):
    model = Loan
    template_name = 'loans/loan_list.html'
    context_object_name = 'loans'

class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    template_name = 'loans/loan_form.html'
    success_url = reverse_lazy('loan-list')

    def form_valid(self, form):
        # Call the base form_valid method to save the loan instance
        response = super().form_valid(form)

        # Get the book instance associated with the loan
        book_instance = form.cleaned_data['book_instance']
        due_back = form.cleaned_data['due_date']

        # Update the status of the book instance
        book_instance.status = 'on_loan'  # Update this status based on your needs
        book_instance.due_back = due_back  # Update this date based on your needs
        book_instance.save()

        return response


class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = 'loans/loan_form.html'
    success_url = reverse_lazy('loan-list')

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'loans/loan_confirm_delete.html'
    success_url = reverse_lazy('loan-list')

class LoanDetailView(DetailView):
    model = Loan
    template_name = 'loans/loan_detail.html'
    context_object_name = 'loan'

class BookInstanceListView(ListView):
    model = BookInstance
    template_name = 'book_instance/bookinstance_list.html'  
    context_object_name = 'bookinstances' 

class BookInstanceDetailView(DetailView):
    model = BookInstance
    template_name = 'book_instance/bookinstance_detail.html'
    context_object_name = 'bookinstance'

class BookInstanceCreateView(CreateView):
    model = BookInstance
    template_name = 'book_instance/bookinstance_form.html'
    fields = ['book', 'unique_id', 'status', 'due_back']  
    success_url = reverse_lazy('bookinstance-list') 

class BookInstanceUpdateView(UpdateView):
    model = BookInstance
    template_name = 'book_instance/bookinstance_form.html'
    fields = ['book', 'unique_id', 'status', 'due_back']
    success_url = reverse_lazy('bookinstance-list')

class BookInstanceDeleteView(DeleteView):
    model = BookInstance
    template_name = 'book_instance/bookinstance_confirm_delete.html'
    success_url = reverse_lazy('bookinstance-list')

from django.views.generic import TemplateView
from .models import Book, BookInstance

class DashboardView(TemplateView):
    template_name = 'dash_board.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = Book.objects.count()
        context['total_instances'] = BookInstance.objects.count()
        context['available_instances'] = BookInstance.objects.filter(status='available').count()
        context['on_loan_instances'] = BookInstance.objects.filter(status='on_loan').count()

        context['available_books'] = BookInstance.objects.filter(status='available')
        context['on_loan_books'] = BookInstance.objects.filter(status='on_loan')

        return context

