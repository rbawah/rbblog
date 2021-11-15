from django.contrib.sitemaps import Sitemap
from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, post):
        return post.published_date
        
    def location(self, post):
        #return post.get_absolute_url
        return '/blog/post/%s' % (post.slug)

