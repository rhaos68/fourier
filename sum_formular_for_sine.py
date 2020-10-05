from manimlib.imports import *
from src.jeff.info_graph import InfoGraph

# projection to y
def projection(x,y):
    # (y/np.linalg.norm(y)) * (np.dot(x,y)/np.linalg.norm(y))
    return y * np.dot(x, y) / np.dot(y, y)

def unit_vector(x):
    return x / np.linalg.norm(x)

# 점x에서, 직선AB와 평행한 단위 벡터
def parallel(x,a,b,length=1):
    v = np.subtract(b,a)
    u = unit_vector(v) * length
    y = np.add(x,u)
    return y

def distance(a,b):
    return np.linalg.norm(a - b)

def sText(str, color=WHITE):
    return Text(str, font='굴림', size=0.3, stroke_width=0, color=color)

def mText(str, color=WHITE):
    return Text(str, font='굴림', size=0.7, stroke_width=0, color=color)

def lText(str, color=WHITE):
    return Text(str, font='굴림', size=1, stroke_width=0, color=color)


def mTex(str, color=WHITE):
    return TexMobject(str, color=color).scale(0.8)

def sTex(str, color=WHITE):
    return TexMobject(str, color=color).scale(0.6)


def sTextM(str, color=WHITE):
    return TextMobject(str, color=color).scale(0.6)

def mTextM(str, color=WHITE):
    return TextMobject(str, color=color).scale(0.8)

def xy(x,y):
    return np.array([x,y,0])

def get_triangle(p1,p2,p3):
    return Polygon(p1,p2,p3)

class LawOfSineSum(MovingCameraScene):
    def addInfoGraph(self):
        logo = InfoGraph().scale(1.3)
        logo.to_corner(DR).shift(UP*0.5+RIGHT*0.1)
        self.add(logo)

    def construct(self):
        self.addInfoGraph()

        self.s1()
        self.s2()
        self.s3()
        self.s4()
        self.s5()
        self.s6()
        self.s7()
        self.s8()

    def s1(self):
        # 삼각함수의 덧셈정리 중 사인함수의 덧셈에 대해 알아보겠습니다.
        # t1 = mText("삼각함수의 덧셈정리중 사인함수의 덧셈정리")
        t1 = lText("삼각함수의 덧셈정리중 사인함수의 덧셈정리", color=BLUE)
        t1.to_edge(UP).to_edge(LEFT).shift(RIGHT)

        t2 = mTex(r"\sin (\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta")
        t2.next_to(t1, DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)

        self.wait()
        self.add_sound(r"res\sound\s1\01_삼각함수의_덧셈정리_중_싸인함수의_덧셈에_대해_알아보겠습니다.mp3")
        self.play(
            LaggedStart(
                ShowCreation(t1),
                ShowCreation(t2),
            ),
            run_time=3,
        )
        self.wait(3)

        # 알파 플러스 베타에 대한 싸인값을, 알파와 베타의 각 싸인 값, 코싸인 값으로 나타내보는 것이 덧셈정리입니다.
        t3 = mTextM(r"$\rightarrow \sin (\alpha + \beta)$ 를 $\sin \alpha, \sin \beta, \cos \alpha, \cos \beta$로 표현 ")
        t3.next_to(t2,DOWN, aligned_edge=LEFT)

        self.add_sound(r"res\sound\s1\02_알파_플러스_베타에_대한_싸인값을_알파와_베타의_각_싸인_값_코싸인_값으로_나타내보는_.mp3")
        self.play(ShowCreation(t3), run_time=4)

        self.wait(6)

        self.to_be_removed = VGroup(t3,)

    def s2(self):
        # 먼저 기본으로 알아야할 것은, 삼각형에서 싸인값 코싸인값이겠죠
        p1,p2,p3 = xy(-5,-2),xy(-1,-2),xy(-1,1)
        a,b,c = Line(p1,p2), Line(p2,p3), Line(p3,p1)
        tri = VGroup(a,b,c)

        x,y,d=-1,-2,0.3
        elbow = VGroup(Line(xy(x,y+d),xy(x-d,y+d)),Line(xy(x-d,y+d),xy(x-d,y)))
        arc = Arc(arc_center=p1, start_angle=0, angle=np.arcsin(3/5))
        theta = mTex(r"\theta").next_to(arc, RIGHT).shift(LEFT*0.1+UP*0.1)

        at = mTex("a").next_to(a,DOWN)
        bt = mTex("b").next_to(b, RIGHT)
        ct = mTex("c").next_to(c.point_from_proportion(0.5), UP)
        line_text = VGroup(at,bt,ct)

        h_at = mText("밑변(가로)", color=RED).next_to(at,DOWN)
        h_bt = mText("높이(세로)", color=RED).next_to(bt, DOWN,aligned_edge=LEFT)
        h_ct = mText("빗변", color=RED).next_to(ct, DOWN, aligned_edge=RIGHT).shift(LEFT*0.6)
        line_h_text = VGroup(h_at, h_bt, h_ct)

        self.add_sound(r"res\sound\s1\03_먼저_기본으로_알아야할_것은_삼각형에서_싸인값_코싸인값이겠죠.mp3")
        self.play( #5
            LaggedStart(
                ShowCreation(tri),
                ShowCreation(elbow),
                ShowCreation(arc),
                ShowCreation(theta),
                ShowCreation(line_text),
                ShowCreation(line_h_text),
            ),
            run_time=3,
        )
        self.wait(1.5)

        # 직각 삼각형이  있을 때, 각 쎄타에 대한 싸인 값은, 빗변분의 세로이고,
        # 코싸인값은 빗변분의 가로입니다.
        t1 = mTex(r"\sin \theta = ").next_to(bt,RIGHT).shift(RIGHT*2+UP)
        t2 = mTex(r"\frac {b}{c}").next_to(t1)

        t3 = mTex(r"\cos \theta = ").next_to(t1,DOWN, aligned_edge=LEFT).shift(DOWN)
        t4 = mTex(r"\frac {a}{c}").next_to(t3)

        self.add_sound(r"res\sound\s1\04_직각_삼각형이__있을_때_각_쎄타에_대한_싸인_값은_빗변분의_세로이고_코싸인값은_빗변.mp3")
        self.play(ShowCreation(t1), run_time=2)
        self.play(TransformFromCopy(VGroup(ct,bt),t2),run_time=2)
        self.wait()

        self.play(ShowCreation(t3), run_time=2)
        self.play(TransformFromCopy(VGroup(ct, at), t4), run_time=2)
        self.wait(2)

        # 만약 빗변이 1이라고 하면, 싸인 쎄타는 세로이고, 코싸인 세타는 가로값이 됩니다.
        # 머리에 세겨 둡시다.

        self.add_sound(r"res\sound\s1\05_만약_빗변이_1이라고_하면_싸인_쎄타는_세로이고_코싸인_세타는_가로값이_됩니다_머리에.mp3")

        t_1 = mTex("1", color=YELLOW).move_to(ct)
        t_sin = mTex(r"= \sin \theta",color=YELLOW).next_to(bt,RIGHT)
        t_cos = mTex(r"= \cos \theta", color=YELLOW).next_to(at, RIGHT)

        self.play(
            LaggedStart(
                FadeIn(c),
                Transform(ct,t_1),
            ),
            run_time=1,
        )

        self.play(
            LaggedStart(
                FadeIn(b),
                ShowCreation(t_sin),
            ), run_time=1.5,
        )

        self.play( #15
            LaggedStart(
                FadeIn(a),
                ShowCreation(t_cos),
            ), run_time=1.5,
        )

        self.play(
            LaggedStart(
                FadeIn(t_sin), FadeIn(t_cos),
            ),run_time=1.5,
        )

        self.wait(3.5)

        self.to_be_removed.add(tri, elbow, arc,theta, line_text, line_h_text)
        self.to_be_removed.add(t1,t2,t3,t4)
        self.to_be_removed.add(t_1, t_sin, t_cos)


    def s3(self):
        # 이제 정리를 유도해 보겠습니다.
        self.add_sound(r"res\sound\s2\01_이제_정리를_유도해_보겠습니다.mp3")
        self.play(FadeOut(self.to_be_removed),run_time=2)
        self.wait(1)

        # 먼저, 반지름이 1인 원을 그려보겠습니다.
        pO = xy(-5,-2)
        circle = Circle(radius=1,).move_to(pO)
        origin_dot = Dot(color=RED).move_to(circle.get_center())

        self.add_sound(r"res\sound\s2\01_먼저_반지름이_1인_원을_그려보겠습니다.mp3")
        self.play(
            LaggedStart(
                ShowCreation(circle),
                ShowCreation(origin_dot)
            ),run_time=1,
        )

        self.play(circle.scale,4, run_time=2)
        line_x = Line(circle.get_left(), circle.get_right(), color=RED, stroke_width=2)
        line_y = Line(circle.get_bottom(),circle.get_top(), color=RED, stroke_width=2)
        t_1 = mTex("1", color=RED).next_to(line_y.point_from_proportion(0.75), LEFT)
        self.play(
            LaggedStart(
                ShowCreation(line_x),
                ShowCreation(line_y),
                ShowCreation(t_1),
            ),run_time=0.5,
        )
        self.wait()

        # 각각의 각이, 알파와 베타가 되도록 점을 찍어보면,
        pA = circle.point_from_proportion(0.25/3)
        pB = circle.point_from_proportion(0.25*2/3)
        dotA = Dot().move_to(pA)
        dotB = Dot().move_to(pB)
        tA = mTex("A").next_to(dotA, RIGHT).shift(LEFT*0.1)
        tB = mTex("B").next_to(dotB, RIGHT).shift(LEFT*0.25,UP*0.25)

        lineX = Line(pO, circle.get_right())
        lineOA = Line(pO, pA)
        lineOB = Line(pO, pB)

        arcA = ArcBetweenPoints(lineX.point_from_proportion(0.2),lineOA.point_from_proportion(0.2))
        arcB = ArcBetweenPoints(lineOA.point_from_proportion(0.2), lineOB.point_from_proportion(0.2))
        alphaT = sTex(r"\alpha").next_to(arcA.point_from_proportion(0.5), RIGHT)
        betaT = sTex(r"\beta").next_to(arcB.point_from_proportion(0.5), RIGHT).shift(LEFT*0.1,UP*0.2)

        self.add_sound(r"res\sound\s2\02_각각의_각이_알파와_베타가_되도록_점을_찍어보면.mp3")
        self.play( #24
            LaggedStart(
                ShowCreation(dotA),
                ShowCreation(tA),
                ShowCreation(lineOA),
                ShowCreation(arcA),
                ShowCreation(alphaT),

                ShowCreation(dotB),
                ShowCreation(tB),
                ShowCreation(lineOB),
                ShowCreation(arcB),
                ShowCreation(betaT),
            ),run_time=4,
        )
        self.wait()

        # 알파에 대한 삼각형은 이렇게,
        pP = xy(pA[0],pO[1])
        lineAP = Line(pA,pP)
        linePO = Line(pP,pO)
        pPP = xy(linePO.point_from_proportion(0.1)[0],lineAP.point_from_proportion(0.85)[1] )
        elbowP = VGroup(
            Line(lineAP.point_from_proportion(0.85), pPP),
            Line(pPP, linePO.point_from_proportion(0.1)),
        )
        triA = VGroup(lineAP, linePO, lineOA, elbowP)

        self.add_sound(r"res\sound\s2\03_알파에_대한_삼각형은_이렇게.mp3")
        self.play(
            Succession(
                ShowCreation(lineAP),
                ShowCreation(linePO),
                ShowCreation(lineOA),
                ShowCreation(elbowP),
            ),run_time=1.5,
        )
        self.play(WiggleOutThenIn(triA), run_time=4)
        self.wait()

        # 베타에 대한 삼각형은 이렇게 되고,
        pQ = pO + projection(lineOB.get_vector(), lineOA.get_vector())
        lineBQ = Line(pB, pQ)
        lineQO = Line(pQ, pO)

        pY = lineBQ.point_from_proportion(0.85)
        dQY = distance(pQ,pY)

        pZ = parallel(pY,pQ,pO,length=dQY)
        pX = parallel(pZ, pB, pQ, length=dQY)
        elbowQ = VGroup(
            Line(pY,pZ), Line(pZ,pX),
        )
        triB = VGroup(lineBQ, lineQO, lineOB, elbowQ)

        self.add_sound(r"res\sound\s2\04_베타에_대한_삼각형은_이렇게_되고.mp3")
        self.play(
            Succession(
                ShowCreation(lineBQ),
                ShowCreation(lineQO),
                ShowCreation(lineOB),
                ShowCreation(elbowQ),
            ), run_time=1.5,
        )
        self.play(WiggleOutThenIn(triB), run_time=4)
        self.wait()

        # 알파 플러스 베타에 대한 삼각형은 이렇게 됩니다.
        arcAB = ArcBetweenPoints(lineX.point_from_proportion(0.1), lineOB.point_from_proportion(0.1))
        alphabetaT = sTex(r"\alpha + \beta").next_to(arcAB.get_start(),DOWN, buff=0.15)
        pR = xy(pB[0], pO[1])
        lineBR = Line(pB, pR)
        lineRO = Line(pR, pO)
        pRR = xy(lineRO.point_from_proportion(0.15)[0], lineBR.point_from_proportion(0.92)[1])
        elbowR = VGroup(
            Line(lineBR.point_from_proportion(0.92), pRR),
            Line(pRR, lineRO.point_from_proportion(0.15)),
        )
        triC = VGroup(lineBR, lineRO, lineOB, elbowR)

        self.add_sound(r"res\sound\s2\05_알파_플러스_베타에_대한_삼각형은_이렇게_됩니다.mp3")
        self.play(
            Succession(
                ShowCreation(arcAB),
                ShowCreation(alphabetaT),
                ShowCreation(lineBR),
                ShowCreation(lineRO),
                ShowCreation(lineOB),
                ShowCreation(elbowR),
            ), run_time=2.5,
        )
        self.play(WiggleOutThenIn(triC), run_time=4)
        self.wait(2)

        # 베타에 대한 삼각형에서, 빗변이 1이기에, 세로변은 싸인 베타이고, 밑 변은 코싸인 베타입니다.
        t_b1 = mTex("1",color=YELLOW).next_to(lineOB.point_from_proportion(0.5),LEFT,buff=0.1)
        t_bsin = mTex(r"\sin \beta",color=YELLOW).move_to(lineBQ.point_from_proportion(0.5))
        t_bcos = mTex(r"\cos \beta", color=YELLOW).move_to(lineQO.point_from_proportion(0.5)).rotate(12*DEGREES)
        self.add_sound(r"res\sound\s2\06_베타에_대한_삼각형에서_빗변이_1이기에_세로변은_싸인_베타이고_밑_변은_코싸인_베타입.mp3")
        self.play(WiggleOutThenIn(triB), run_time=2)
        self.play(ShowCreation(t_b1), run_time=1)
        self.wait(2)
        self.play(ShowCreation(t_bsin), run_time=1)
        self.wait(1)
        self.play(ShowCreation(t_bcos), run_time=1)

        self.wait(3)

        # 알파에 대한 삼각형에서, 세로 변은 싸인 알파, 밑 변은 코싸인 알파입니다.
        t_asin = mTex(r"\sin \alpha", color=YELLOW).move_to(lineAP.point_from_proportion(0.5))
        t_acos = mTex(r"\cos \alpha", color=YELLOW).next_to(linePO.point_from_proportion(0.5), DOWN, buff=0.1)
        self.add_sound(r"res\sound\s2\07_알파에_대한_삼각형에서_세로_변은_싸인_알파_밑_변은_코싸인_알파입니다.mp3")
        self.play(WiggleOutThenIn(triA), run_time=2)
        self.wait(1)
        self.play(ShowCreation(t_asin), run_time=1)
        self.wait(1)
        self.play(ShowCreation(t_acos), run_time=1)

        self.wait(4)

        # 알파 플러스 베타에 대한 싸인값은,
        self.add_sound(r"res\sound\s2\08_알파_플러스_베타에_대한_싸인값은.mp3")
        self.play(WiggleOutThenIn(triC), run_time=3)

        # 이 삼각형에서 세로 변 이것에 해당합니다.
        self.add_sound(r"res\sound\s2\09_이_삼각형에서_세로_변_이것에_해당합니다.mp3")
        self.play(lineBR.set_color, BLUE, run_time=2)
        self.play(WiggleOutThenIn(lineBR), run_time=2)

        self.wait(1)

        # 즉, 사인함수의 덧셈정리는, 이 세로 변 값을,
        self.add_sound(r"res\sound\s2\10_즉_사인함수의_덧셈정리는_이_세로_변_값을.mp3")
        self.wait(3)
        self.play(WiggleOutThenIn(lineBR, run_time=2))
        self.wait(0.5)

        # 싸인 베타, 코싸인 베타, 싸인 알파, 코싸인 알파을 이용해서 나타내는 것입니다.
        self.add_sound(r"res\sound\s2\11_싸인_베타_코싸인_베타_싸인_알파_코싸인_알파을_이용해서_나타내는_것입니다.mp3")
        sine_texts = VGroup(t_bsin, t_bcos, t_asin, t_acos)
        self.play(WiggleOutThenIn(sine_texts, run_time=6))

        self.wait(3)

        self.pB, self.pO, self.pQ, self.pR = pB, pO, pQ, pR
        self.lineBR =lineBR

        self.arcA = arcA
        self.alphaT = alphaT
        self.t_bcos = t_bcos
        self.t_bsin = t_bsin

        self.elbowQ = elbowQ
        self.elbowR = elbowR

    def s4(self):
        pB, pO, pQ, pR = self.pB, self.pO, self.pQ, self.pR
        lineBR = self.lineBR

        # 이 세로 변을 적당히 두 개로 나눠보겠습니다.
        pS = xy(pR[0], pQ[1])
        lineQS = Line(pQ,pS)
        lineBS = Line(pB,pS, stroke_width=6,color=GREEN)
        lineSR = Line(pS,pR, stroke_width=6,color=RED)

        self.add_sound(r"res\sound\s3\01_이_세로_변을_적당히_두_개로_나눠보겠습니다.mp3")
        self.play(WiggleOutThenIn(lineBR), run_time=3)

        self.wait(1)
        self.play(
            AnimationGroup(
                ShowCreation(lineQS),
                ShowCreation(lineBS),
                ShowCreation(lineSR),
                lag_ratio=1,
            ), run_time=2,
        )
        self.play(
            LaggedStart(
                WiggleOutThenIn(lineBS),
                WiggleOutThenIn(lineSR),
            ), run_time=2,
        )
        self.wait(0.5)

        # 이렇게 나눠서, 아래를 엑스, 윗 부분을 "와이"라 하겠습니다.
        self.add_sound(r"res\sound\s3\02_이렇게_나눠서_아래를_엑스_윗_부분을_Y라고_하겠습니다.mp3")
        self.wait(2)

        tx = mTex("x",color=RED).next_to(lineSR.point_from_proportion(0.5),RIGHT, buff=0.15)
        ty = mTex("y",color=GREEN).next_to(lineBS.point_from_proportion(0.7),RIGHT, buff=0.15)

        self.play(ShowCreation(tx))
        self.wait(0.5)
        self.play(ShowCreation(ty)) #65
        self.wait(3)

        # 이렇게 하면, 싸인 알파 플러스 베타는 엑스 더하기 와이가 됩니다.
        self.add_sound(r"res\sound\s3\03_이렇게_하면_싸인_알파_플러스_베타는_엑스_더하기_와이가_됩니다.mp3")
        t_sin_ab = TexMobject(r"\sin (\alpha + \beta) =", "x + y", color=YELLOW).scale(0.8)
        t_sin_ab.next_to(lineBS.get_start(),RIGHT).shift(RIGHT+UP*0.5)
        # t1 = mTex(r"\sin (\alpha + \beta) = x + y",color=YELLOW).next_to(lineBS.get_start(),RIGHT).shift(RIGHT+UP*0.5)
        self.play(Write(t_sin_ab), run_time=2)
        self.wait(3)


        # 이렇게 나눈것은,
        pT = xy(pQ[0], pR[1])
        lineQT = Line(pQ, pT, color=RED, stroke_width=6)
        self.add_sound(r"res\sound\s3\04_이렇게_나눈_것은.mp3")
        self.wait(2)
        self.play(ShowCreation(lineQT))

        # 엑스의 값은, 이 값과 같기에,
        self.add_sound(r"res\sound\s3\05_엑스의_값은_이_값과_같기에.mp3")
        self.play(WiggleOutThenIn(lineQT), run_time=3)
        self.wait()

        # 삼각형 이 것을 이용하겠다는 것이고,
        lineTO = Line(pT, pO, stroke_width=6, color=RED)
        lineOQ = Line(pO, pQ, stroke_width=6, color=RED)
        triX = VGroup(lineQT, lineTO, lineOQ)

        self.add_sound(r"res\sound\s3\06_삼각형_이_것을_이용하겠다는_것이고.mp3")
        self.play(ShowCreation(triX))
        self.play(WiggleOutThenIn(triX), run_time=4)
        self.wait(1)

        # y의 값은, 삼각형 이 것을 이용하기 위해서입니다.
        lineSQ = Line(pS, pQ, stroke_width=6, color=GREEN)
        lineQB = Line(pQ,pB, stroke_width=6, color=GREEN)
        triY = VGroup(lineBS, lineSQ, lineQB)

        self.add_sound(r"res\sound\s3\07_y의_값은_삼각형_이_것을_이용하기_위해서입니다.mp3")
        self.play(ShowCreation(triY))
        self.play(WiggleOutThenIn(triY), run_time=4)

        self.wait(2)

        self.triX = triX
        self.tx = tx
        self.ty = ty
        self.lineBS = lineBS
        self.lineSQ=lineSQ
        self.lineQB = lineQB

        self.t_sin_ab = t_sin_ab

    def s5(self):
        triX = self.triX
        tx = self.tx

        arcA = self.arcA
        alphaT=self.alphaT
        t_bcos=self.t_bcos

        t_bcos2 = t_bcos.copy()
        triX2 = VGroup(triX, arcA, alphaT, t_bcos2).copy()
        tx2 = tx.copy()

        # 먼저 x를 구해 볼게요.
        self.add_sound(r"res\sound\s4\01_먼저_x를_구해_볼게요.mp3")

        self.play( #79
            triX2.shift, 6 * RIGHT, run_time=4,
        )
        self.play(tx2.next_to, triX2.get_right(),{"direction":RIGHT}, run_time=2)
        self.wait(2)

        # 이 삼각형에서 빗변이 코싸인 베타, 세로변이 엑스니깐,
        self.add_sound(r"res\sound\s4\02_이_삼각형에서_빗변이_코싸인_베타_세로변이_엑스니깐.mp3")
        self.play(Indicate(triX2[3]), run_time=2)
        self.wait(1)
        self.play(Indicate(tx2), run_time=2)
        self.wait(0.5)


        # 싸인 알파는, 코싸인 베타 분의 엑스가됩니다.
        self.add_sound(r"res\sound\s4\03_싸인_알파는_코싸인_베타_분의_엑스가됩니다.mp3")
        t_sin_alpha = mTex(r"\sin \alpha = \frac {x}{\cos \beta}",color=YELLOW).next_to(triX2,DOWN,aligned_edge=LEFT)
        self.play(Write(t_sin_alpha), run_time=3)
        self.wait(4)

        # 따라서, 엑스는 싸인 알파, 코싸인 베타가 됩니다.
        self.add_sound(r"res\sound\s4\04_따라서_엑스는_싸인_알파_코싸인_베타가_됩니다.mp3")
        t_x_equal = mTex(r"x = \sin \alpha \cos \beta",color=YELLOW).next_to(t_sin_alpha,DOWN,aligned_edge=LEFT)
        boxX = SurroundingRectangle(t_x_equal)

        self.play(Write(t_x_equal), run_time=3)
        self.wait()
        self.play(Write(boxX))
        self.wait(3)

        self.boxX = boxX

    def s6(self):
        t_bsin=self.t_bsin.copy()
        ty = self.ty.copy()
        lineBS=self.lineBS.copy()
        lineSQ=self.lineSQ.copy()
        lineQB=self.lineQB.copy()

        pQ = self.pQ
        pO = self.pO
        pB = self.pB

        elbowQ = self.elbowQ
        elbowR = self.elbowR

        alphaT = self.alphaT

        # 이제 y값을 구해보겠습니다.
        shifted_triX = VGroup(lineBS,lineSQ,lineQB,t_bsin)

        self.add_sound(r"res\sound\s5\01_이제_y값을_구해보겠습니다.mp3")
        self.play(shifted_triX.shift, RIGHT*3, run_time=3)
        self.play(ty.shift, RIGHT*2.5, run_time=2)

        # 여기서 이 각은 알파가 됩니다.
        n_pB = shifted_triX[0].get_top()
        pArcS = shifted_triX[0].point_from_proportion(0.2)
        pArcE = shifted_triX[2].point_from_proportion(0.83)
        arc = ArcBetweenPoints(pArcS, pArcE)
        tAlpha = mTex(r"\alpha",color=YELLOW).next_to(n_pB,RIGHT,buff=0.3).shift(DOWN*0.1)

        #B에 있는 알파와 아크
        pArcS = self.lineBS.point_from_proportion(0.2)
        pArcE = self.lineQB.point_from_proportion(0.83)
        arcB = ArcBetweenPoints(pArcS, pArcE)

        alpha_in_B = mTex(r"\alpha", YELLOW).next_to(pB, RIGHT, buff=0.1).shift(DOWN * 0.1)

        self.add_sound(r"res\sound\s5\02_여기서_이_각은_알파가_됩니다.mp3")
        self.play(
            ShowCreation(arc),
            ShowCreation(tAlpha),
           run_time=2
        )

        #B에 있는
        self.play(
            ShowCreation(arcB),
            Write(alpha_in_B),
            run_time=1,
        )
        self.wait(2)

        # 왜냐하면, 이 각은 서로 마주보는 각이기에 같고,
        self.add_sound(r"res\sound\s5\03_왜냐하면_이_각은_서로_마주보는_각이기에_같고.mp3")

        Tx = pB[0]
        Ty = ((pQ[1]-pO[1])/(pQ[0]-pO[0]))*(Tx - pO[0])+pO[1]
        pT = xy(Tx,Ty)
        dot1 = Dot(radius=0.04,color=GREEN).move_to(pT).shift(DOWN*0.1+LEFT*0.05)
        dot2 = Dot(radius=0.04, color=GREEN).move_to(pT).shift(UP * 0.1 + RIGHT * 0.05)

        self.camera_frame.save_state()
        self.play(
            self.camera_frame.shift, LEFT*2+DOWN*0.5,
            self.camera_frame.scale, 0.6,
            run_time=2,
        )

        self.play(
            ShowCreation(dot1),
            ShowCreation(dot2),
        )
        self.play(
            Indicate(dot1, scale_factor=1.5, run_time=2),
            Indicate(dot2,scale_factor=1.5, run_time=2),
        )
        self.wait(2)

        # 여기와 여기가 직각이기에,
        self.add_sound(r"res\sound\s5\04_여기와_여기가_직각이기에.mp3")
        self.play(
            Indicate(elbowQ, scale_factor=1.4),
            Indicate(elbowR, scale_factor=1.4),
            Flash(elbowQ, run_time=2),
            Flash(elbowR, run_time=2),
        )
        self.wait(2)

        # 이 각이 알파가 됩니다.
        self.add_sound(r"res\sound\s5\05_이_각이_알파가_됩니다.mp3")

        self.play(
            ShowCreation(arcB),
            Write(alpha_in_B),
            run_time=1,
        )
        self.play(
            Indicate(arcB),
            TransformFromCopy(alphaT,alpha_in_B),
            run_time=4,
        )
        self.wait(2.5)

        self.play(self.camera_frame.restore)
        self.wait()

        self.shifted_triX = shifted_triX
        self.shifted_ty = ty

    def s7(self):
        triX = self.shifted_triX
        ty = self.shifted_ty
        t_sinb = triX[3]

        # 이제 이 삼각형에서,
        self.add_sound(r"res\sound\s6\01_이제_이_삼각형에서.mp3")
        self.wait()
        self.play(WiggleOutThenIn(triX), run_time=2)
        self.wait(2)

        # 빗 변은 싸인 베타이고, 밑 변이 와이 이기에
        self.add_sound(r"res\sound\s6\02_빗_변은_싸인_베타이고_밑_변이_와이_이기에.mp3")
        self.play(Indicate(t_sinb,scale_factor=1.3),run_time=2)
        self.play(Indicate(ty, scale_factor=1.3), run_time=2)
        self.wait()

        # 코싸인 알파는 싸인 베타 분의 와이이고,
        self.add_sound(r"res\sound\s6\03_코싸인_알파는_싸인_베타_분의_와이이고.mp3")
        t_cos_alpha = mTex(r"\cos \alpha = \frac {y}{\sin \beta}", color=YELLOW).next_to(triX.get_top(), RIGHT).shift(RIGHT+DOWN*0.5)
        self.play(Write(t_cos_alpha), run_time=3)
        self.wait(3)

        # 따라서 와이는, 코싸인 알파, 싸인 베타가 됩니다.
        self.add_sound(r"res\sound\s6\04_따라서_와이는_코싸인_알파_싸인_베타가_됩니다.mp3")
        t_y_equal = mTex(r"y = \cos \alpha \sin \beta", color=YELLOW).next_to(t_cos_alpha, DOWN, aligned_edge=LEFT)
        boxY = SurroundingRectangle(t_y_equal)

        self.play(Write(t_y_equal), run_time=3)
        self.wait(2)
        self.play(Write(boxY))

        self.wait()
        self.boxY = boxY

    def s8(self):
        t_sin_ab = self.t_sin_ab

        boxX = self.boxX
        boxY = self.boxY

        t_sincos = mTex(r"\sin \alpha \cos \beta",color=YELLOW).next_to(t_sin_ab[0],RIGHT)
        t_plus = mTex("+",color=YELLOW).next_to(t_sincos)
        t_cossin = mTex(r"\cos \alpha \sin \beta", color=YELLOW).next_to(t_plus)

        # 이제 엑스 더하기 와이를 해보면,
        self.add_sound(r"res\sound\s7\01_이제_엑스_더하기_와이를_해보면.mp3")
        self.play(Indicate(t_sin_ab, scale_factor=1.4, run_time=2))
        self.play(Flash(t_sin_ab[1], run_time=2))
        self.play(FadeOut(t_sin_ab[1]))

        self.play(boxX.move_to, t_sincos, run_time=3)
        self.play(
            Transform(boxX, t_sincos),
            Write(t_plus),
        )
        self.wait()

        self.play(boxY.move_to, t_cossin, run_time=3)
        self.play(Transform(boxY, t_cossin),)
        self.wait()

        # 싸인 알파, 코싸인 베타, 더하기, 코싸인 알파, 싸인 베타가 됩니다.
        self.add_sound(r"res\sound\s7\02_싸인_알파_코싸인_베타_더하기_코싸인_알파_싸인_베타가_됩니다.mp3")
        self.play(Indicate(VGroup(t_sincos,t_plus,t_cossin)))
        self.wait(5)

        # 간략히 하면, 싸인 알파 더하기 베타는, "씬 코 코 씬" 입니다.
        h1 = mText("씬",color=RED).next_to(t_sincos, DOWN, aligned_edge=LEFT)
        h2 = mText("코",color=RED).next_to(h1, RIGHT, buff=0.8)
        h3 = mText("코", color=RED).next_to(t_cossin, DOWN, aligned_edge=LEFT)
        h4 = mText("씬", color=RED).next_to(h3, RIGHT, buff=0.8)

        self.add_sound(r"res\sound\s7\03_간략히_하면_싸인_알파_더하기_베타는_씬코_코씬입니다_박수.mp3")
        box = SurroundingRectangle(VGroup(t_sin_ab[0],t_sincos,t_plus,t_cossin))
        self.play(ShowCreation(box, run_time=2))
        self.play(
            LaggedStart(
                Write(h1), Write(h2), Write(h3), Write(h4),
            ),
            run_time=3,
        )

        self.wait(12)