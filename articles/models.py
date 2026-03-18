from django.db import models

# Create your models here.
class Article(models.Model):
    titre_article = models.CharField(max_length=500)
    description_article = models.TextField(blank=True, null=True)
    titre_1 = models.CharField(max_length=300)
    paragraphe_1 = models.TextField()
    titre_2 = models.CharField(max_length=300,blank=True, null=True)
    paragraphe_2 = models.TextField(blank=True, null=True)
    titre_3 = models.CharField(max_length=300,blank=True, null=True)
    paragraphe_3 = models.TextField(blank=True, null=True)
    titre_4 = models.CharField(max_length=300,blank=True, null=True)
    paragraphe_4 = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f" {self.id} titre : {self.titre_article}"
    
