from django.db import models
from django.contrib.auth.models import User
# from posts.models import PostsModels

# Create your models here.
class UserModels(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    following = models.ManyToManyField('self', related_name='follower', symmetrical=False)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return 'posts/{}/'.format(self.name)

class PostsModels(models.Model):
    author = models.ForeignKey(UserModels, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Título', default='Sem título')
    slug = models.SlugField(max_length=50, unique=True)
    text = models.TextField(verbose_name='Texto', null=False, blank=False)
    like = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '{} ({})'.format(self.title, self.created)

    def get_absolute_url(self):
        return 'posts/{}/'.format(self.slug)