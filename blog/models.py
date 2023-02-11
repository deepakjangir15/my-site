from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts',null=True)
    tags = models.ManyToManyField(Tag)
    url = models.URLField(max_length=200, blank=True, default='',null=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    date_posted = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')

class Certificate(models.Model):
    certificate_name = models.CharField(max_length=100)
    certificate_issuer = models.CharField(max_length=100)
    certificate_issue_date = models.DateField()
    certificate_expiry_date = models.DateField(null=True,blank=True)
    certificate_credential_id = models.CharField(max_length=120)
    certificate_url = models.URLField(max_length=200, blank=True, default='',null=True)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return f"{self.certificate_name}"
    

