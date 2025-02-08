from django.db import models
import uuid


class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,  # 自动生成 UUID4
        editable=False,  # 禁止编辑
        unique=True
    )
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = 'user'
        db_table_comment = 'All users data'
