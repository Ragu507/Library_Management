from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Member URLs
    path('members/', MemberListView.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('members/create/', MemberCreateView.as_view(), name='member-create'),
    path('members/<int:pk>/update/', MemberUpdateView.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='member-delete'),

    # Loan URLs
    path('loans/', LoanListView.as_view(), name='loan-list'),
    path('loans/create/', LoanCreateView.as_view(), name='loan-create'),
    path('loans/<int:pk>/update/', LoanUpdateView.as_view(), name='loan-update'),
    path('loans/<int:pk>/detail/', LoanDetailView.as_view(), name='loan-detail'),
    path('loans/<int:pk>/delete/', LoanDeleteView.as_view(), name='loan-delete'),

    path('bookinstances/', BookInstanceListView.as_view(), name='bookinstance-list'),
    path('bookinstance/<int:pk>/', BookInstanceDetailView.as_view(), name='bookinstance-detail'),
    path('bookinstance/create/', BookInstanceCreateView.as_view(), name='bookinstance-create'),
    path('bookinstance/<int:pk>/update/', BookInstanceUpdateView.as_view(), name='bookinstance-update'),
    path('bookinstance/<int:pk>/delete/', BookInstanceDeleteView.as_view(), name='bookinstance-delete'),

    path('', DashboardView.as_view(), name='dash_board'),
]
