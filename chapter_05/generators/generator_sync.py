def positive_integers(until: int):
    for integer in range(until):
        yield integer

positive_integers = positive_integers(3)
for integer in positive_integers:
    print(integer)
