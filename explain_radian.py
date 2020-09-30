from manimlib.imports import *

class ExplainRadian(Scene):
    def construct(self):
        R = 2
        A = np.array([R,0,0])
        #A = circle.point_from_proportion(0)

        #1. draw circle
        circle = Circle(radius=R)
        o_dot = Dot(color=BLUE).move_to(circle.get_center())
        o_text = TextMobject("O").next_to(circle.get_center(),DOWN)
        self.add(circle, o_dot, o_text)

        #2. draw r
        r_line = Line(circle.get_center(), circle.point_from_proportion(0), color=BLUE)
        a_dot = Dot(color=BLUE).move_to(A)
        a_text = TextMobject("A").next_to(A, RIGHT)
        r_text = TextMobject("r", color=BLUE).next_to(r_line, DOWN)
        self.play(
            LaggedStart(
                ShowCreation(r_line),
                ShowCreation(a_dot),
                FadeIn(a_text),
                ShowCreation(r_text),
            ),
            run_time=2,
        )

        #3. make another r line
        r_line2 = r_line.copy().next_to(circle.get_top(),UP)
        line_text = TextMobject("a string equal to radius r").next_to(r_line2, UP)
        self.play(
            LaggedStart(
                ShowCreation(line_text),
                ShowCreation(r_line2),
            ),
            run_time=3,
        )
        self.play(r_line2.move_to, r_line.get_center(), run_time=1.5)
        self.wait(0.5)
        target = r_line2.generate_target()
        target.shift(R * RIGHT)
        self.play(
            LaggedStart(
                FadeOut(line_text),
                MoveToTarget(r_line2),
            ),
            run_time=2,
        )
        self.wait()

        #4. draw arc
        B = circle.point_from_proportion(1 / (2 * PI))
        arc = ArcBetweenPoints(A,B, angle=TAU/6, color=BLUE)
        b_dot = Dot(color=BLUE).move_to(B)
        b_text = TextMobject("B").next_to(B,RIGHT).shift(UP*0.1)
        r2_text = r_text.copy().next_to(arc,RIGHT, buff=0.1).shift(UP*0.05)
        self.play(
            LaggedStart(
                Transform(r_line2, arc),
                ShowCreation(b_dot),
                ShowCreation(b_text),
                ShowCreation(r2_text),
            ),
            run_time=4,
        )
        self.wait()

        #5 draw BO line
        bo_line = Line(B, ORIGIN, color=BLUE)
        r3_text = r_text.copy().next_to(bo_line, LEFT).shift(RIGHT*0.4)
        self.play(
            LaggedStart(
                ShowCreation(bo_line),
                ShowCreation(r3_text),
            ),
            run_time=2,
        )

        #6. radian
        theta = ArcBetweenPoints(r_line.point_from_proportion(0.2), bo_line.point_from_proportion(1-0.2),color=YELLOW)
        radian_text = TextMobject("1 radian", color=YELLOW).scale(0.7).next_to(theta,RIGHT).shift(LEFT*0.15+UP*0.1)
        self.play(
            LaggedStart(
                ShowCreation(theta),
                ShowCreation(radian_text),
            ),
            run_time=2,
        )
        self.wait()
