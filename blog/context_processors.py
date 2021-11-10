from blog.models import Post, Topic, Category


def render_sidebar(request):
    ''' Returns necessary information for sidebar
    '''
    posts = Post.objects.all()[:10]
    topics = Topic.objects.all()
    categories = Category.objects.all()

    return {
        'topics': topics,
        'categories': categories,
        'posts': posts,

    }