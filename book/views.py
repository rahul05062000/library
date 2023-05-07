
from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from django.http import HttpResponseBadRequest
from .models import Book
from django.core.paginator import Paginator


def home(request):
    return render(request,'home.html')


def add_data(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        publisher = request.POST['publisher']
        publication_date = request.POST['publication_date']
        isbn = request.POST['isbn']
        category = request.POST['category']

        if not title:
            return HttpResponseBadRequest("Title is required")
        if not author:
            return HttpResponseBadRequest("Author is required")
        if not publisher:
            return HttpResponseBadRequest("Publisher is required")
        if not publication_date:
            return HttpResponseBadRequest("Publication date is required")
        if not isbn:
            return HttpResponseBadRequest("ISBN is required")
        if not category:
            return HttpResponseBadRequest("Category is required")

        book = Book(title=title, author=author, publisher=publisher, publication_date=publication_date, isbn=isbn, category=category)
        book.save()
        return render(request, 'home.html')
    else:
        return render(request, 'add_book.html')

    
# def show_data(request):
#     tdata=Book.objects.all()
#     return render(request,'show.html',{'book_list':tdata})

def show_data(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 2) # Show 25 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'show.html', {'page_obj': page_obj})

def delete(request):
    isbn= request.GET['id']
    Book.objects.filter(isbn=isbn).delete()
    return HttpResponseRedirect("show")



def edit(request):
    isbn = request.GET['id']
    publisher = author = "Not Available"
    for data in Book.objects.filter(isbn=isbn):
        publisher = data.publisher
        author = data.author
    return render(request,"edit.html",{'isbn':isbn,'publisher':publisher,'author':author})

def RecordEdited(request):
    if request.method == 'POST':
        isbn = request.POST['isbn']
        publisher = request.POST['publisher']
        author = request.POST['author']
        Book.objects.filter(isbn=isbn).update(publisher=publisher,author=author)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")


def search_book(request):
    name = request.GET.get('q')
    book_list = Book.objects.filter(author=name)
    paginator = Paginator(book_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'show.html', {'page_obj': page_obj})




    