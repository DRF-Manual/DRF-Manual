"""쿼리셋 반환 메소드"""
from django.db.models import Count
from models import Animal

# filter(* args, ** kwargs)
Animal.objects.filter(name="Tiger", zoo_id=1, medical_check__exact=True)

# exclude(* args, ** kwargs)
Animal.objects.exclude(zoo_id__exact=1, medical_check=True)

# annotate(* args, ** kwargs)
q = Animal.objects.annotate(number_of_animal=Count("id"))
q[0].name
q[0].number_of_animal

# alias(*args, **kwargs)

# order_by(*fields)
Animal.objects.order_by("id")
Animal.objects.order_by('-birth_at')

# reverse()
Animal.objects.order_by('-birth_at').reverse()

# distinct(*fields)
Animal.objects.distinct()
Animal.objects.distinct("medical_check")

# values(*fields, **expressions)
Animal.objects.filter().values()

# values_list(*fields, flat=False, named=False)
Animal.objects.filter().values_list()

# dates(field, kind, order='ASC')
Animal.objects.dates("birth_at", "day")

# datetimes(field_name, kind, order='ASC', tzinfo=None)
Animal.objects.datetimes("birth_at", "hour", order="DESC")

# none()
Animal.objects.none()

# all()
Animal.objects.all()
Animal.objects.none().all()

# union(*other_qs, all=False)

# intersection(*other_qs)

# difference(*other_qs)

# select_related(*fields)

# prefetch_related(*lookups)

# defer(*fields)

# only(*fields)

# using(alias)
Animal.objects.using("backup")

# select_for_update(nowait=False, skip_locked=False, of=(), no_key=False)

# raw(raw_query, params=(), translations=None, using=None)