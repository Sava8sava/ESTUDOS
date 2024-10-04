from queue import Queue # type: ignore

lemon = Queue()
lemon.addQ('maurico',60)
#lemon.addQ('carlos',80)
lemon.addQ('teste',70)
lemon.addQ('teste',80)
lemon.addQ('teste',90)
lemon.addQ('teste',101)


lemon.addQ('fernando',20)

lemon.displayList()

lemon.dequeue()
lemon.dequeue()
lemon.displayList()

print(lemon.priority(5))
