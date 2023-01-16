from django.urls import path
from library import views

urlpatterns = [
    path("", views.avb_books, name="books"),
    path('customers/', views.avb_customers, name='customers'),
    path('cust_detail/', views.cust_detail, name='cust_detail'),
    path('book_detail/', views.book_detail, name='book_detail'),
    path('add_cust/', views.add_cust, name='add_cust'),
    path('new-c/', views.new_c, name='new-c'),
    path('add_book/', views.add_book, name='add_book'),
    path('new-b/', views.new_b, name='new-b'),
    path('loans/', views.avb_loans, name='loans'),
    path('loan_detail/', views.loan_detail, name='loan_detail'),
    path('add_loan/', views.add_loan, name='add_loan'),
    path('new-l/', views.new_l, name='new-l'),

]