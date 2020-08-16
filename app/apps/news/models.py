from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=64)
    overview=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='courses'
        verbose_name='课程'
        verbose_name_plural=verbose_name
        ordering=('-created',)

    def __str__(self):
        return self.title