def classify_triangle(a:float,b:float,c:float)->str:
    if a==b and b==c:
        return "equilateral"
    l=sorted([a,b,c])

    #Determines whether each side of a triangle is greater than 0
    for i in l:
        if i<=0:
            raise ValueError("The sild must more than zore")

    #Determine whether three sides make a triangle
    if l[0]+l[1]-l[2]<=0:
        raise ValueError("It is not an triangle")

    #Determine isosceles triangle
    if (l[0]==l[1] and l[1]!=l[2]) or (l[0]!=l[1] and l[1]==l[2]):
        return "isosceles"

    #Determining Right Triangles
    if l[0]*l[0]+l[1]*l[1]-l[2]*l[2]==0:
        return "right"

    #If neither of these conditions is true, ordinary triangle
    return "scalene"
def get_side()->list():
    l=[0,0,0]
    for i in range(3):
        l[i]=float(input(f"Please input the {i+1} side:"))
    return l

if __name__ == '__main__': 
    while(True):
        l=get_side()
        try:
            print(f"The type of triangles is: {classify_triangle(l[0],l[1],l[2])}")
        except ValueError as e:
            print(e)
        r=input("If you exit, type 'q' and other to continue")
        if r=='q':
            break