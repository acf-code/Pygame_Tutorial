from random import randint

list_rand = []
for i in range(10000):
    list_rand.append(randint(-100,100))

print(list_rand)

def quick_sort(li):
    if len(li) <= 1:
        return li
    else:
        pivot = li[0]
        left = [x for x in li[1:] if x < pivot]
        right = [x for x in li[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
    
list_sort = quick_sort(list_rand)
print(list_sort)
