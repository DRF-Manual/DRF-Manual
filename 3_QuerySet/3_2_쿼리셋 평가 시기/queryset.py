"""쿼리셋 평가 시기"""
import pickle
from models import Animal

# lteration (Asynchronous iteration)
for i in Animal.objects.all():
    print(i.name)

# Slicing
Animal.objects.all()[:4:2]

# Pickling/Caching
query = pickle.loads(pickled_data)
queryset = Animal.objects.all()
queryset.query = query

# repr()
repr(Animal.objects.filter(id__exact=1))

# len()
len(Animal.objects.all())

# list()
list(Animal.objects.all())

# bool()
if Animal.objects.filter(name="Tiger"):
    print("There is a Tiger!")