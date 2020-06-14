from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views import View

from django.db.models import Q
import markdown

from .models import Article,ArticleColumn
from .forms import ArticleForm
from comment.models import ArticleComment
from comment.forms import ArticleCommentForm
from Usergroup.models import Usergroup

# 帖子列表
def showArticle(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    tag = request.GET.get('tag')

    if search:
        article_list = Article.objects.all()
        if order == 'total_views':
            article_list = article_list.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search) |
                Q(column__title__icontains=search) |
                Q(tags__name__icontains=search)
            ).order_by('-total_views')
        else:
            article_list = article_list.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search) |
                Q(column__title__icontains=search)|
                Q(tags__name__icontains=search)
            )
    else:
        search = ''
        if order == 'total_views':
            article_list = Article.objects.all().order_by('-total_views')
        else:
            article_list = Article.objects.all()

    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    all_count = Article.objects.all().count()

    context = {
        'all_count':all_count,
        'articles': articles,
        'order': order,
        'search': search ,
        'article_list':article_list ,
        'colum':column ,
        'tag':tag
    }
    return render(request, 'Articles/showArticles.html', context)

# 帖子内容
def ArticleDetail(request,id):
    article = Article.objects.get(id=id)
    comments = ArticleComment.objects.filter(article=id)
    comment_form = ArticleCommentForm()
    article.body = markdown.markdown(
        article.body,
        extensions=[
            'markdown.extensions.extra',# 包含 缩写、表格等常用扩展
            'markdown.extensions.codehilite',# 语法高亮扩展
        ]
    )

    if request.user.id != article.author.id:
        article.total_views += 1
        article.save(update_fields=['total_views'])

    context = {'article':article,'comments':comments,'comment_form':comment_form}
    return render(request, 'Articles/ArticleDetail.html', context)

# 写帖子
def ArticleCreate(request):
    if request.method == "POST":
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
            new_article.save()
            article_form.save_m2m()
            return redirect("ArticleDetail",id=new_article.id)
        else:
            return HttpResponse("<script>alert('帖子生成错误');location.href=\"\";</script>")
    else:
        article_form = ArticleForm()
        columns = ArticleColumn.objects.all()
        context = {'article_form':article_form,'columns':columns}
        return render(request,'Articles/upload.html',context)

# 删帖
@login_required
def ArticleDelete(request,id):
    article = Article.objects.get(id=id)
    # 仅允许管理员和发帖人删除
    if request.user.id == article.author_id or request.user.is_superuser:
        article.delete()
        return redirect('showArticle')
    else:
        return redirect('ArticleDetail', id)

# 小组删帖
@login_required
def GroupPostDelete(request,gid,id):
    group = Usergroup.objects.get(id=gid)
    article = Article.objects.get(id=id)

    if article == group.top_article:
        group.top_article = None
        group.save()
        article.delete()
        return redirect('Usergroup:Groupdetail',gid)
    else:
        article.delete()
        return redirect('Usergroup:Groupdetail',gid)

# 改帖
@login_required
def ArticleUpdate(request,id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            if request.POST['column'] != 'none':
                article.column = ArticleColumn.objects.get(id=request.POST['column'])
            else:
                article.column = None
            article.save()
            return redirect("ArticleDetail",id=id)
        else:
            return HttpResponse("修改时出现了错误")
    else:
        article_form = ArticleForm()
        columns = ArticleColumn.objects.all()
        context = {'article':article, 'article_form':article_form,'columns':columns}
        return render(request, 'Articles/update.html', context)

# 点赞数变化
class IncreaseLikesView(View):
    def post(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs.get('id'))
        article.likes += 1
        article.save()
        return HttpResponse('success')





