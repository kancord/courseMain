from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    #Курс
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''Служит для формирования ссылки'''
        from django.urls import reverse
        return reverse('course-detail', args=[str(self.id)])

    class Meta:
        #Порядок
        ordering = ['name']

class Subscribe(models.Model):
    #Подписки
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.course.name, self.subUser.username)

    class Meta:
        # Порядок
        ordering = ['course']
        #UK
        unique_together = ('course', 'subUser')

    #def get_absolute_url(self):
    #    '''Служит для формирования ссылки'''
    #    from django.urls import reverse
    #    return reverse('course-detail', args=[str(self.id)])

class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    media_file = models.FileField()
    class Meta:
        # Порядок
        ordering = ['name']

    def __str__(self):
        return self.name

