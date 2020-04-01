from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# 展示图书
def showBook(request):
    Book_list = Book.objects.all()
    return render(request, 'Books/showBooks.html', {'Book_list':Book_list})

def Bookdetail(request, id):
    a_book = Book.objects.get(pk=id)
    return render(request, 'Books/Bookdetail.html', {'a_book':a_book})

@login_required
def Bookupload(request):
    if request.method == 'POST':
        newbook_form = BookForm(request.POST,request.FILES)
        if newbook_form.is_valid():
            book_name = newbook_form.cleaned_data['Book_name']
            book_auth = newbook_form.cleaned_data['Book_auth']
            book_intro = newbook_form.cleaned_data['Book_intro']
            # book_img = newbook_form.cleaned_data['Book_img']
            book_img = request.FILES.get('Book_img')
            book = Book.objects.create(Book_name=book_name,
                                       Book_auth=book_auth,
                                       Book_intro=book_intro,
                                       Book_img=book_img)
            return redirect("Bookdetail",id=book.id)
        else:
            return HttpResponse('forms error!')
    else:
        Book_form = BookForm()
        return render(request, 'Books/upload.html')