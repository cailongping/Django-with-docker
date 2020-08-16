from django.shortcuts import render,HttpResponse
from .models import Course
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from . import tasks

# Create your views here.
def index(request):
    r= tasks.mul.apply_async((10, 10))
    print(r.ready()) # 查看任务状态，返回布尔值, 任务执行完成, 返回True, 否则返回 False.
    # print(r.wait())  # 会阻塞等待任务完成, 返回任务执行结果，很少使用；
    # print(r.get()) # 获取任务执行结果，可以设置等待时间，如果超时但任务未完成返回None；timeout=6
    # print(r.result)  # 任务执行结果，未完成返回None；
    # print(r.state)  # PENDING, START, SUCCESS，任务当前的状态
    # print(r.status)  # PENDING, START, SUCCESS，任务当前的状态
    # print(r.successful)  # 任务成功返回true
    # print(r.traceback)  # 如果任务抛出了一个异常，可以获取原始的回溯信息

    return HttpResponse('res: %s' % r.id)

def task_test(request):
    res = tasks.add.delay(228, 24)
    print("start running task")
    # print("async task res:", res.get())

    return HttpResponse('hello world')

def course_search(request):
    """
    搜索课程
    :param request:
    :return:
    """
    form=SearchForm()
    query=None
    results=[]
    if 'query' in request.GET:
        form=SearchForm(request.GET)
        if form.is_valid():
            query=form.cleaned_data['query']
            results=Course.objects.annotate(search=SearchVector('title','overview'),).filter(search=query)
    return render(request, 'news/bs-search.html', {'query':query, 'results':results})
