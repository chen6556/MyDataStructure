from structure import LinkedList

linkedlist = LinkedList(range(10))
print(linkedlist)

linkedlist.insert(0, 10)
print(len(linkedlist))

linkedlist.remove(10)
print(linkedlist)

for i in reversed(linkedlist):
    print(i, end=',')
print()

for i in range(10):
    linkedlist[i] += 7
print(linkedlist)

for i in range(3):
    while True:
        try:
            print(next(linkedlist), end=',')
        except StopIteration:
            print()
            break

linkedlist.clear()
print(linkedlist)