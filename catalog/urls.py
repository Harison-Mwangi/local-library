from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),    
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('books/', views.BookListView.as_view(), name='books'),
 
    path('borrowed/', views.LoanedBooksListView.as_view(), name='all-borrowed'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]