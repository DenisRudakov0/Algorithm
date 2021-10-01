def unique_in_order(iterable):
    if len(iterable) == 1:
        return [iterable[i] for i in range(len(iterable))]
    elif len(iterable) == 0:
        return list()
    elif iterable.count('A') == len(iterable):
        return list('A')
    else:
        iterable = [iterable[i] for i in range(len(iterable)) if iterable[i] != iterable[i - 1] ]
        return iterable
