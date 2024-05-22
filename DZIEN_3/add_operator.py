class Count:
    def __init__(self,count):
        self._count=count

    def __add__(self,other):
        total_count = self._count + other._count
        return Count(total_count)

    def __str__(self):
        return f'Count: {self._count}'

#vanilla method

c1 = Count(34)
c2 = Count(16)
c5 = Count(22)

c3 = c1+c2+c5
print(type(c3))

print(c3)
