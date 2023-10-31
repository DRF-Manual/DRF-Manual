"""쿼리셋 평가 메소드"""
from django.db.models import Sum
from models import Animal

# get(*args, **kwargs)
# aget(*args, **kwargs)
Animal.objects.get(id=1)
Animal.objects.get(pk=1) 

# create(**kwargs)
# acreate(**kwargs)

# get_or_create(defaults=None, **kwargs)
# aget_or_create(defaults=None, **kwargs)

# update_or_create(defaults=None, **kwargs)
# aupdate_or_create(defaults=None, **kwargs)

# bulk_create(objs, batch_size=None, ignore_conflicts=False, update_conflicts=False, update_fields=None, unique_fields=None)
# abulk_create(objs, batch_size=None, ignore_conflicts=False, update_conflicts=False, update_fields=None, unique_fields=None)

# bulk_update(objs, fields, batch_size=None)
# abulk_update(objs, fields, batch_size=None)

# count()
# acount()
Animal.objects.count()   
Animal.objects.filter(medical_check=True).count() 

# in_bulk(id_list=None, *, field_name='pk')
# ain_bulk(id_list=None, *, field_name='pk')
Animal.objects.in_bulk([1]) 

# iterator(chunk_size=None)
# aiterator(chunk_size=None)
queryset = Animal.objects.filter(medical_check=True)
for i in queryset.iterator():
    print(i.name)

# latest(*fields)
# alatest(*fields)
Animal.objects.latest("name") 

# earliest(*fields)
# aearliest(*fields)
Animal.objects.earliest("name") 

# first()
# afirst()
Animal.objects.first()                              

# last()
# alast()
Animal.objects.last()          

# aggregate(*args, **kwargs)
# aaggregate(*args, **kwargs)
Animal.objects.aggregate(total_animal=Sum("id"))   

# exists()
# aexists()
Animal.objects.exists()

# contains(obj)
# acontains(obj)
queryset1 = Animal.objects.filter()
queryset1.contains(Zoo)

# update(**kwargs)
# aupdate(**kwargs)
Animal.objects.filter(name="Penguin").update(medical_check=True) 

# delete()
# adelete()

# explain(format=None, **options)
# aexplain(format=None, **options)
Animal.objects.filter(name="Tiger").explain()