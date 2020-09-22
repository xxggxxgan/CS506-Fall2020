def euclidean_dist(x, y):
    if (len(x) != len(y)):
        raise ValueError("Error! lengths must be equal")
    result = sum([abs(x[i] - y[i])**2 for i in range(len(x))])**(1/2)
    return result
    
def manhattan_dist(x, y):
    if (len(x) != len(y)):
        raise ValueError("Error! lengths must be equal")
    result = sum([abs(x[i] - y[i]) for i in range(len(x))])
    return result

def jaccard_dist(x, y):
    if (len(x) != len(y)):
        raise ValueError("Error! lengths must be equal")
    result = 0
    if (x == []):
        result = 0
    elif (y == []):
        result = 0
    else:
        result = 1 - ((len(set(x).intersection(set(y))))/len(set(x).union(set(y))))
    return result

def cosine_sim(x, y):
    if (len(x) != len(y)):
        raise ValueError("Error! lengths must be equal")
    x_len = sum([num**2 for num in x])**0.5
    y_len = sum([num**2 for num in y])**0.5
    if x_len == 0 or y_len == 0:
        raise ValueError("Error! lengths must not be zero")
    inner_product = sum([x[i] * y[i] for i in range(len(x))])
    result = inner_product / (x_len * y_len)
    return result

# Feel free to add more
