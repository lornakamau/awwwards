from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('Profile Picture')
    bio =  models.TextField()
    location = models.CharField(max_length = 40)
    email = models.EmailField()
    link = models.URLField()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    def edit_bio(self, new_bio):
        self.bio = new_bio
        self.save()

class Project(models.Model):
    name = models.CharField(max_length = 30)
    screenshot = CloudinaryField('Project screenshot')
    description = models.TextField()
    link = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True, null = True)
    voters = models.ManyToManyField(Profile, related_name="votes")
    design_score = models.IntegerField(default=0)
    usability_score = models.IntegerField(default=0)
    content_score = models.IntegerField(default=0)
    average_design = models.FloatField(default=0,)
    average_usability = models.FloatField(default=0)
    average_content = models.FloatField(default=0)
    average_score = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def voters_count(self):
        return self.voters.count()

    @classmethod
    def display_all_projects(cls):
        return cls.objects.all()

    @classmethod 
    def search_project(cls,name):
        return Project.objects.filter(name__icontains = name)

    @classmethod
    def get_user_projects(cls,profile):
        return cls.objects.filter(profile=profile)

    class Meta:
        ordering = ['-post_date']
    
class Vote(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete= models.CASCADE, related_name = "votes")
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)

    def save_vote(self):
        self.save()

    def delete_vote(self):
        self.delete()

    @classmethod
    def get_project_votes(cls, project):
        return cls.objects.filter(project = project)

    @classmethod
    def get_project_voters(cls, voter):
        return cls.objects.filter(voter = voter)

    class Meta:
        ordering = ['-post_date']
    
