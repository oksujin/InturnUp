# Generated by Django 2.2.3 on 2019-07-22 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Uniuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '유니포인트 인턴업 게시글',
                'verbose_name_plural': '유니포인트 인턴업 게시글',
                'db_table': 'inturnup_board',
            },
        ),
    ]
