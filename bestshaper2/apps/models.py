from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    nick_name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    mail = models.EmailField

class Brassiere(models.Model):
    bra_name = models.CharField(max_length=32)
    wash_num = models.IntegerField()

#受け取ったデータでデータベースを更新する処理
# def put_wash_num(models.Model):
#     b = Brassiere.objects.get(pk='1')
#     serializedData =
#
#


# class Entry(models.Model):
#     STATUS_DRAFT = "draft"
#     STATUS_PUBLIC = "public"
#     STATUS_SET = (
#         (STATUS_DRAFT, "下書き"),
#         (STATUS_PUBLIC, "公開中"),
#     )
#     title = models.CharField(max_length=128)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
#     author = models.ForeignKey(User, related_name='entries')
