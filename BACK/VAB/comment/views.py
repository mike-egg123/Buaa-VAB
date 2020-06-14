from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from Books.models import Book
from Videos.models import Video
from article.models import Article
from notifications.signals import notify
from .forms import BookCommentForm,ArticleCommentForm,VideoCommentForm
from .models import ArticleComment,VideoComment,BookComment

@login_required
def post_Bookcomment(request,id):
    book = get_object_or_404(Book,id=id)

    if request.method == 'POST':
        comment_form = BookCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.book = book
            new_comment.save()
            return redirect("Bookdetail",id=book.id)
        else:
            return HttpResponse("<script>alert('填写错误，请重试');")
    else:
        return HttpResponse("<script>alert('请求无效');</script>")

@login_required
def post_Videocomment(request,id):
    video = get_object_or_404(Video,id=id)

    if request.method == 'POST':
        comment_form = VideoCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.video = video
            new_comment.save()
            return redirect("Videodetail",id=video.id)
        else:
            return HttpResponse("<script>alert('填写错误，请重试');</script>")
    else:
        return HttpResponse("<script>alert('请求无效');</script>")

@login_required
def post_Articlecomment(request,article_id,parent_comment_id=None):
    article = get_object_or_404(Article,id=article_id)

    if request.method == 'POST':
        comment_form = ArticleCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.article = article

            # 二级回复
            if parent_comment_id:
                parent_comment = ArticleComment.objects.get(id=parent_comment_id)
                new_comment.parent_id = parent_comment.get_root().id
                new_comment.reply_to = parent_comment.user
                new_comment.save()

                # 回复通知
                if not parent_comment.user.is_superuser:
                    notify.send(
                        request.user,
                        recipient=parent_comment.user,
                        verb='回复了你',
                        target=article,
                        action_object=new_comment,
                    )
                    print(article.__class__)
                return HttpResponse('200 OK')

            new_comment.save()

            if not request.user.is_superuser:
                notify.send(
                    request.user,
                    recipient=User.objects.filter(is_superuser=1),
                    verb='回复了你',
                    target=article,
                    action_object=new_comment,
                )
            return redirect("ArticleDetail",id=article.id)
        else:
            return HttpResponse("<script>alert('填写错误，请重试');</script>")
    elif request.method == 'GET':
        comment_form = ArticleCommentForm
        context = {
            'comment_form':comment_form,
            'article_id':article_id,
            'parent_comment_id':parent_comment_id
        }
        return render(request,'Comment/reply.html',context)
    else:
        return HttpResponse("<script>alert('请求无效');</script>")

# 删除评论
@login_required
def delete_Bookcomment(request,id):
    bookcomment = BookComment.objects.get(id=id)
    book = bookcomment.book
    if request.user.id == bookcomment.user.id or request.user.is_superuser:
        bookcomment.delete()
        return redirect("Bookdetail",book.id)

@login_required
def delete_Videocomment(request,id):
    videocomment = VideoComment.objects.get(id=id)
    video = videocomment.video
    if request.user.id == videocomment.user.id or request.user.is_superuser:
        videocomment.delete()
        return redirect("Videodetail",video.id)

@login_required
def delete_Articlecomment(request,id):
    articlecomment = ArticleComment.objects.get(id=id)
    if request.user.id == articlecomment.user.id or request.user.is_superuser:
        articlecomment.canbeseen = False
        articlecomment.save()
        article = articlecomment.article
        return redirect("ArticleDetail",article.id)

# 点赞评论/踩评论
@login_required
def like_Bookcomment(request,id):
    bookcomment = BookComment.objects.get(id=id)
    book = bookcomment.book
    bookcomment.likes += 1
    bookcomment.save()
    return redirect("Bookdetail",book.id)

@login_required
def like_Videocomment(request,id):
    videocomment = VideoComment.objects.get(id=id)
    video = videocomment.video
    videocomment.likes += 1
    videocomment.save()
    return redirect("Videodetail",video.id)

@login_required
def like_Articlecomment(request,id):
    articlecomment = ArticleComment.objects.get(id=id)
    article = articlecomment.article
    articlecomment.likes += 1
    articlecomment.save()
    return redirect("ArticleDetail",article.id)

@login_required
def unlike_Bookcomment(request,id):
    bookcomment = BookComment.objects.get(id=id)
    book = bookcomment.book
    bookcomment.hates += 1
    bookcomment.save()
    return redirect("Bookdetail",book.id)

@login_required
def unlike_Videocomment(request,id):
    videocomment = VideoComment.objects.get(id=id)
    video = videocomment.video
    videocomment.hates += 1
    videocomment.save()
    return redirect("Videodetail",video.id)

@login_required
def unlike_Articlecomment(request,id):
    articlecomment = ArticleComment.objects.get(id=id)
    article = articlecomment.article
    articlecomment.hates += 1
    articlecomment.save()
    return redirect("ArticleDetail",article.id)