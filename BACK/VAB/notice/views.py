from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import Article
from Books.models import Book

class CommentNoticeListView(LoginRequiredMixin, ListView):
    context_object_name = 'notices'
    template_name = 'notice/list.html'
    login_url = '/login/'

    # 未读通知的查询集
    def get_queryset(self):
        return self.request.user.notifications.unread()


class CommentNoticeUpdateView(View):
    def get(self, request):
        notice_id = request.GET.get('notice_id')
        if notice_id:
            if request.GET.get('article_id'):
                article = Article.objects.get(id=request.GET.get('article_id'))
                request.user.notifications.get(id=notice_id).mark_as_read()
                return redirect('ArticleDetail', id=article.id)
            elif request.GET.get('book_id'):
                book = Book.objects.get(id=request.GET.get('book_id'))
                request.user.notifications.get(id=notice_id).mark_as_read()
                return redirect('Bookdetail', id=book.id)
        # 更新全部通知
        else:
            request.user.notifications.mark_all_as_read()
            print(1)
            return redirect('notice:list')