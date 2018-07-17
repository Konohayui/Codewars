def remove_smallest(numbers):
    if len(numbers) > 0:
        m = min(numbers)
        print(m)
        numbers.remove(m)
        return numbers
    else:
        return numbers
    raise NotImplementedError("TODO: remove_smallest")
