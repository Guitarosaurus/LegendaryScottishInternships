from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    MAX_NAME_LENGTH = 255
    MAX_ADDR_LENGTH = 255
    MAX_EMAIL_LENGTH = 127
    MAX_URL_LENGTH = 255
    
    name = models.CharField(max_length=MAX_NAME_LENGTH, unique=True)
    address = models.CharField(max_length=MAX_ADDR_LENGTH, default="None")
    email = models.CharField(max_length=MAX_EMAIL_LENGTH, default="no.email@provided") # This default string may need formatting
    website = models.CharField(max_length=MAX_URL_LENGTH, default="https://en.wikipedia.org/w/index.php?search=&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'companies'

class Internship(models.Model):
    MAX_NAME_LENGTH = 255
    MAX_DESC_LENGTH = 1023
    MAX_ADDR_LENGTH = 255
    MAX_LIST_LENGTH = 1023 # This may not be long enough?
    # id = models.AutoField(primary_key=True) # This is added automatically by django
    name = models.CharField(max_length=MAX_NAME_LENGTH, unique=True)
    description = models.CharField(max_length=MAX_DESC_LENGTH, default="This is an internship...")
    closing_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.FloatField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=MAX_ADDR_LENGTH, default="None")
    checklist = models.CharField(max_length=MAX_LIST_LENGTH, default="No extra items") # This default string may need formatting
    slug = models.SlugField(unique=True)
    user_ids = models.ManyToManyField(User)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Internship, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Comment(models.Model):
    MAX_COMMENT_LENGTH = 1023
    data = models.CharField(max_length=MAX_COMMENT_LENGTH)
    internship_id = models.ForeignKey(Internship, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
        
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', default='/images/generic_profile.jpg', blank=True)
    
    def __str__(self):
        return self.user.username
