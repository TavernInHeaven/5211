import turtle


def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0],points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0],points[1][1])
    my_turtle.goto(points[2][0],points[2][1])
    my_turtle.goto(points[0][0],points[0][1])
    my_turtle.end_fill()


def get_mid(p1,p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree,my_turtle):
    color_map = ['blue', 'red','green','white','yellow','violet','orange']
    draw_triangle(points,color_map[degree],my_turtle)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0],points[1]),get_mid(points[0],points[1])], degree - 1, my_turtle)
        sierpinski([points[1], get_mid(points[0],points[1]),get_mid(points[1],points[2])], degree - 1, my_turtle)
        sierpinski([points[2], get_mid(points[2],points[1]),get_mid(points[0],points[2])], degree - 1, my_turtle)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100, -50], [0,100], [100,-50]]
    sierpinski(my_points, 3, my_turtle)
    my_win.exitonclick()

def poll(n):
    if n<=1:
        return n
    else:
        return poll(n%2) + poll(n//2)

print(poll(31))

def my(n,i = 2):
    if i * i <= n:
        if n % i == 0:
            my(n//i,i)
            print(i)
        else:
            my(n,i+1)
    else:
        print(n)

print(my(100))