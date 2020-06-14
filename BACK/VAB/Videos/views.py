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
from .models import Video,VideoColumn
from .forms import VideoForm
from comment.models import VideoComment
from comment.forms import VideoCommentForm

# 引入Q对象（查找）
from django.db.models import Q

# 展示影视
def showVideo(request):
    search = request.GET.get('search')
    column = request.GET.get('column')
    tag = request.GET.get('tag')

    Video_list = Video.objects.all()

    videocolumn = VideoColumn.objects.filter(title__exact=search).first()

    if search:
        if videocolumn:
            Video_list = Video_list.filter(
                Q(Video_Country__contains=search) |
                Q(Video_intro__contains=search) |
                Q(Video_name__contains=search) |
                Q(Video_column=videocolumn)
            )
        else:
            Video_list = Video_list.filter(
                Q(Video_Country__contains=search) |
                Q(Video_intro__contains=search) |
                Q(Video_name__contains=search)
            )
    else:
        search = ''

    if column is not None and column.isdigit():
        Video_list = Video_list.filter(column=column)

    if tag and tag != 'None':
        Video_list = Video_list.filter(Video_tags__in=[tag])

    # 每一页展示5部影视
    paginator = Paginator(Video_list, 5)
    page = request.GET.get('page')
    videos = paginator.get_page(page)
    all_count = Video.objects.all().count()
    context = {'videos': videos,
               'all_count': all_count,
               'search':search,
               'column':column,
               'tag':tag
               }
    return render(request, 'Videos/showVideos.html', context)


def Videodetail(request, id):
    a_video = Video.objects.get(pk=id)
    comments = VideoComment.objects.filter(video=id)
    comment_form = VideoCommentForm()

    context = {'a_video': a_video, 'comments':comments, 'comment_form':comment_form}
    return render(request, 'Videos/Videodetail.html', context)


# 上传影视信息
@method_decorator(login_required, name='post')
class Videoupdload(View):
    form_class = VideoForm
    initial = {}
    template_name = 'Videos/upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        columns = VideoColumn.objects.all()
        return render(request, self.template_name, {'form': form, 'columns':columns})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            video_name = form.cleaned_data['Video_name']
            video_country = form.cleaned_data['Video_Country']
            video_intro = form.cleaned_data['Video_intro']
            video_column = form.cleaned_data['Video_column']
            video_tags = form.cleaned_data['Video_tags']
            video_img = request.FILES.get('Video_img')
            video = Video.objects.create(Video_name=video_name,
                                         Video_Country=video_country,
                                         Video_intro=video_intro,
                                         Video_img=video_img,
                                         Video_column=video_column)
            video.Video_tags.set(*request.POST.get('Video_tags').split(','),clear=True)
            return redirect("Videodetail", id=video.id)
        else:
            print("error!")
        return render(request, self.template_name, {'form': form})







