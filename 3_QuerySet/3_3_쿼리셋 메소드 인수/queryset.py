"""쿼리셋 메소드 인수"""
import datetime
from models import Animal

# exact
Animal.objects.get(id__exact=1)
Animal.objects.filter(info__exact=None)

# in
Animal.objects.filter(id__in=[1, 3, 5])

# range
Animal.objects.filter(birth_at__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))

# isnull
Animal.objects.filter(medical_check__isnull=False)
Animal.objects.filter(medical_check__isnull=True)

# regex
Animal.objects.filter(info__regex=r"Star(.*?)")

# iregex
Animal.objects.filter(info__iregex=r"star(.*?)")


# LIKE & ILKIE 연산자
# iexact
Animal.objects.filter(info__iexact="king of the zoo")

# contains
Animal.objects.get(info__contains="BBC")

# icontains
Animal.objects.filter(info__icontains="the")

# startswith
Animal.objects.get(info__startswith="Our")

# istartswith
Animal.objects.filter(info__istartswith="the")

# endswith
Animal.objects.filter(info__endswith="animal")

# iendwith
Animal.objects.filter(info__iendswith="bbc")


# 비교 연산자
# gt
Animal.objects.filter(id__gt=3)

# gte
Animal.objects.filter(id__gte=3)

# lt
Animal.objects.filter(id__lt=3)

# lte
Animal.objects.filter(id__lte=3) 


# 날짜와 시간
# date
Animal.objects.get(birth_at__date=datetime.date(2021, 8, 16))

# year
Animal.objects.filter(birth_at__year=2022)

# iso_year
Animal.objects.filter(birth_at__iso_year=2023)

# month
Animal.objects.filter(birth_at__month=8)

# day
Animal.objects.filter(birth_at__day=16)

# week
Animal.objects.filter(birth_at__week=1)

# week_day
Animal.objects.filter(birth_at__week_day=1)

# iso_week_day
Animal.objects.filter(birth_at__iso_week_day=1)

# quarter
Animal.objects.filter(birth_at__quarter=2)

# time
Animal.objects.filter(birth_at__time=datetime.time(9))

# hour
Animal.objects.filter(birth_at__hour=9)

# minute
Animal.objects.filter(birth_at__minute=30)

# second
Animal.objects.filter(birth_at__second=10)