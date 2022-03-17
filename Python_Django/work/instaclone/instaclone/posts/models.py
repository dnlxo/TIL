from django.db import models
from instaclone.instaclone.users import models as user_model

# Create your models here.
class TimeStampModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True # 얘는 단독으로 테이블이 안만들어짐

class Post(TimeStampModel):
    author = models.ForeignKey(
        user_model.user,
        null=True,
        on_delete=models.CASCADE,
        related_name='post_author'
    )


class Comment(TimeStampModel):
    pass
