def euler(x,y,f,h,xend):
    file = open("question_one"+ str(h)+".txt", "w+")
    while (x<=xend):
        file.writelines([str(x)+"   ",str(y)+"\n"])
        y+=h*f(y,x)
        x+=h
    file.close()

def rungekutta4(x,y,z,dydx,dzdx,h,xstart,xend):
    file = open("RK4"+ str(h)+".txt", "w+")
    a=x
    b=y
    c=z
    g=-h
    while (x<=xend) and (a>=xstart):
        file.writelines([str(x)+"   ",str(y)+"\n"])

        k1y=h*dydx(z,x)
        k1z=h*dzdx(z,y,x)
        k1b=g*dydx(c,a)
        k1c=g*dzdx(c,b,a)

        k2y=h*dydx(z+k1z/2,x+h/2)
        k2z=h*dzdx(z,y+k1y/2,x+h/2)
        k2b=g*dydx(c+k1c/2,a+g/2)
        k2c=g*dzdx(c,b+k1b/2,a+g/2)

        k3y=h*dydx(z+k2z/2,x+h/2)
        k3z=h*dzdx(z,y+k2y/2,x+h/2)
        k3b=g*dydx(c+k2c/2,a+g/2)
        k3c=g*dzdx(c,b+k2b/2,a+g/2)

        k4y=h*dydx(z+k3z/2,x+h)
        k4z=h*dzdx(z,y+k3y/2,x+h)
        k4b=g*dydx(c+k3c/2,a+g)
        k4c=g*dzdx(c,b+k3b/2,a+g)

        y+=(k1y + 2*k2y + 2*k3y + k4y)/6
        b+=(k1b + 2*k2b + 2*k3b + k4b)/6
        z+=(k1z + 2*k2z + 2*k3z + k4z)/6
        c+=(k1c + 2*k2c + 2*k3c + k4c)/6
        x+=h
        a+=g
        file.writelines([str(a)+"   ",str(b)+"\n"])
    file.close()

