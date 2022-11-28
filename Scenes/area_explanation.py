from manim import *
import math
class a_of_circle(Scene):
    def construct(self):
        self.title = Text("aReA oF a cIrClE", font_size=40, color=YELLOW).to_edge(UL)

        self.circle = Circle(
            radius = 3,
            color=BLUE,
            fill_opacity= .5
        )

        self.big_a = MathTex("A", font_size = 100).add_updater(lambda x : x.move_to(self.circle.get_center()))

        
        self.play(Create(self.circle), Write(self.title), run_time = 1)
        self.play(FadeIn(self.big_a), run_time = .5)
        self.play(self.circle.animate.shift(LEFT * 3))
        
        eq = MathTex("= {\\pi}r^2", font_size = 100, color = YELLOW).shift(RIGHT * 2)

        tau_eq = MathTex("= {\\frac {\\tau} {2}}r^2", font_size = 100, color = RED).move_to(eq.get_center())

        self.play(FadeIn(eq))
        self.wait(1.5)
        self.play(Transform(eq, tau_eq))
        self.wait(2)

        gross = Text("Thats disgusting!")
        or_is_it = Text("...or is it?")
        text = VGroup(gross, or_is_it)
        text.arrange(DOWN, center=False, aligned_edge=LEFT).to_edge(DR)
        text[1].set_color(YELLOW)
        self.play(FadeIn(text[0]), run_time=.5)
        self.wait(1)
        self.play(FadeIn(text[1]))
        self.wait(3)
        

class split(Scene):
    def construct(self):
        self.circle = Circle(
            radius=2,
            color=BLUE,
            fill_opacity = .5
        )


        self.play(Create(self.circle))
        self.wait(1)
        NUMBER_OF_LINES = 10
        lines = []
        for num in range(1, NUMBER_OF_LINES):
            start_angle = TAU/NUMBER_OF_LINES * num
            end = TAU/NUMBER_OF_LINES * num + TAU/2

            line = Line(
                self.circle.point_at_angle(start_angle),
                self.circle.point_at_angle(end),
                stroke_width = .9
            )
            lines.append(line)

        lines = VGroup(*lines)
        self.play(lines.animate, run_time = .1)
        
        self.wait(1)
        for n in [20]:
            sects=[AnnularSector(
                inner_radius=0, 
                outer_radius=2, 
                angle=TAU/n, 
                start_angle=TAU*i/n, 
                fill_opacity=.5,
                stroke_width=0, 
                color=BLUE) for i in range(n)]

            VGroup(*sects).set_stroke(WHITE, width=.9)


            topp=[]
            bot=[]
            anis=[]
            for i in range(n):
                temp=sects[i].copy()
                if i<math.floor(n/2):
                    temp.rotate(-2*PI*i/n, about_point=[0,0,0])
                    temp.rotate(3 * PI/2-PI/n, about_point=[0,0,0])
                    topp.append(temp)
                    anis.append(sects[i].animate.set_fill(BLUE_D, opacity=1))
                else:
                    temp.rotate(-2 * PI * i / n, about_point=[0, 0, 0])
                    temp.rotate(3*PI / 2 - PI / n, about_point=[0, 0, 0])
                    bot.append(temp)
                    anis.append(sects[i].animate.set_fill(BLUE_D, opacity=1))

            self.remove(self.circle)
            self.remove(lines)
            topsects=VGroup(*topp)
            topsects.arrange(RIGHT, buff=0)
            botsects=VGroup(*bot)
            botsects.arrange(LEFT * 5, buff=0)
            botsects.shift(.5*3*DOWN, LEFT * 3)
            topsects.next_to(botsects.get_right(), buff=0)
 
            self.play(ReplacementTransform(VGroup(*sects[:math.floor(n/2)]),topsects),ReplacementTransform(VGroup(*sects[math.floor(n/2):]),botsects), run_time=2)
            self.wait(.5)
            # self.play(topsects.animate.shift(.5*math.cos(PI/n)*3*DOWN+.5*sects[0].get_width()*RIGHT), botsects.animate.shift(.5*math.cos(PI/n)*3*UP), run_time=2)
            # self.wait(.5)
            # self.play(topsects.animate.set_stroke(PURPLE, width=0).set_fill(PURPLE, opacity=1),botsects.animate.set_stroke(PURPLE, width=0))
            # self.wait(3)

    
        





