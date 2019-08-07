from django.db import models


class Commute(models.Model):
    objects = models.Manager()
    commuter = models.ForeignKey('user.Uniuser', on_delete=models.CASCADE,
                                 verbose_name='기록자')
    registered_go_work = models.DateTimeField(
        auto_now_add=True, verbose_name='출근시간')
    registered_off_work = models.DateTimeField(
        auto_now_add=True, verbose_name='퇴근시간')

    def __str__(self):
        return self.commuter

    class Meta:
        db_table = 'inturnup_commute'
        verbose_name = "유니포인트 인턴업 출퇴근 기록부"
        verbose_name_plural = "유니포인트 출퇴근 기록부"
