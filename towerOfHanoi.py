def toh(n, a,b,c):
    if n == 1:
        print(f"Move {n} from A to C")
    else:
        toh(n-1,a,c,b)
        print(f"Move {n} from A to B")
        toh(n-1,b,a,c)
        print(f"Move {n} from B to C")
