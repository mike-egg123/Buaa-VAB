# http响应
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponseRedirect

# 用于分页
from django.core.paginator import Paginator

# 方法装饰器
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User

# 类视图
from django.views import View

# 导入
from .models import Book,BookColumn
from .forms import BookForm
from comment.models import BookComment
from comment.forms import BookCommentForm

# 引入Q对象（查找）
from django.db.models import Q

# 展示图书
def showBook(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    tag = request.GET.get('tag')

    bookcolumn = BookColumn.objects.filter(title__exact=search).first()

    Book_list = Book.objects.all()

    if search:
        if bookcolumn:
            Book_list = Book_list.filter(
                Q(Book_auth__contains=search) |
                Q(Book_intro__contains=search) |
                Q(Book_name__contains=search) |
                Q(Book_column=bookcolumn)
            )
        else:
            Book_list = Book_list.filter(
                Q(Book_auth__contains=search) |
                Q(Book_intro__contains=search) |
                Q(Book_name__contains=search)
            )
    else:
        search = ''

    if column is not None and column.isdigit():
        Book_list = Book_list.filter(column=column)

    if tag and tag != 'None':
        Book_list = Book_list.filter(Book_tags__in=[tag])

    if order == 'Book_total_views':
        Book_list = Book_list.order_by('-Book_total_views')

    # 每一页展示5本书
    paginator = Paginator(Book_list, 5)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    all_count = Book.objects.all().count()

    context = {'books': books,
               'order': order,
               'all_count': all_count,
               'search':search,
               'column':column,
               'tag':tag
               }
    return render(request, 'Books/showBooks.html', context)


# TODO:如何解决刷阅读量的问题，一个人是否只能提供一个阅读量
def Bookdetail(request, id):
    a_book = Book.objects.get(pk=id)
    comments = BookComment.objects.filter(book=id)
    comment_form = BookCommentForm()
    a_book.Book_total_views += 1
    a_book.save(update_fields=['Book_total_views'])

    context = {'a_book': a_book, 'comments':comments, 'comment_form':comment_form}
    return render(request, 'Books/Bookdetail.html', context)

# 上传图书信息
@method_decorator(login_required, name='post')
class Bookupdload(View):
    form_class = BookForm
    initial = {}
    template_name = 'Books/upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        columns = BookColumn.objects.all()
        return render(request, self.template_name, {'form': form, 'columns':columns})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            book_name = form.cleaned_data['Book_name']
            book_auth = form.cleaned_data['Book_auth']
            book_intro = form.cleaned_data['Book_intro']
            book_column = form.cleaned_data['Book_column']
            book_tags = form.cleaned_data['Book_tags']
            book_img = request.FILES.get('Book_img')
            book = Book.objects.create(Book_name=book_name,
                                       Book_auth=book_auth,
                                       Book_intro=book_intro,
                                       Book_img=book_img,
                                       Book_column=book_column)
            book.Book_tags.set(*request.POST.get('Book_tags').split(','),clear=True)
            return redirect("Bookdetail", id=book.id)
        else:
            print("error!")
        return render(request, self.template_name, {'form': form})
