from django.db import models

from django_summernote.fields import SummernoteTextField

class Article(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField( upload_to='5m/blog/')
    description = models.TextField()
    content = SummernoteTextField()  # CKEditor rich text field
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class EmailSubmission(models.Model):
    email = models.EmailField(unique=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
