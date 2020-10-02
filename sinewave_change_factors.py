from manimlib.imports import *

class Amplitude_Change(Scene):
    def construct(self):
        self.draw_axis()
        self.draw_wave_changing_amp()
        self.wait()

    def draw_axis(self):
        MIN_X, MAX_X = -6, 6
        MIN_Y, MAX_Y = -3,3
        #1. axis
        x_start = np.array([MIN_X, 0, 0])
        x_end = np.array([MAX_X, 0, 0])

        y_start = np.array([-2, MIN_Y, 0])
        y_end = np.array([-2, MAX_Y, 0])

        x_axis = Line(x_start, x_end, color=BLUE, stroke_width=5)
        y_axis = Line(y_start, y_end, color=BLUE, stroke_width=5)

        self.add(x_axis, y_axis)

        # 2. labels
        x_labels = [
            TexMobject(r"-\pi"),
            TexMobject(r"-\frac {\pi} {2}"), TexMobject(r"0"),
            TexMobject(r"\frac {\pi} {2}"), TexMobject(r"\pi"),
            TexMobject(r"\frac {3 \pi} {2}"), TexMobject(r"2 \pi"),
            TexMobject(r"\frac {5 \pi} {2}"), TexMobject(r"3 \pi} "),
            TexMobject(r"\frac {7 \pi} {2}"),
        ]

        y_labels =[
            TexMobject(r"-2"),TexMobject(r"-1"),TexMobject(r"0"),
            TexMobject(r"1"), TexMobject(r"2"),
        ]

        #i: 0   1   2 3 4
        #x:-4  5
        for i in range(len(x_labels)):
            x_labels[i].scale(0.6)
            x_labels[i].next_to(np.array([i-4, 0, 0]), DOWN)
            self.add(x_labels[i])
        x_labels[2].shift(RIGHT*0.1) #zero label

        #i: 0   1  2 ...
        #y:-2  -1  0
        for i in range(len(y_labels)):
            if i == 2: continue
            y_labels[i].scale(0.6)
            y_labels[i].next_to(np.array([-2, i-2, 0]), LEFT)
            self.add(y_labels[i])

        #3. grid
        def get_line(x1,y1,x2,y2):
            return Line(np.array([x1,y1,0]), np.array([x2,y2,0]), stroke_color=BLUE_D, stroke_width=2,stroke_opacity=1)

        def get_s_line(x1,y1,x2,y2): #small grid
            return Line(np.array([x1, y1, 0]), np.array([x2, y2, 0]), stroke_color=BLUE_D, stroke_width=1,
                        stroke_opacity=0.7)

        x1, y1, x2, y2 = MIN_X, MAX_Y, MAX_X, MIN_Y
        v_lines = [get_line(x,y1,x,y2) for x in range(MIN_X,MAX_X+1)]
        h_lines = [get_line(x1,y,x2,y) for y in range(MIN_Y,MAX_Y+1)]
        self.add(*v_lines, *h_lines)

        sv_lines = [get_s_line(x,y1,x,y2) for x in np.arange(MIN_X+0.5,MAX_X,1)]
        sh_lines = [get_s_line(x1,y,x2,y) for y in np.arange(MIN_Y+0.5,MAX_Y+1)]
        self.add(*sv_lines, *sh_lines)

        self.MIN_X, self.MAX_X  = MIN_X, MAX_X
        self.MIN_Y, self.MAX_Y = MIN_Y,  MAX_Y

    def draw_wave_changing_amp(self):
        def get_wave(amp):
            return FunctionGraph(
                lambda t: amp * np.sin(t * PI / 2),
                x_min=self.MIN_X,
                x_max=self.MAX_X,
            )

        wave = get_wave(1)

        text = TextMobject("Amplitude: ", color=YELLOW)
        text.next_to(np.array([self.MIN_X, self.MAX_Y,0]), UP, aligned_edge=LEFT)

        num = DecimalNumber(1.0, num_decimal_places=2)
        num.next_to(text, RIGHT)

        self.add(wave, text, num)

        # ani
        vt = ValueTracker(10)

        def update_wave(mob):
            new_wave = get_wave(vt.get_value() / 10.0)
            mob.become(new_wave)

        def update_num(mob):
            num.set_value(vt.get_value() / 10.0)

        wave.add_updater(update_wave)
        num.add_updater(update_num)

        self.play(vt.set_value, 25, rate_func=linear, run_time=5)
        self.play(vt.set_value, 5, rate_func=linear, run_time=5)
        self.play(vt.set_value, 10, rate_func=linear, run_time=3)


class Phase_Change(Scene):
    def construct(self):
        self.draw_axis()
        self.draw_wave_changing_phase()
        self.wait()

    def draw_axis(self):
        MIN_X, MAX_X = -6, 6
        MIN_Y, MAX_Y = -3, 3
        # 1. axis
        x_start = np.array([MIN_X, 0, 0])
        x_end = np.array([MAX_X, 0, 0])

        y_start = np.array([-2, MIN_Y, 0])
        y_end = np.array([-2, MAX_Y, 0])

        x_axis = Line(x_start, x_end, color=BLUE, stroke_width=5)
        y_axis = Line(y_start, y_end, color=BLUE, stroke_width=5)

        self.add(x_axis, y_axis)

        # 2. labels
        x_labels = [
            TexMobject(r"-\pi"),
            TexMobject(r"-\frac {\pi} {2}"), TexMobject(r"0"),
            TexMobject(r"\frac {\pi} {2}"), TexMobject(r"\pi"),
            TexMobject(r"\frac {3 \pi} {2}"), TexMobject(r"2 \pi"),
            TexMobject(r"\frac {5 \pi} {2}"), TexMobject(r"3 \pi} "),
            TexMobject(r"\frac {7 \pi} {2}"),
        ]

        y_labels = [
            TexMobject(r"-2"), TexMobject(r"-1"), TexMobject(r"0"),
            TexMobject(r"1"), TexMobject(r"2"),
        ]

        # i: 0   1   2 3 4
        # x:-4  5
        for i in range(len(x_labels)):
            x_labels[i].scale(0.6)
            x_labels[i].next_to(np.array([i - 4, 0, 0]), DOWN)
            self.add(x_labels[i])
        x_labels[2].shift(RIGHT * 0.1)  # zero label

        # i: 0   1  2 ...
        # y:-2  -1  0
        for i in range(len(y_labels)):
            if i == 2: continue
            y_labels[i].scale(0.6)
            y_labels[i].next_to(np.array([-2, i - 2, 0]), LEFT)
            self.add(y_labels[i])

        # 3. grid
        def get_line(x1, y1, x2, y2):
            return Line(np.array([x1, y1, 0]), np.array([x2, y2, 0]), stroke_color=BLUE_D, stroke_width=2,
                        stroke_opacity=1)

        def get_s_line(x1, y1, x2, y2):  # small grid
            return Line(np.array([x1, y1, 0]), np.array([x2, y2, 0]), stroke_color=BLUE_D, stroke_width=1,
                        stroke_opacity=0.7)

        x1, y1, x2, y2 = MIN_X, MAX_Y, MAX_X, MIN_Y
        v_lines = [get_line(x, y1, x, y2) for x in range(MIN_X, MAX_X + 1)]
        h_lines = [get_line(x1, y, x2, y) for y in range(MIN_Y, MAX_Y + 1)]
        self.add(*v_lines, *h_lines)

        sv_lines = [get_s_line(x, y1, x, y2) for x in np.arange(MIN_X + 0.5, MAX_X, 1)]
        sh_lines = [get_s_line(x1, y, x2, y) for y in np.arange(MIN_Y + 0.5, MAX_Y + 1)]
        self.add(*sv_lines, *sh_lines)

        self.MIN_X, self.MAX_X = MIN_X, MAX_X
        self.MIN_Y, self.MAX_Y = MIN_Y, MAX_Y
        self.ORIGIN = np.array([-2,0,0])

    def draw_wave_changing_phase(self):
        def get_wave(phase): # unit: degree
            return FunctionGraph(
                lambda t: np.sin(t * PI / 2 - phase * PI / 180),
                x_min=self.MIN_X,
                x_max=self.MAX_X,
            )

        wave = get_wave(0) # 0도

        text = TextMobject("Phase: ", color=YELLOW)
        text.next_to(np.array([self.MIN_X, self.MAX_Y, 0]), UP, aligned_edge=LEFT)

        num = DecimalNumber(1, num_decimal_places=0)
        num.next_to(text, RIGHT)

        dot = Dot(color=RED)
        dot.move_to(self.ORIGIN)

        self.add(wave, dot, text, num)

        # ani
        vt = ValueTracker(0)

        def update_wave(mob):
            new_wave = get_wave(vt.get_value() )
            mob.become(new_wave)

        def update_num(mob):
            num.set_value(vt.get_value())

        # phase: 0 1 2 ... 90...180
        # dot  : 0         1    2
        # x    : -2        -1   0
        def update_dot(mob):
            val = vt.get_value()
            dot.move_to(np.array([val/90.0 - 2,0,0]))

        wave.add_updater(update_wave)
        num.add_updater(update_num)
        dot.add_updater(update_dot)

        self.play(vt.set_value, 180, rate_func=there_and_back, run_time=10)
        self.wait()
        self.play(vt.set_value, -180, rate_func=there_and_back, run_time=10)
        self.wait()


class Frequency_Change(Scene):
    def construct(self):
        self.draw_axis()
        self.draw_wave_changing_freq()
        self.wait()

    def draw_axis(self):
        MIN_X, MAX_X = -6, 6
        MIN_Y, MAX_Y = -3,3
        #1. axis
        x_start = np.array([MIN_X, 0, 0])
        x_end = np.array([MAX_X, 0, 0])

        y_start = np.array([-2, MIN_Y, 0])
        y_end = np.array([-2, MAX_Y, 0])

        x_axis = Line(x_start, x_end, color=BLUE, stroke_width=5)
        y_axis = Line(y_start, y_end, color=BLUE, stroke_width=5)

        self.add(x_axis, y_axis)

        # 2. labels
        x_labels = [
            TexMobject(r"-\pi"),
            TexMobject(r"-\frac {\pi} {2}"), TexMobject(r"0"),
            TexMobject(r"\frac {\pi} {2}"), TexMobject(r"\pi"),
            TexMobject(r"\frac {3 \pi} {2}"), TexMobject(r"2 \pi"),
            TexMobject(r"\frac {5 \pi} {2}"), TexMobject(r"3 \pi} "),
            TexMobject(r"\frac {7 \pi} {2}"),
        ]

        y_labels =[
            TexMobject(r"-2"),TexMobject(r"-1"),TexMobject(r"0"),
            TexMobject(r"1"), TexMobject(r"2"),
        ]

        #i: 0   1   2 3 4
        #x:-4  5
        for i in range(len(x_labels)):
            x_labels[i].scale(0.6)
            x_labels[i].next_to(np.array([i-4, 0, 0]), DOWN)
            self.add(x_labels[i])
        x_labels[2].shift(RIGHT*0.1) #zero label

        #i: 0   1  2 ...
        #y:-2  -1  0
        for i in range(len(y_labels)):
            if i == 2: continue
            y_labels[i].scale(0.6)
            y_labels[i].next_to(np.array([-2, i-2, 0]), LEFT)
            self.add(y_labels[i])

        #3. grid
        def get_line(x1,y1,x2,y2):
            return Line(np.array([x1,y1,0]), np.array([x2,y2,0]), stroke_color=BLUE_D, stroke_width=2,stroke_opacity=1)

        def get_s_line(x1,y1,x2,y2): #small grid
            return Line(np.array([x1, y1, 0]), np.array([x2, y2, 0]), stroke_color=BLUE_D, stroke_width=1,
                        stroke_opacity=0.7)

        x1, y1, x2, y2 = MIN_X, MAX_Y, MAX_X, MIN_Y
        v_lines = [get_line(x,y1,x,y2) for x in range(MIN_X,MAX_X+1)]
        h_lines = [get_line(x1,y,x2,y) for y in range(MIN_Y,MAX_Y+1)]
        self.add(*v_lines, *h_lines)

        sv_lines = [get_s_line(x,y1,x,y2) for x in np.arange(MIN_X+0.5,MAX_X,1)]
        sh_lines = [get_s_line(x1,y,x2,y) for y in np.arange(MIN_Y+0.5,MAX_Y+1)]
        self.add(*sv_lines, *sh_lines)

        self.MIN_X, self.MAX_X  = MIN_X, MAX_X
        self.MIN_Y, self.MAX_Y = MIN_Y,  MAX_Y

    def draw_wave_changing_freq(self):
        def get_wave(freq):
            return FunctionGraph(
                lambda t: np.sin(freq * t * PI / 2),
                x_min=self.MIN_X,
                x_max=self.MAX_X,
            )

        wave = get_wave(1)

        text = TextMobject("Frequency: ", color=YELLOW)
        text.next_to(np.array([self.MIN_X, self.MAX_Y,0]), UP, aligned_edge=LEFT)

        num = DecimalNumber(1, num_decimal_places=0)
        num.next_to(text, RIGHT)

        self.add(wave, text, num)

        # ani
        vt = ValueTracker(1)

        def update_wave(mob):
            new_wave = get_wave(vt.get_value() )
            mob.become(new_wave)

        def update_num(mob):
            num.set_value(vt.get_value() )

        wave.add_updater(update_wave)
        num.add_updater(update_num)

        self.play(vt.set_value, 20, rate_func=there_and_back, run_time=10)
        self.wait()



