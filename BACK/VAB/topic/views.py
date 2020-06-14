from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views import View

from django.db.models import Q

from .models import Topic
from .forms import TopicForm
from article.models import Article,ArticleColumn

# 新建一个话题
def createTopic(request):
    if request.method == "POST":
        topic_form = TopicForm(data=request.POST)
        if topic_form.is_valid():
            topic = topic_form.cleaned_data['topic']
            body = topic_form.cleaned_data['body']
            topicimg = request.FILES.get('topicimg')

            new_topic = Topic.objects.create(topic=topic,topicimg=topicimg,body=body)
            new_Articlecolumn = ArticleColumn.objects.create(title=topic)

            new_topic.save()
            new_Articlecolumn.save()

            return redirect('topic:TopicDetail',id=new_topic.id)
        else:
            return HttpResponse("wrong")
    else:
        topic_form = TopicForm()
        context = {'topic_form':topic_form}
        return render(request,'topic/makeAtopic.html',context)

# 所有话题
def alltopics(request):
    search = request.GET.get('search')
    alltopics = Topic.objects.all()

    if search:
        alltopics = alltopics.filter(Q(topic__icontains=search))
    else:
        search = ''

    paginator = Paginator(alltopics, 5)
    page = request.GET.get('page')
    topics = paginator.get_page(page)
    all_count = alltopics.count()

    context = {
        'alltopics':alltopics,
        'topics':topics,
        'all_count':all_count,
        'search':search
    }

    return render(request, 'topic/allTopics.html', context)



# 查看详情
def topicDetail(request,id):
    topic = Topic.objects.get(id=id)

    # flag = Article.objects.filter(column=topic.topic).exists()
    # allRelateArticles = Article.objects.all()

    column = ArticleColumn.objects.filter(title=topic.topic).first()

    if column:
        allRelateArticles = Article.objects.filter(column=column)
        topic.allcount = allRelateArticles.count()
        topic.save()
        search = request.GET.get('search')

        if search:
            allRelateArticles = allRelateArticles.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )
        else:
            search = ''

    else:
        allRelateArticles = None
        search = ''

    paginator = Paginator(allRelateArticles, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    all_count = allRelateArticles.count()

    context = {
        'all_count':all_count,
        'articles':articles,
        'topic':topic,
        'allRelateArticles':allRelateArticles
    }

    return render(request, 'topic/topicdetail.html', context)