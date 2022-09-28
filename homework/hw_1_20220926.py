import turtle as t

#def canvas color
t.bgcolor("gray")

#make a circle
def circle (rad,x,y,cirColor,lineColor,lineWidth):
    t.pencolor(lineColor)
    t.width(lineWidth)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.fillcolor(cirColor)
    t.begin_fill()
    t.circle(rad)
    t.fillcolor(cirColor)
    t.end_fill()
    t.penup()


#make a ellipse(eyes)
def Ellipse(size,x,y,lineColor,Ecolor,lineWidth):
    t.setpos(x,y)
    t.pencolor(lineColor)
    t.width(lineWidth)
    t.pendown()
    t.fillcolor(Ecolor)
    t.begin_fill()
    t.right(45)
    for i in range(2):
        t.circle(size,90)
        t.circle(size/2,90)
    t.left(45)
    t.end_fill()
    t.penup()

#make a smile
def smile(x,y,smileColor,FaceColor,rad):
    circle(rad,x,y,smileColor,smileColor,1)
    circle(rad+10,x,y+(rad+10)/2,FaceColor,FaceColor,1)

#making a face
circle(400,0,-400,"#ffe6ee","#fdab9f",10)
#making a nose
circle(20,0,-10,"black","black",5)
#making a eyes(R/L)
Ellipse(100,100,150,"black","blue",20)#R eye
Ellipse(70,-250,100,"black","skyblue",5)#L eye
#smile!
smile(0,-300,"red","#ffe6ee",100)
#end drawing
t.penup()

#displaying!!!!
t.exitonclick()
