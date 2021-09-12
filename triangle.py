def classify_triangle(a, b, c):#determines triangle type
    if(a==b):#1st and 2nd sides are equal
        if(b==c):#2nd and 3rd sides are equal
            return "Equilateral"
        else:
            return "Isosceles"
    elif(b==c):#3rd and 2nd sides are equal
        return "Isosceles"
    elif(a==c):#1st and 3rd sides are equal
        return "Isosceles"
    return "Scalene"#if no side is equal
x = int(input("Enter side1: "))
y = int(input("Enter side2: "))
z = int(input("Enter side3: "))
if((x + y > z) and ( x + z > y) and (y + z > x)):#sum of 2 sides should be greater than 3rd side
    print("Triangle is " + classify_triangle(x, y, z))
else:
    print("Not a triangle")
if x**2+y**2==z**2:
    print('Right Triangle')
else:
    print('Not Right Triangle')
