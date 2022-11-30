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
        

class split(MovingCameraScene):
    # def __init__(self, **kwargs):
    #     ZoomedScene.__init__(
    #         self,
    #         zoom_factor=0.3,
    #         zoomed_display_height=8,
    #         zoomed_display_width=1.5,
    #         image_frame_stroke_width=20,
    #         zoomed_camera_config={
    #             "default_frame_stroke_width": 3,
    #             },
    #         **kwargs
    #     )

    def construct(self):
        self.circle = Circle(
            radius=2,
            color=BLUE,
            fill_opacity = .5
        )


        self.play(Create(self.circle))
        self.wait(1)
        NUMBER_OF_LINES = 50
        lines = []
        for num in range(1, NUMBER_OF_LINES):
            start_angle = TAU/NUMBER_OF_LINES * num
            end = TAU/NUMBER_OF_LINES * num + TAU/2

            line = Line(
                self.circle.point_at_angle(start_angle),
                self.circle.point_at_angle(end),
                stroke_width = 2
            )
            lines.append(line)

        lines = VGroup(*lines)
        self.play(FadeIn(lines), run_time = .1)
        
        self.wait(1)
        for n in [NUMBER_OF_LINES]:
            sects=[AnnularSector(
                inner_radius=0, 
                outer_radius=2, 
                angle=TAU/n, 
                start_angle=TAU*i/n, 
                fill_opacity=.5,
                stroke_width= 2, 
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
            self.play(*anis)
            topsects=VGroup(*topp)
            topsects.arrange(RIGHT, buff=0)
            botsects=VGroup(*bot)
            botsects.arrange(LEFT * 5, buff=0)
            botsects.shift(.5*3*DOWN, LEFT * 3)
            topsects.next_to(botsects.get_right(), buff=0)
 
            self.play(ReplacementTransform(VGroup(*sects[:math.floor(n/2)]),topsects),ReplacementTransform(VGroup(*sects[math.floor(n/2):]),botsects), run_time=2)
            self.wait(.5)
            
            all_sects = VGroup(*topsects, *botsects)
            # all_sects.shift(UP * 1)
            self.play(all_sects.animate.shift(UP * 2))
            self.wait(2)

            infty = MathTex("\\infty", font_size=70).move_to([
                all_sects.get_right()[0],
                all_sects.get_top()[1] + 1, 
                0
            ])
            dots = MathTex("\\cdots", font_size = 70).move_to([
                all_sects.get_top()[0],
                all_sects.get_top()[1] + 1,
                0
            ])

            one_two_three = MathTex(
                "1, 2, 3",
                font_size = 70
            ).move_to([
                all_sects.get_left()[0] + .7,
                all_sects.get_top()[1] + 1,
                0
            ])

            n = MathTex("n", font_size=70).move_to(infty.get_center())

            textGroup = VGroup(one_two_three, dots, infty)

            self.play(Write(textGroup)) 
            self.wait(3)
            self.play(Transform(textGroup[2], n), run_time = 1)
            br = Brace(all_sects, sharpness=1)
            tau_r = MathTex("\\tau r", font_size = 70, color = RED).move_to(br.get_center()).shift(DOWN * 1)
 
            self.play(Create(br), run_time = 2)
            self.wait(2)
            self.play(Write(tau_r))

            self.wait(2)
            to_focus = all_sects[NUMBER_OF_LINES - 1]
            diagram = VGroup(*all_sects, br, tau_r, *textGroup)

            # frame = self.zoomed_camera.frame
            # frame.move_to(to_focus)
            # self.play(
            #     Create(frame),
            # )
            # self.activate_zooming(animate=False)
            # self.play(self.get_zoomed_display_pop_out_animation())
            # set(height = to_focus.height * 7, width = to_focus.width * 3)

            self.camera:MovingCamera

            self.camera.frame.save_state()
            self.play( self.camera.frame.animate.set(height = to_focus.height))
            self.play(
                self.camera.frame.animate
                .next_to([to_focus.get_left()[0] - self.camera.frame.width + to_focus.width, to_focus.get_left()[1], to_focus.get_left()[2]], buff= 0),

            )

            self.wait(2)
 

            self.wait(3)
    
        





