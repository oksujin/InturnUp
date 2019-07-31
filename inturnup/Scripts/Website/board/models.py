from django.db import models


class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.Uniuser', on_delete=models.CASCADE,
                               verbose_name='작성자')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'inturnup_board'
        verbose_name = "유니포인트 인턴업 게시글"
        verbose_name_plural = "유니포인트 인턴업 게시글"

class UploadFileModel(models.Model):
        title = models.TextField(default='')
        file = models.FileField(null=True)