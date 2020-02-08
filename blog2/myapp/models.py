from django.db import models


class Author(models.Model):
    authorname = models.CharField(max_length=100)
    createtime = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.authorname

    class Meta:
        verbose_name = verbose_name_plural = '作者'

class Post(models.Model):
    postAuthor = models.ForeignKey(Author,on_delete=models.CASCADE)
    posttitle = models.CharField(max_length=100)
    comment = models.TextField()
    createtime = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("category",on_delete=models.CASCADE)

    def __str__(self):
        return self.posttitle

    class Meta:
        verbose_name = verbose_name_plural = '文章'


class User(models.Model):
    username = models.CharField(max_length=100)
    userpasswd = models.CharField(max_length=100)
    createtime = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = verbose_name_plural = '用户'

class Remark(models.Model):
    owner = models.ForeignKey("User",on_delete=models.CASCADE)
    content = models.TextField()
    createtime = models.DateTimeField(auto_now_add=True)
    posttitle = models.ForeignKey(Post,on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)


    class Meta:
        verbose_name = verbose_name_plural = '评论'

class category(models.Model):
    cate_name = models.CharField(max_length=50)
    createtime = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = verbose_name_plural = '分类'


