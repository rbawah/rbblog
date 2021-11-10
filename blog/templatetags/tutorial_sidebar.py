from django import template
from blog.models import Post, Topic, Category

register = template.Library()

'''
@register.inclusion_tag('blog/sidebar_tutorial_topic.html')
def get_topic_sidebar(slug):
    #slug = kwargs['slug']
    topic1 = Topic.objects.get(slug=slug)
    post_list1 = Post.objects.filter(
        category__name='Tutorial'
    ).filter(
        topics__name=topic1
    ).order_by(
        'published_date')


    return {
        'topic1': topic1,
        'post_list1': post_list1,
    }
'''