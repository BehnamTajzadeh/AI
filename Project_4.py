points=[(1,3),(3,1)]
alpha = 0.01
w = 0 
b = 0 
step_needed= 5

for i in range(step_needed):
    w_total=0
    b_total=0
    for j in points:
        w_total += j[0]*(j[1]-w*j[0]-b) 
        b_total += (j[1]-w*j[0]-b) 
    dw= -2*w_total
    db= -2*b_total
    print("Step : ",i+1)
    w=w-alpha*dw
    print("W = ",w)
    b=b-alpha*db
    print("B = ",b)

    

    