from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import uuid


def upload_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['avatars', str(instance.user_profile.id) + str(".") + str(ext)])

class Profile(models.Model):
    user_profile = models.OneToOneField(
        User, related_name='user_profile',
        on_delete=models.CASCADE
    )
    img = models.ImageField(blank=True, null=True, upload_to=upload_avatar_path)

    def __str__(self):
        return self.user_profile.username

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS = (
        ('1', '新規'),
        ('2', '進行中'),
        ('3', '完了'),
    )

    PROGRESS = (
        ('0', '0%'),
        ('1', '10%'),
        ('2', '20%'),
        ('3', '30%'),
        ('4', '40%'),
        ('5', '50%'),
        ('6', '60%'),
        ('7', '70%'),
        ('8', '80%'),
        ('9', '90%'),
        ('10', '100%'),

    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    criteria = models.CharField(max_length=100)
    status = models.CharField(max_length=40, choices=STATUS, default='1')
    progress = models.CharField(max_length=40, choices=PROGRESS, default='0')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    estimate = models.IntegerField(validators=[MinValueValidator(0)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsible')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

class Comment(models.Model):
    text = models.CharField(max_length=200)
    user_comment = models.ForeignKey(
        User, related_name='userComment',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
