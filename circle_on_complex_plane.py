from manimlib.imports import *

def tex(str, color=WHITE):
    return TexMobject(str, color=color).scale(0.7)

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

class CircleOnComplexPlane_COS(Scene):
    def construct(self):
        self.draw_axis()
        self.draw_circle()
        self.move_circle()

        self.wait(2)

    def draw_axis(self):
        min_x, max_x = -6, -2
        min_y, max_y = -3.7, 3.7

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

        self.play(ShowCreation(dot))

        vt = ValueTracker(0)
        def update_dot(mob):
            p = vt.get_value() %  1
            mob.move_to(circle.point_from_proportion(p))

        dot.add_updater(update_dot)

        self.play(vt.set_value, 1.00, rate_func=linear)

        dot.remove_updater(update_dot)

        dot2=Dot(radius=0.04, color=YELLOW).move_to(xy(-3,2))
        line = Line(dot2.get_center(),dot2.get_center())
        wave = VGroup(Line(dot2.get_center(),dot2.get_center(), color=YELLOW))

        self.play(
            ShowCreation(dot2),
            ShowCreation(line),
            ShowCreation(wave),
        )

        #cosine 라인괘적
        def update_dot2(mob):
            y = self.ori[1] - (vt.get_value() % 1.0) * 5
            x = dot.get_center()[0]
            mob.move_to(xy(x,y))

        def update_line(mob):
            new_line = Line(dot.get_center(), dot2.get_center())
            mob.become(new_line)

        def update_wave(mob):
            line_group = mob.copy()
            last_line = line_group[-1]

            s = last_line.get_end()
            e = dot2.get_center()

            #두바퀴째 원을 그릴때, wave끝에서 dot2쪽으로의 선이 그려지지 않게하기위함임
            if s[1] < e[1]: return

            new_line = Line(s, e, color=YELLOW_D)
            line_group.add(new_line)
            mob.become(line_group)

        dot2.add_updater(update_dot2)
        line.add_updater(update_line)
        dot.add_updater(update_dot)
        wave.add_updater(update_wave)

        vt.set_value(0)
        self.play(vt.set_value,2, rate_func=linear, run_time=8)


class CircleOnComplexPlane_Imaginary(MovingCameraScene):
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
            y = dot.get_center()[1]
            x = self.ori[0] #고정
            mob.move_to(xy(x,y))

        def update_line(mob):
            new_line = Line(dot.get_center(), dot2.get_center())
            mob.become(new_line)

        dot2.add_updater(update_dot2)
        line.add_updater(update_line)
        dot.add_updater(update_dot)

        vt.set_value(0)
        self.play(vt.set_value,1, rate_func=linear, run_time=4)
        self.wait()
        self.play(vt.set_value, 2, rate_func=linear, run_time=4)


class CircleOnComplexPlane_SIN(Scene):
    def construct(self):
        self.draw_axis()
        self.draw_circle()
        self.move_circle()

        self.wait(1)

    def draw_axis(self):
        min_x, max_x = -6, 2
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
        dot = Dot(radius=0.06).move_to(xy(-3,2)) #원위를 움직인느.

        self.play(ShowCreation(dot))

        vt = ValueTracker(0)
        def update_dot(mob):
            p = vt.get_value() %  1
            mob.move_to(circle.point_from_proportion(p))

        dot.add_updater(update_dot)

        self.play(vt.set_value, 1.00, rate_func=linear)

        dot.remove_updater(update_dot)

        dot2=Dot(radius=0.04, color=YELLOW).move_to(self.ori) #사인파를 그리는.
        line = Line(dot2.get_center(),dot2.get_center())
        wave = VGroup(Line(dot2.get_center(),dot2.get_center(), color=YELLOW))

        self.play(
            ShowCreation(dot2),
            ShowCreation(line),
            ShowCreation(wave),
        )

        #sine 라인괘적을 따라 움직인다.
        def update_dot2(mob):
            y = dot.get_center()[1]  #sin 괘적. 원위의 dot의 y좌표
            x = self.ori[0] + (vt.get_value() % 1.0) * 5 #시간의 흐름
            mob.move_to(xy(x,y))

        def update_line(mob):
            new_line = Line(dot.get_center(), dot2.get_center())
            mob.become(new_line)

        def update_wave(mob):
            line_group = mob.copy()
            last_line = line_group[-1]

            s = last_line.get_end()
            e = dot2.get_center()

            #두바퀴째 원을 그릴때, wave끝에서 dot2쪽으로의 선이 그려지지 않게하기위함임
            if s[0] > e[0]: return

            new_line = Line(s, e, color=YELLOW_D)
            line_group.add(new_line)
            mob.become(line_group)

        dot2.add_updater(update_dot2)
        line.add_updater(update_line)
        dot.add_updater(update_dot)
        wave.add_updater(update_wave)

        vt.set_value(0)
        self.play(vt.set_value, 0.4, rate_func=linear, run_time=3) #1. 처음부분은 천천히 보여주고
        self.wait()                                                #2. 잠시 쉬었다가
        self.play(vt.set_value,2, rate_func=linear, run_time=8)    #3. 나머지 전체를 보여줌

class CircleOnComplexPlane_SINCOS(Scene):
    def construct(self):
        self.draw_axis()
        self.draw_circle()
        self.move_circle()

        self.wait(1)

    def draw_axis(self):
        min_x, max_x = -6, 2
        min_y, max_y = -3.7, 3.7

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
        # self.add(circle)

        self.circle = circle

    def move_circle(self):
        circle = self.circle
        dot = Dot(radius=0.06).move_to(xy(-3,2)) #원위를 움직인느.

        self.play(ShowCreation(dot))

        vt = ValueTracker(0)
        def update_dot(mob):
            p = vt.get_value() %  1
            mob.move_to(circle.point_from_proportion(p))

        dot_sine=Dot(radius=0.06, color=YELLOW).move_to(self.ori) #사인파를 그리는.
        line_sine = Line(dot_sine.get_center(),dot_sine.get_center(), color=YELLOW)
        wave_sine = VGroup(Line(dot_sine.get_center(),dot_sine.get_center(), color=YELLOW))

        dot_cos = Dot(radius=0.06, color=WHITE).move_to(self.ori)  # 사인파를 그리는.
        line_cos = Line(dot_cos.get_center(), dot_cos.get_center(), color=WHITE)
        wave_cos = VGroup(Line(dot_cos.get_center(), dot_cos.get_center(), color=WHITE))

        circle_group = VGroup(Line(dot.get_center(), dot.get_center(), color=RED))

        self.play(
            ShowCreation(dot_sine),
            ShowCreation(line_sine),
            ShowCreation(wave_sine),

            ShowCreation(dot_cos),
            ShowCreation(line_cos),
            ShowCreation(wave_cos),

            ShowCreation(circle_group)
        )

        # sine 라인괘적을 따라 움직인다.
        def update_dot_sine(mob):
            y = dot.get_center()[1]  # sin 괘적. 원위의 dot의 y좌표
            x = self.ori[0] + (vt.get_value() % 1.0) * 5  # 시간의 흐름
            mob.move_to(xy(x, y))

        def update_line_sine(mob):
            new_line = Line(dot_sine.get_center(), dot.get_center(),color=YELLOW)
            mob.become(new_line)

        def update_wave_sine(mob):
            line_group = mob.copy()
            last_line = line_group[-1]

            s = last_line.get_end()
            e = dot_sine.get_center()

            #두바퀴째 원을 그릴때, wave끝에서 dot2쪽으로의 선이 그려지지 않게하기위함임
            if s[0] > e[0]: return

            new_line = Line(s, e, color=YELLOW_D)
            line_group.add(new_line)
            mob.become(line_group)

        # cos 라인괘적을 따라 움직인다.
        def update_dot_cos(mob):
            y = self.ori[1] - (vt.get_value() % 1.0) * 5  # 시간의 흐름
            x = dot.get_center()[0]  # cos 괘적. 원위의 dot의 x좌표
            mob.move_to(xy(x, y))

        def update_line_cos(mob):
            new_line = Line(dot_cos.get_center(), dot.get_center(),color=WHITE)
            mob.become(new_line)

        def update_wave_cos(mob):
            line_group = mob.copy()
            last_line = line_group[-1]

            s = last_line.get_end()
            e = dot_cos.get_center()

            # 두바퀴째 원을 그릴때, wave끝에서 dot2쪽으로의 선이 그려지지 않게하기위함임
            if s[1] < e[1]: return

            new_line = Line(s, e, color=WHITE)
            line_group.add(new_line)
            mob.become(line_group)

        def update_circle_group(mob):
            line_group = mob.copy()
            last_line = line_group[-1]

            s = last_line.get_end()
            e = dot.get_center()

            new_line = Line(s, e, color=RED)
            line_group.add(new_line)
            mob.become(line_group)

        dot_sine.add_updater(update_dot_sine)
        line_sine.add_updater(update_line_sine)
        wave_sine.add_updater(update_wave_sine)

        dot_cos.add_updater(update_dot_cos)
        line_cos.add_updater(update_line_cos)
        wave_cos.add_updater(update_wave_cos)

        dot.add_updater(update_dot)
        circle_group.add_updater(update_circle_group)

        vt.set_value(0)
        self.play(vt.set_value, 0.4, rate_func=linear, run_time=4) #1. 처음부분은 천천히 보여주고
        self.wait()                                                #2. 잠시 쉬었다가
        self.play(vt.set_value,1, rate_func=linear, run_time=4)    #3. 나머지 전체를 보여줌

        self.wait()
        vt.set_value(0)
        self.play(vt.set_value, 1, rate_func=linear, run_time=3)  # 3. 나머지 전체를 보여줌

class CircelOnComplexPlane_SINCOS2(MovingCameraScene):
    def construct(self):
        self.draw_axis()
        self.draw_cosine()
        self.draw_sine()
        self.draw_circle()

        self.wait()

    def draw_axis(self):
        min_x, max_x = -6, 2
        min_y, max_y = -3.7, 3.7

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

    def draw_cosine(self):
        max_len = 5

        #origin_point:원점, starting_point:그래프 시작점, curve_len:그래프의 길이
        def get_cosine_graph(op, sp, curve_len):
            t = np.arange(0,2*np.pi,0.1) # 0~2pi까지 0.1간격
            dt = curve_len / len(t)
            y_t = np.cos(t)
            g = VGroup(Line(sp,sp))
            for i in range(0, len(t)):
                end_p = g[-1].get_end()
                px = op[0] + y_t[i]
                py = end_p[1] - dt
                new_line = Line(end_p, xy(px,py))
                g.add(new_line)
            return g

        ori = self.ori

        cos_t = tex(r"\cos \theta").move_to(xy(-5.5,-0.5))
        graph_start_pos = xy(ori[0]+1, ori[1])
        cos_graph = get_cosine_graph(ori, graph_start_pos, max_len )
        self.add(cos_graph, cos_t)

        vt = ValueTracker(0)

        #1. dot가 코사인 그래프를 따라서 한번 왔다 갔다
        def update_dot(mob):
            alpha = vt.get_value() % 1.0
            subs = cos_graph.submobjects
            len_subs = len(subs)
            if len_subs == 0 : return

            pos = int(alpha * len_subs)
            mob.move_to(subs[pos])

        dot = Dot(color=WHITE).move_to(graph_start_pos)
        self.add(dot)
        dot.add_updater(update_dot)

        self.play(vt.set_value, 1, rate_func=there_and_back, run_time=4)
        # dot.remove_updater(update_dot)

        #2. 코사인그래프를 shrink
        def update_cos_graph(mob):
            # vt:   0   0.5   1
            # size: 0   2.5  5(=max_len)
            tgt_size = vt.get_value() * max_len
            new_graph = get_cosine_graph(ori, graph_start_pos, tgt_size)

            mob.become(new_graph)

        cos_graph.add_updater(update_cos_graph)
        vt.set_value(1)

        self.remove(cos_t)
        self.play(vt.set_value, 0, rate_func=linear, run_time=4)
        cos_graph.remove_updater(update_cos_graph)

        #3. 전부 shrink된다음에 왔다 갔다
        vt.set_value(0)
        self.play(vt.set_value, 2, rate_func=linear, run_time=3)
        dot.remove_updater(update_dot)

        self.wait()

        self.cos_dot = dot

    def draw_sine(self):
        max_len = 5

        #origin_point:원점, starting_point:그래프 시작점, curve_len:그래프의 길이
        def get_sine_graph(op, sp, curve_len):
            t = np.arange(0,2*np.pi,0.1) # 0~2pi까지 0.1간격
            dt = curve_len / len(t)
            y_t = np.sin(t)
            g = VGroup(Line(sp,sp, color=YELLOW))
            for i in range(0, len(t)):
                end_p = g[-1].get_end()
                px = end_p[0] + dt
                py = op[1] + y_t[i]
                new_line = Line(end_p, xy(px,py), color=YELLOW)
                g.add(new_line)
            return g

        ori = self.ori

        sin_t = tex(r"\sin \theta",color=YELLOW).move_to(xy(-2.25, 3.2))
        graph_start_pos = ori
        sin_graph = get_sine_graph(ori, graph_start_pos, max_len )
        self.add(sin_graph, sin_t)

        vt = ValueTracker(0)

        #1. dot가 사인 그래프를 따라서 한번 왔다 갔다
        def update_dot(mob):
            alpha = vt.get_value() % 1.0
            subs = sin_graph.submobjects
            len_subs = len(subs)
            if len_subs == 0 : return

            pos = int(alpha * len_subs)
            mob.move_to(subs[pos])

        dot = Dot(color=YELLOW).move_to(graph_start_pos)
        self.add(dot)
        dot.add_updater(update_dot)

        self.play(vt.set_value, 1, rate_func=there_and_back, run_time=4)

        #2. 사인그래프를 shrink
        def update_sin_graph(mob):
            # vt:   0   0.5   1
            # size: 0   2.5  5(=max_len)
            tgt_size = vt.get_value() * max_len
            new_graph = get_sine_graph(ori, graph_start_pos, tgt_size)

            mob.become(new_graph)

        sin_graph.add_updater(update_sin_graph)
        vt.set_value(1)

        self.remove(sin_t)
        self.play(vt.set_value, 0, rate_func=linear, run_time=4)
        sin_graph.remove_updater(update_sin_graph)

        #3. 전부 shrink된다음에 왔다 갔다
        vt.set_value(0)
        self.play(vt.set_value, 2, rate_func=linear, run_time=3)
        dot.remove_updater(update_dot)

        self.wait()
        self.sin_dot = dot

    def draw_circle(self):
        ori = self.ori
        cos_dot = self.cos_dot
        sin_dot = self.sin_dot
        cf = self.camera_frame

        #1. frame 확대
        self.play(
            cf.move_to, ori,
            cf.scale,0.5,
            run_time=2,
        )

        #2.1 text
        cos_t = tex(r"\cos \theta").scale(0.8).move_to(cos_dot).shift(UP*0.3)
        sin_t = tex(r"\sin \theta").scale(0.8).move_to(sin_dot).shift(UP*0.3)
        self.add(cos_t, sin_t)

        #2.2 (dot+tex)만 move
        left, right = xy(-5,2), xy(3,2)
        top, bottom = xy(-4,3), xy(-4,1)

        circle = Circle(radius=1, color=RED).move_to(ori)
        circle_dot = Dot(radius=0,color=RED).move_to(right)

        vt = ValueTracker(0)
        def update_circle_dot(mob):
            alpha = vt.get_value() % 1.0
            mob.move_to(circle.point_from_proportion(alpha))

        def update_cos_dot(mob):
            p = xy(circle_dot.get_center()[0], 2)
            mob.move_to(p)

        def update_sin_dot(mob):
            p = xy(-4, circle_dot.get_center()[1])
            mob.move_to(p)

        def update_cos_t(mob):
            mob.move_to(cos_dot).shift(UP*0.3)

        def update_sin_t(mob):
            mob.move_to(sin_dot).shift(UP*0.3)

        circle_dot.add_updater(update_circle_dot)
        cos_dot.add_updater(update_cos_dot)
        sin_dot.add_updater(update_sin_dot)
        cos_t.add_updater(update_cos_t)
        sin_t.add_updater(update_sin_t)

        self.add(circle_dot)
        self.play(vt.set_value, 2, rate_func=linear, run_time=4)

        #3. 원그림
        circle_group = VGroup(Line(circle_dot.get_center(), circle_dot.get_center(), color=RED))
        cos_line = Line(cos_dot.get_center(), circle_dot.get_center(), color=WHITE)
        sin_line = Line(sin_dot.get_center(), circle_dot.get_center(), color=YELLOW)

        self.add(circle_group, cos_line, sin_line)

        def update_circle_group(mob):
            g = mob.copy()
            last_pos = mob[-1].get_end()
            new_line = Line(last_pos, circle_dot.get_center(), color=RED)
            g.add(new_line)
            mob.become(g)

        def update_cos_line(mob):
            new_line = Line(cos_dot.get_center(), circle_dot.get_center(), color=WHITE)
            mob.become(new_line)

        def update_sin_line(mob):
            new_line = Line(sin_dot.get_center(), circle_dot.get_center(), color=YELLOW)
            mob.become(new_line)

        circle_group.add_updater(update_circle_group)
        cos_line.add_updater(update_cos_line)
        sin_line.add_updater(update_sin_line)

        vt.set_value(0)
        self.play(vt.set_value, 0.37, rate_func=linear, run_time=4)
        self.wait()
        self.play(vt.set_value, 1, rate_func=linear, run_time=5)

        self.wait()
        vt.set_value(0)
        self.play(vt.set_value, 1, rate_func=linear, run_time=4)