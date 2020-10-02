from manimlib.imports import *

class PhaseChange(Scene):
    def construct(self):
        self.draw_axis()
        self.draw_grid()

        self.draw_wave()
        self.wait()

    def get_axis(self, max_y=1):
        g = VGroup()
        min_x = -6
        max_x = 6

        def xy(x, y):
            return np.array([x, y, 0])

        def tex(str, color=WHITE):
            return TexMobject(str,color=color).scale(0.6)

        def get_line(s,e):
            return Line(s,e , color=BLUE, stroke_width=5)

        x_axis = get_line(xy(min_x,0), xy(max_x,0))
        g.add(x_axis)

        x_labels = [tex("0.5", color=BLUE), tex("1", color=BLUE)]

        # i: 0   1
        # x: 0   6
        for i in range(len(x_labels)):
            x_labels[i].next_to(xy(6*i,0), DOWN)
            g.add(x_labels[i])

        # max_y: 1 -> 0.5 ~ -0.5
        #        2 -> 1 ~ -1
        y_axis = get_line(xy(min_x, max_y/2),xy(min_x,-max_y/2) )
        g.add(y_axis)

        y_labels = []
        for i in range(max_y, -max_y-1, -1):
            y_labels.append(tex(str(i)))

        #i: 0    1   2    or  0   1   2   3   4
        #y: 0.5  0  -0.5      1  0.5 0 -0.5 -1
        for i in range(len(y_labels)):
            y_labels[i].next_to(xy(-6, -0.5*(i-max_y)), LEFT)
            g.add(y_labels[i])

        self.min_x = min_x
        self.max_x = max_x
        return g

    def draw_grid(self):
        def get_s_line(x1, y1, x2, y2):  # small grid
            return Line(np.array([x1, y1, 0]), np.array([x2, y2, 0]), stroke_color=BLUE_D, stroke_width=1,
                        stroke_opacity=0.7)
        y1, y2 = 2.5, -2.5
        sv_lines = [get_s_line(x, y1, x, y2) for x in np.arange(self.min_x , self.max_x+1, 1)]

        self.add(*sv_lines)

    def draw_axis(self):
        def tex(str):
            return TexMobject(str, ).scale(0.8)

        eq1 = tex(r"y_1=\sin 2\pi \cdot 2 \cdot t")
        eq2 = tex(r"y_1=\sin (2\pi \cdot 2 \cdot t - \phi), \phi = ")
        eq3 = tex(r"y = y_1 + y_2")

        phi_num = Integer(0, color=RED)

        axis1 = self.get_axis(1)
        axis1.shift(UP*2)
        eq1.next_to(axis1,UP,aligned_edge=LEFT, buff=0).shift(RIGHT*0.8+DOWN*0.1)


        axis2 = self.get_axis(1)
        axis2.shift(UP*0.5)
        eq2.next_to(axis2, UP, aligned_edge=LEFT, buff=0).shift(RIGHT * 0.8+DOWN*0.1)
        phi_num.next_to(eq2, RIGHT)

        axis3 = self.get_axis(2)
        axis3.shift(DOWN*1.5)
        eq3.next_to(axis3, UP, aligned_edge=LEFT, buff=0).shift(RIGHT * 0.8+DOWN*0.1)

        self.add(axis1, axis2, axis3)
        self.add(eq1, eq2, phi_num, eq3)

        self.phi_num = phi_num

    def draw_wave(self):
        vt = ValueTracker(0)

        def get_wave(A=1, f=2, phi=0):  # phi: degree
            # x: -6 ...  0 ... 6
            # t: 0  ..  0.5 .. 1
            # t = x/12 + 0.5
            return FunctionGraph(
                lambda x: A/2*np.sin(2 * PI * f * (x / 12 + 0.5) - phi * PI / 180),
                # lambda t : np.sin(t),
                x_min=self.min_x,
                x_max=self.max_x,
            )

        def get_sum_cal(A=1,f=2):
            phi = vt.get_value()
            return FunctionGraph(
                lambda x: (A / 2 * np.sin(2 * PI * f * (x / 12 + 0.5))) +
                          (A / 2 * np.sin(2 * PI * f * (x / 12 + 0.5)-(phi * PI / 180))),
                # lambda t : np.sin(t),
                x_min=self.min_x,
                x_max=self.max_x,
            )

        wave1 = get_wave(1, 2, 0).shift(UP * 2)
        wave2 = get_wave(1, 2, 0).shift(UP * 0.5)
        wave3 = get_sum_cal(1, 2).shift(DOWN * 1.5)
        self.add(wave1, wave2, wave3)

        #ani
        def update_wave2(mob):
            new_wave = get_wave(phi=vt.get_value()).shift(UP * 0.5)
            mob.become(new_wave)

        def update_wave3(mob):
            new_wave = get_sum_cal(1, 2).shift(DOWN * 1.5)
            mob.become(new_wave)

        def update_phi(mob):
            mob.set_value(vt.get_value())

        wave2.add_updater(update_wave2)
        wave3.add_updater(update_wave3)
        self.phi_num.add_updater(update_phi)

        self.play(vt.set_value, 360, rate_func=linear, run_time=10)
        self.wait()