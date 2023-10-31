"""쿼리셋 결합"""
from django.db.models import Q
from models import Animal

Animal.objects.filter(Q(birth_at__year__gt=2021) | ~Q(medical_check__exact=True))

# 연산자를 통한 쿼리셋 결합
Animal.objects.filter(zoo=1) | Animal.objects.filter(zoo=2)

# Q 객체를 사용한 결합
Animal.objects.filter(Q(zoo=1) | Q(zoo=2))