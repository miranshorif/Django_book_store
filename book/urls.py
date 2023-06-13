from django.urls import path
# from book.views import home,store_book,show_books,edit_book,delete_book
from . import views
urlpatterns = [
    path('<int:roll>/',views.MyTemplateView.as_view(),{'author': 'rahim'},name = 'homepage'),
    # path('store_new_book/',views.store_book,name='store_book'),
    path('store_new_book/',views.BookFormView.as_view(),name='store_book'),
    # path('show_books/',views.show_books,name='show_books'),
    path('show_books/',views.BookListView.as_view(),name='show_books'),
    # path('edit_book/<int:id>',views.edit_book,name='edit_book'),
    path('edit_book/<int:pk>',views.BookUpdate.as_view(),name='edit_book'),
    path('bookdetail/<int:id>',views.BookDetails.as_view(),name='bookdetail'),
    # path('delete_book/<int:id>',views.delete_book,name='delete_book'),
    path('delete_book/<int:pk>',views.DeleteBookView.as_view(),name='delete_book'),
]