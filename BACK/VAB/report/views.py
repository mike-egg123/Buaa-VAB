from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponseRedirect

# 方法装饰器
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User

# 导入所需要的模型
from comment.models import BookComment,VideoComment,ArticleComment
from Books.models import Book
from article.models import Article
from Videos.models import Video

from .models import VideoCommentReport,BookCommentReport,ArticleCommentReport
from .form import BookCommentReportForm,VideoCommentReportForm,ArticleCommentReportForm

# 发起举报
def RBookComment(request,id):
    if request.method == "POST":
        reportbookcomment_form = BookCommentReportForm(data=request.POST)
        if reportbookcomment_form.is_valid():
            reason = reportbookcomment_form.cleaned_data['reason']
            aBookreport = BookCommentReport.objects.create(
                reporter=request.user,
                Administrator=User.objects.filter(is_superuser=1).first(),
                bookcomment=BookComment.objects.get(id=id),
                reason=reason
            )
            return redirect("Bookdetail",id=BookComment.objects.get(id=id).book.id)
        else:
            return HttpResponse("举报生成错误")
    else:
        bookcomment = BookComment.objects.get(id=id)
        reportform = BookCommentReportForm()
        context = {'reportform':reportform,'comment':bookcomment}
        return render(request,'report/bookreport.html',context)

def RVideoComment(request,id):
    if request.method == "POST":
        reportvideocomment_form = VideoCommentReportForm(data=request.POST)
        if reportvideocomment_form.is_valid():
            reason = reportvideocomment_form.cleaned_data['reason']
            aVideoreport = VideoCommentReport.objects.create(
                reporter=request.user,
                Administrator=User.objects.filter(is_superuser=1).first(),
                videocomment=VideoComment.objects.get(id=id),
                reason=reason
            )
            return redirect("Videodetail",id=VideoComment.objects.get(id=id).video.id)
        else:
            return HttpResponse("举报生成错误")
    else:
        videocomment = VideoComment.objects.get(id=id)
        reportform = VideoCommentReportForm()
        context = {'reportform': reportform,'comment':videocomment}
        return render(request, 'report/videoreport.html', context)

def RArticleComment(request,id):
    if request.method == "POST":
        reportarticlecomment_form = ArticleCommentReportForm(data=request.POST)

        if reportarticlecomment_form.is_valid():
            reason = reportarticlecomment_form.cleaned_data['reason']
            article = ArticleComment.objects.get(id=id).article
            aArticlereport = ArticleCommentReport.objects.create(
                reporter=request.user,
                Administrator=User.objects.filter(is_superuser=1).first(),
                articlecomment=ArticleComment.objects.get(id=id),
                reason=reason
            )
            return redirect("ArticleDetail",id=article.id)
        else:
            return HttpResponse("举报生成错误")
    else:
        articlecomment = ArticleComment.objects.get(id=id)
        reportform = ArticleCommentReportForm()
        context = {'reportform': reportform,'comment':articlecomment}
        return render(request, 'report/articlereport.html', context)

def LookAllMyReport(request):
    allBookReport = BookCommentReport.objects.filter(reporter=request.user)
    allVideoReport = VideoCommentReport.objects.filter(reporter=request.user)
    allArticleReport = ArticleCommentReport.objects.filter(reporter=request.user)
    context = {'allBookReport':allBookReport,'allVideoReport':allVideoReport,'allArticleReport':allArticleReport}
    return render(request,'report/allMyreport.html',context)

def needhandleReport(request):
    allBookReport = BookCommentReport.objects.all()
    allVideoReport = VideoCommentReport.objects.all()
    allArticleReport = ArticleCommentReport.objects.all()
    context = {'allBookReport': allBookReport, 'allVideoReport': allVideoReport, 'allArticleReport': allArticleReport}
    return render(request, 'report/handlereport.html',context)

def refusebookreport(request,id):
    bookreport = BookCommentReport.objects.get(id=id)
    bookreport.state = 1
    bookreport.save()
    return redirect('report:needHandle')

def handlebookreport(request,id):
    bookreport = BookCommentReport.objects.get(id=id)
    bookreport.state = 2
    bookreport.save()
    bookcomment = BookComment.objects.get(id=bookreport.bookcomment.id)
    bookcomment.delete()
    return redirect('report:needHandle')

def refusevideoreport(request,id):
    videoreport = VideoCommentReport.objects.get(id=id)
    videoreport.state = 1
    videoreport.save()
    return redirect('report:needHandle')

def handlevideoreport(request,id):
    videoreport = VideoCommentReport.objects.get(id=id)
    videoreport.state = 2
    videoreport.save()
    videocomment = VideoComment.objects.get(id=videoreport.videocomment.id)
    videocomment.delete()
    return redirect('report:needHandle')

def refusearticlereport(request,id):
    articlereport = ArticleCommentReport.objects.get(id=id)
    articlereport.state = 1
    articlereport.save()
    return redirect('report:needHandle')

def handlearticlereport(request,id):
    articlereport = ArticleCommentReport.objects.get(id=id)
    articlereport.state = 2
    articlereport.save()
    articlecomment = ArticleComment.objects.get(id=articlereport.articlecomment.id)
    articlecomment.canbeseen = False
    articlecomment.save()
    return redirect('report:needHandle')
