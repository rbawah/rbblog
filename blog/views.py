from django.shortcuts import render
from blog.models import Post, Topic, Category
from django.views import View
from django.contrib.humanize.templatetags.humanize import naturaltime
from blog.utils import dump_queries
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


class PostListView(View):
    template_name = "blog/list_copy.html"
    #paginate_by = 5

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval)
            query.add(Q(text__icontains=strval), Q.OR)
            post_list = Post.objects.filter(query).prefetch_related('category').order_by('id')#[:10]
        else :
            post_list = Post.objects.all().order_by('id')#[:10]

        # Augment the post_list

        paginator = Paginator(post_list, 5)  # Show 5 posts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        ctx = {'page_obj': page_obj, 'search': strval}
        return render(request, self.template_name, ctx)

class TutsListView(View):
    template_name = "blog/tuts_detail_list.html"

    def get(self, request, slug):
        topic = Topic.objects.get(slug=slug)
        post_list1 = Post.objects.filter(
            category__name='Tutorial'
        ).filter(
            topics__slug=slug
        ).order_by(
            'published_date')

        post_list = Post.objects.prefetch_related('topics')

        paginator = Paginator(post_list, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        ctx = {'page_obj': page_obj, 'topic': topic,}
        return render(request, self.template_name, ctx)


def get_posts_by_topic(request, slug):
    posts = Post.objects.filter(topics__slug=slug).order_by('published_date')
    topic = Topic.objects.get(slug=slug)
    #topic = get_object_or_404(Topic, slug=slug)

    return render(request, 'blog/topic_articles.html', {
        "posts": posts,
        "topic":topic,
    })


def get_posts_by_category(request, slug):
    cat_posts = Post.objects.filter(category__slug=slug).order_by('published_date') #filter post based on Category (Blog or Tutorial)
    category = Category.objects.get(slug=slug)
    return render(request, 'blog/category_articles.html', {

        "cat_posts": cat_posts,
        "category": category
    })


'''
class TopicListView(generic.ListView):
    model = Topic
    #template_name ='blog/topic_list.html'
    template_name ='blog/side_bar.html'

    def get_queryset(self):
        return Topic.objects.all()'''