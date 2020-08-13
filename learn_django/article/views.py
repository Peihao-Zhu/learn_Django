from django.shortcuts import render,get_object_or_404
from  django.http import HttpResponse,Http404
from  .models import Article

# Create your views here.
def aritcle_detail(request,article_id):

    #使用get_object_or_404 传入模型和判断条件，方法内部会进行判断，返回404，自己不用进行异常处理了
    article=get_object_or_404(Article,id=article_id)
    #context是字典对象，传入render有要求
    context={}
    context['article_obj']=article
    return render(request,'article_detail.html',context)

def article_list(request):
    #不是显示所有的文章，而是针对is_deleted进行过滤。
    articles=Article.objects.filter(if_deleted=False)
    context={}
    context['articles']=articles
    return render(request,'article_list.html',context)