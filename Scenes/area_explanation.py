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
        RADIUS = 2
        MINI_TRIANGLE_FONT = 12
        self.circle = Circle(
            radius= RADIUS    ,
            color=BLUE,
            fill_opacity = .5
        )


        self.play(Create(self.circle))
        self.wait(1)
        NUMBER_OF_LINES = 50
        self.wait(1)
        for n in [NUMBER_OF_LINES]:
            sects = VGroup()

            for i in range(n):
                sect = AnnularSector(
                    inner_radius=0, 
                    outer_radius=RADIUS, 
                    angle=TAU/n, 
                    start_angle=TAU*i/n, 
                    fill_opacity=1,
                    stroke_width= 2, 
                    color=BLUE
                ).set_stroke(WHITE, width=.9)
                sects.add(sect)
                
            self.play(FadeIn(sects), run_time = 1.5)

            topp=[]
            bot=[]
            anis=[]
            for i in range(n):
                temp=sects[i].copy()
                temp.rotate(-2*PI*i/n, about_point=[0,0,0])
                temp.rotate(3 * PI/2-PI/n, about_point=[0,0,0])
                if i<math.floor(n/2):
                    topp.append(temp)
                    anis.append(sects[i].animate.set_fill(BLUE_D, opacity=1))
                else:
                    bot.append(temp)
                    anis.append(sects[i].animate.set_fill(BLUE_D, opacity=1))

            self.remove(self.circle)
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
            all_sects.shift(UP * 1)
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

            self.camera:MovingCamera

            self.camera.frame.save_state()
            self.play( self.camera.frame.animate.set(height = to_focus.height * 1.25))
            self.play(self.camera.frame.animate.shift(DOWN * .1))
            self.play(
                self.camera.frame.animate
                .next_to([to_focus.get_left()[0] - self.camera.frame.width + to_focus.width * 1.5, to_focus.get_left()[1], to_focus.get_left()[2]], buff= 0),
            )

            self.wait(2)

            r = MathTex("r", font_size = MINI_TRIANGLE_FONT).move_to(to_focus.get_left())
            r2 = r.copy().move_to(to_focus.get_right())
            theta = MathTex("\\theta", font_size = MINI_TRIANGLE_FONT).move_to(to_focus.get_top() - [0, .7, 0])
            tau_r_n = MathTex("\\frac {\\tau r} {n}", font_size = MINI_TRIANGLE_FONT - 2, color = RED).move_to(to_focus.get_bottom() + [0, -.16, 0])

            self.play(
                FadeIn(r),
                FadeIn(r2),
                FadeIn(theta),
                FadeIn(tau_r_n)
            )

            theta_equals = MathTex("\\theta = \\frac {\\tau} {n}", font_size = 15).move_to(self.camera.frame.get_edge_center(UL) + [.5, -.5, 0])

            area_of_triangle = MathTex("A = \\frac {1} {2} \\sin", "\\left(","\\theta", "\\right)", "ab", font_size = 15).move_to(theta_equals.get_bottom() + [0, -.3, 0])


            self.play(Write(theta_equals))
            self.play(Write(area_of_triangle))

            self.play(area_of_triangle.animate.shift(RIGHT * 1.5))

            a_but_with_n_param = MathTex("A(n) = \\frac {1} {2} \\sin", "\\left(","\\theta", "\\right)", "ab" font_size = 15).move_to(area_of_triangle[0])
            self.play(ReplacementTransform(area_of_triangle, a_but_with_n_param))
            t_n = MathTex("\\frac {\\tau} {n}", font_size = 15, color = RED).move_to(area_of_triangle[2].get_center())
            r_sq = MathTex("r^2", font_size = 15).move_to(area_of_triangle[4])
            self.play(
                Transform(theta_equals, t_n),
                Transform(area_of_triangle[2], t_n),
            )

            self.wait(2)
            self.play(Transform(area_of_triangle[4], r_sq))
            self.play(Restore(self.camera.frame))
            self.wait(1)

            total_area = Text("Total area:", font_size = 15).move_to(tau_r.get_bottom()).shift(DOWN * 1.2)
            equation_for_total_area = MathTex("nA(n)")

            self.play(Write(total_area), Write(equation_for_total_area))

            self.play( self.camera.frame.animate.set(height = to_focus.height * 1.25))
            self.camera.frame.animate.shift(DOWN * .1)
            self.play(
                self.camera.frame.animate
                .next_to([to_focus.get_left()[0] - self.camera.frame.width + to_focus.width * 1.5, to_focus.get_left()[1], to_focus.get_left()[2]], buff= 0),
            )


            


    
        


class no_split(MovingCameraScene):
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
        RADIUS = 3
        self.circle = Circle(
            radius=RADIUS,
            color=BLUE,
            fill_opacity = .5
        )


        self.play(Create(self.circle))
        self.wait(1)
        NUMBER_OF_LINES = 75
        self.camera:MovingCamera
        self.camera.frame.save_state()
        for n in [NUMBER_OF_LINES]:
            sects= VGroup()

            for i in range(n):
                sect = AnnularSector(
                    inner_radius=0, 
                    outer_radius=RADIUS, 
                    angle=TAU/n, 
                    start_angle=TAU*i/n, 
                    fill_opacity=1,
                    stroke_width= 2, 
                    color=BLUE
                ).set_stroke(WHITE, width=.9)
                sects.add(sect)
                
            self.play(Create(sects), run_time = 1.5)

            all_sects = VGroup(*sects)

            self.remove(self.circle)


            self.wait(2)
            to_focus: AnnularSector = all_sects[NUMBER_OF_LINES - 1]




            self.play(self.camera.frame.animate.set(height = to_focus.height - 2, width = to_focus.width * 1.1),
                all_sects.animate.set(stroke_width = 0))
            self.play(
                self.camera.frame.animate.move_to([to_focus.get_left()[0] + self.camera.frame.width / 2, to_focus.get_left()[1], to_focus.get_left()[2]]),
                to_focus.animate.set(color = YELLOW)
            )

            theta = MathTex("\\theta", font_size = 15)
            angle = MathTex("\\frac {\\tau} {n}", font_size = 15).next_to(to_focus.get_left())
            radius = MathTex("r", font_size = 15, color = BLACK ).move_to([
                to_focus.get_top()[0],
                to_focus.get_top()[1],
                to_focus.get_top()[2],
                ])
            radius2 = radius.copy().move_to([
                to_focus.get_bottom()[0],
                to_focus.get_bottom()[1] + to_focus.width / 2,
                to_focus.get_bottom()[2],
                ])

            sector_formula = MathTex("\\theta r", font_size = 15).next_to(to_focus.get_right())
            sector_length = MathTex("\\frac {\\tau r} {n}", font_size = 15).next_to(to_focus.get_right())

            
            
            self.play(
                FadeIn(radius),
                FadeIn(radius2)
            )
            self.play(
                FadeIn(angle)
            )


 

            self.wait(3)



