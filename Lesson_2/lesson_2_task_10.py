def bank(X, Y):
    total = X
    for year in range(Y):
        total *= 1.10 
    return total
X = 5000 
Y = 5
result = bank(X, Y)
print("Сумма через", Y, "лет:", result)