from manimlib.imports import *

def tex(str):
    return TexMobject(str, ).scale(0.7)

def xy(x, y):
    return np.array([x, y, 0])

class CircleOnComplexPlane(MovingCameraScene):
    def construct(self):
        self.draw_axis()
        self.draw_circle()
        self.move_circle()

        self.wait()

    def draw_axis(self):
        min_x, max_x = -6, -2
        min_y, max_y = 0, 3.7

        ori = xy(-4, 2)

        def get_line(s,e):
            return Line(s,e , color=BLUE, stroke_width=5)

        x_axis = get_line(xy(min_x,ori[1]), xy(max_x,ori[1]))
        y_axis = get_line(xy(ori[0], min_y), xy(ori[0], max_y))

        t_x1=tex("1").scale(0.85).move_to(xy(-3,2)).shift(RIGHT*0.1+DOWN*0.15)
        t_xm1=tex("-1").scale(0.85).move_to(xy(-5, 2)).shift(LEFT * 0.25 + DOWN * 0.15)
        t_y1=tex("i").move_to(xy(-4, 3)).shift(LEFT * 0.2+UP*0.2 )
        t_ym1=tex("-i").move_to(xy(-4, 1)).shift(LEFT * 0.25+DOWN*0.15 )

        self.add(x_axis, y_axis)
        self.add(t_x1, t_xm1,t_y1,t_ym1)

        self.ori = ori

    def draw_circle(self):
        ori = self.ori

        circle = Circle(radius=1).move_to(ori)
        self.add(circle)

        self.circle = circle

    def move_circle(self):
        circle = self.circle
        dot = Dot(radius=0.06).move_to(xy(-3,2))
        cf = self.camera_frame

        self.play(
            cf.move_to,self.ori,
            cf.scale, 0.5,
            run_time=2,
        )
        self.play(ShowCreation(dot))

        vt = ValueTracker(0)
        def update_dot(mob):
            p = vt.get_value() %  1
            mob.move_to(circle.point_from_proportion(p))

        dot.add_updater(update_dot)

        self.play(vt.set_value, 1.00, rate_func=linear)

        dot.remove_updater(update_dot)

        ## line위 dot
        dot2=Dot(radius=0.04, color=YELLOW).move_to(xy(-3,2))
        line = Line(dot2.center(),dot2.center())

        self.play(
            ShowCreation(dot2),
            ShowCreation(line),
        )

        def update_dot2(mob):
            y = self.ori[1]
            x = dot.get_center()[0]
            mob.move_to(xy(x,y))

        def update_line(mob):
            new_line = Line(dot.get_center(), dot2.get_center())
            mob.become(new_line)

        dot2.add_updater(update_dot2)
        line.add_updater(update_line)
        dot.add_updater(update_dot)

        vt.set_value(0)
        self.play(vt.set_value,2, rate_func=linear, run_time=8)
