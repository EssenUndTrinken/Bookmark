from django.db import models
from django.urls import reverse
# Create your models here.
# 모델 : 데이터베이스를 SQL없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루겠다
# 모델 = 테이블

class Bookmark(models.Model):
    site_name = models.CharField(max_length=35)
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는것...
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항 (몇x글자?)
    # 3. Form 의 종류, Form에서 제약사항...!
    # 모델을 만들었다 데이터베이스에 어떤 데이터ㄹ들을 어떤 형태로 넣을지 결정!
    #     마이그레이션 데이터베이스에 모델의 내용을 반영!
    #     makemigrations 모델의 변경사항을 추적해서 기록!
    def __str__(self):
        return "name : " +  self.site_name+ ", adress :" + self.url
    def get_absolute_url(self):
        return reverse('detail', args =[str(self.id)])
