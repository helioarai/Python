import turtle
bob=turtle.Turtle()

def desenhar (bob,c):    
    #print(bob)
    for i in range (0,c) :
        bob.fd(600/c)
        bob.lt(360/c)
    turtle.mainloop()

lados=int(input('Adicione o numero de lados do polígono : '))
desenhar(bob,lados)