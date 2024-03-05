from django.db import models
from django.utils import timezone


class ForumThread(models.Model):
    course_id = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.title} [Course ID: {self.course_id}]'
    
    class Meta:
        ordering = ['-created_date']


class ThreadReply(models.Model):
    thread = models.ForeignKey(
        ForumThread,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    user_id = models.IntegerField()
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Reply by User {self.user_id} on "{self.thread.title}"'
    
    class Meta:
        ordering = ['-created_date']