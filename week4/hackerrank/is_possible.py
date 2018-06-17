"""
https://www.hackerrank.com/tests/gm0rslbegqt/questions/np712m6m
"""
def get_neighbors(a, b):
    return ((a+b, b), (a, a+b))

def isPossible(a, b, c, d):
    queue = []
    queue.append((a,b))
    while queue:
        vertex = queue.pop(0)
        a, b = vertex
        for neighbor in get_neighbors(a, b):
            new_a, new_b = neighbor
            if neighbor == (c, d):
                return True
            # check if neighbor is beyond (c,d)
            if new_a > c:
                continue
            if new_b > d:
                continue
            queue.append((new_a, new_b))
    return False

def main():
    a, b, c, d = 1, 4, 5, 10
    assert isPossible(a, b, c, d) == False
    a, b, c, d = 1, 4, 5, 4
    assert isPossible(1, 4, 5, 4) == True
    a, b, c, d = 1, 4, 5, 4
    assert isPossible(1, 4, 5, 4) == True

if __name__ == "__main__":
    main()
