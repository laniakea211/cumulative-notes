def lineargcd(a,b):
    alist = [a]
    coeff = []
    counter = 0
    while b:
        a, b = b, a%b
        alist.append(a)
        coeff.append( (alist[counter] - b) // a)
        counter = counter + 1
    x, y = 1, 0
    for i in range(len(coeff) - 1):
        x, y = x, y + x*coeff[-i-2]
        x, y = y, x
    if len(coeff) % 2 == 0:
        x, y = y, x
    return alist[-1], x, y, len(coeff) % 2

x, y = input("Enter the two numbers you'd like to find the "\
        "g.c.d. of: ").split()
x = int(x)
y = int(y)

if lineargcd(x,y)[3] == 0:
    print(f"The g.c.d. of {x} and {y} is {lineargcd(x,y)[0]}.")
    print(f"You can write this g.c.d. as: "\
            "{x}*{lineargcd(x,y)[1]} - {y}*{lineargcd(x,y)[2]}.")

if lineargcd(x,y)[3] == 1:
    print(f"The g.c.d. of {x} and {y} is {lineargcd(x,y)[0]}.")
    print(f"You can write this g.c.d. as: "\
            "{y}*{lineargcd(x,y)[1]} - {x}*{lineargcd(x,y)[2]}.")
