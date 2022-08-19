def my_range(stop: float, start: float = 0.0, step: float =1.0) -> list[float]:
    res=[]
    while start<stop:
        res.append(start)
        start+=step
    return res

print(my_range(        10))