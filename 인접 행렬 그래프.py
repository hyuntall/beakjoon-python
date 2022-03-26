SIZE = 5
graph = [[0] * SIZE for i in range(SIZE)]
def insert(give, receive, weight, direction):
    if direction:
        graph[receive][give] = weight

    graph[give][receive] = weight

insert(0, 1, 1, 1)
insert(0, 3, 1, 1)
insert(1, 2, 1, 1)
insert(1, 3, 1, 1)
insert(2, 3, 1, 1)

for i in graph:
    print(i)