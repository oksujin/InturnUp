from django.db import models

# Create your models here.

"""
모델은 기본적으로 class로 구성.
원하는 class를 작성해서 넣어줘야함.
여기서는 게시판을 구현
"""

"""
 게시판 작성시 필요한 구성요소들
 장고 doc에서 다양한 field를 확인할 수 있다.
"""
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)
    # 게시물이 생성된 날짜, 시간 : 자동으로 이동

