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


        def create_sects(n_sects) ->VGroup:
            sects = VGroup()
            for i in range(n_sects):
                sect = AnnularSector(
                    inner_radius=0, 
                    outer_radius=RADIUS, 
                    angle=TAU/n_sects, 
                    start_angle=TAU*i/n_sects, 
                    fill_opacity=1,
                    stroke_width= 2, 
                    color=BLUE
                ).set_stroke(WHITE, width=.9)
                sects.add(sect)
            
            topp=[]
            bot=[]
            anis=[]
            for i in range(n_sects):
                temp=sects[i].copy()
                temp.rotate(-2*PI*i/n_sects, about_point=[0,0,0])
                temp.rotate(3 * PI/2-PI/n_sects, about_point=[0,0,0])
                if i<math.floor(n_sects/2):
                    topp.append(temp)
                    anis.append(sects[i].animate.set_fill(BLUE_D, opacity=1))
                else:
                    bot.append(temp)
                    anis.append(sects[i].animate.set_fill(BLUE_D, opacity=1))

            self.remove(self.circle)
            topsects=VGroup(*topp)
            topsects.arrange(RIGHT, buff=0)
            botsects=VGroup(*bot)
            botsects.arrange(LEFT * 5, buff=0)
            botsects.shift(.5*3*DOWN, LEFT * 3)
            topsects.next_to(botsects.get_right(), buff=0)
 
            ReplacementTransform(VGroup(*sects[:math.floor(n_sects/2)]),topsects)
            ReplacementTransform(VGroup(*sects[math.floor(n_sects/2):]),botsects)
            return VGroup(*topsects, *botsects).shift(UP * 3)


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
            self.play(all_sects.animate.shift(UP * 3))
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


            self.to_focus = all_sects[NUMBER_OF_LINES - 1]


            self.camera:MovingCamera

            self.camera.frame.save_state()
            self.play( self.camera.frame.animate.set(height = self.to_focus.height * 1.25), run_time = .5)
            self.play(self.camera.frame.animate.shift(DOWN * .1))
            self.play(
                self.camera.frame.animate
                .next_to([self.to_focus.get_left()[0] - self.camera.frame.width + self.to_focus.width * 1.5, self.to_focus.get_left()[1], self.to_focus.get_left()[2]], buff= 0),
            )

            self.wait(2)

            r = MathTex("r", font_size = MINI_TRIANGLE_FONT).move_to(self.to_focus.get_left())
            r.add_updater(lambda x: x.move_to(self.to_focus.get_left()))
            r2 = r.copy().move_to(self.to_focus.get_right())
            r2.add_updater(lambda x: x.move_to(self.to_focus.get_right()))
            theta = MathTex("\\theta", font_size = MINI_TRIANGLE_FONT).move_to(self.to_focus.get_top() - [0, .7, 0])
            theta.add_updater(lambda x:x.move_to(self.to_focus.get_top() - [0, .7, 0]))
            tau_r_n = MathTex("\\frac {\\tau r} {n}", font_size = MINI_TRIANGLE_FONT - 2, color = RED).move_to(self.to_focus.get_bottom() + [0, -.16, 0])
            tau_r_n.add_updater(lambda x:x.move_to(self.to_focus.get_bottom() + [0, -.16, 0]))
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

            a_but_with_n_param = MathTex("A(n) = \\frac {1} {2} \\sin", "\\left(","\\theta", "\\right)", "ab", font_size = 15).move_to(area_of_triangle[0])
            self.play(ReplacementTransform(area_of_triangle, a_but_with_n_param))

            t_n = MathTex("\\frac {\\tau} {n}", font_size = 15, color = RED).move_to(area_of_triangle[2].get_center())
            r_sq = MathTex("r^2", font_size = 15).move_to(area_of_triangle[4])
            self.play(
                Transform(theta_equals, t_n),
                ReplacementTransform(a_but_with_n_param[2], t_n),
                ReplacementTransform(theta, MathTex("\\frac {\\tau} {n}", font_size = MINI_TRIANGLE_FONT - 2, color = RED).move_to(theta))
            )


            self.wait(2)
            self.play(Transform(a_but_with_n_param[4], r_sq))
            self.play(Restore(self.camera.frame))
            self.wait(1)
            self.remove(theta_equals)
            self.remove(t_n)


            total_area = Text("Total area:", font_size= 50).move_to(tau_r.get_bottom()).shift(DOWN * 1.2)
            equation_for_total_area = MathTex("nA(n)", font_size= 50).next_to(total_area, RIGHT, buff = .5)
            equation_expanded = MathTex(
                "n \\left( \\frac {1} {2} \\sin \\left(\\frac {\\tau} {n}\\right) r^2\\right)", 
                font_size = 50
            ).next_to(total_area, RIGHT, buff=1.5)

            equation_for_total_area_inf = MathTex(
                "\\lim_{n \\to \\infty} n A (n)", 
                font_size = 50).move_to(equation_for_total_area)

            self.wait(2)

            self.play(Write(total_area), Write(equation_for_total_area))

            self.wait(1)
            infty = MathTex("\\infty", font_size=70).move_to([
                all_sects.get_right()[0],
                all_sects.get_top()[1] + 1, 
                0
            ])

            copy_all_sects = all_sects.copy()
            self.n_of_sects = 75
            def make_infinite_sectors(all_sects:VGroup, alpha):
                new_n = int(interpolate(len(all_sects), self.n_of_sects, alpha ))
                all_sects.become(create_sects(new_n))
                self.to_focus = all_sects[new_n - 1].set_color(YELLOW)

            self.play(
                UpdateFromAlphaFunc(
                    all_sects,
                    make_infinite_sectors,
                    run_time = 2.5,
                    rate_func = rate_functions.ease_in_expo
                ),
                Transform(textGroup[2], infty),
                ShowCreationThenFadeOut(SurroundingRectangle(textGroup[2], color = YELLOW, buff=.25))
            )
            self.wait(1)



            self.play(
                Transform(equation_for_total_area, equation_for_total_area_inf)
            )

            self.play( self.camera.frame.animate.set(height = self.to_focus.height * 1.25), run_time = .5)
            self.camera.frame.animate.shift(DOWN * .1)
            self.play(
                self.camera.frame.animate
                .next_to([self.to_focus.get_left()[0] - self.camera.frame.width + self.to_focus.width * 1.5, self.to_focus.get_left()[1], self.to_focus.get_left()[2]], buff= 0),
            )

            equation_for_total_area_inf = MathTex(
                "\\lim_{n \\to \\infty} n A (n) =",
                r"\lim_{n \to \infty}", "n", r"\left(\sin \left(", r"\frac {\tau} {n}", r"\right) \frac {1} {2} r^2 \right)", 
                font_size = 15).move_to(a_but_with_n_param.get_top())
            equation_for_total_area_inf[4].set_color(RED)

            self.play(FadeOut(a_but_with_n_param), run_time = .01)

            self.play(Write(equation_for_total_area_inf))

            copy_of_to_focus = self.to_focus.copy()
            self.n_of_sects = 150

            self.play(
                ShowCreationThenFadeOut(SurroundingRectangle(equation_for_total_area_inf[3:], color = YELLOW, buff=.05)),

                UpdateFromAlphaFunc(
                    all_sects,
                    make_infinite_sectors,
                    run_time = 9,
                    rate_func = rate_functions.ease_in_expo
                ),
                run_time = 2
            )
            self.camera.frame.save_state()
            self.play(
                ShowCreationThenFadeOut(SurroundingRectangle(equation_for_total_area_inf[2], color = YELLOW, buff = .05)),
                run_time = 1
            )

            self.play(
                self.camera.frame.animate.shift(RIGHT * 7),
                run_time = 4
            )

            self.play(Restore(self.camera.frame))

            u_of_n = MathTex(
                "{{u(n)}} = { {{\\tau}} \\over {{n}} } ",
                font_size = 15
            ).move_to(self.camera.frame.get_corner(DL) + [.5, .7, 0])
            u_of_n[2:].set_color(RED)



            n_ito_u = u_of_n.copy().next_to(u_of_n, RIGHT, buff = 1.5)



            self.play(Write(u_of_n))
            self.wait(1)
            self.play(Write(n_ito_u))
            self.play(
                Swap(n_ito_u[4], n_ito_u[0])
            )
            self.wait(1)

            lim_of_u = MathTex(
                "\\lim_{n \\to \\infty}{{u(n)}} = 0 ",
                font_size = 15
            ).move_to(u_of_n.get_bottom() + [0, -.2, 0])
            
            self.play(
                Write(lim_of_u)
            )

            self.wait(1)

            new_limits_ITO_u = MathTex(
                r"\lim_{u(n) \to 0} \frac {\tau} {u(n)}", r"\sin \left(",r"u(n)", r"\right) \frac {1} {2} r^2",
                font_size = 15
            ).move_to(equation_for_total_area_inf[1:]).shift(RIGHT * .2)
            new_limits_ITO_u[2].set_color(RED)

            self.play(
                Transform(equation_for_total_area_inf[1:], new_limits_ITO_u)
            )
            self.play(
                ShowCreationThenFadeOut(SurroundingRectangle(equation_for_total_area_inf[1], color = YELLOW, buff = .05))
            )
            self.wait(1.5)
            self.play(
                Transform(
                    equation_for_total_area_inf[1:],
                    MathTex(
                        r"\lim_{u(n) \to 0}", r"\frac {\sin \left(u(n)\right)} {\frac {u(n)}{\tau} }", r"\frac {1} {2} r^2",
                        font_size = 15
                    ).move_to(new_limits_ITO_u).set_color(WHITE)
                ),
            )

            self.wait(2)

            self.play(
                Transform(
                    equation_for_total_area_inf[1:],
                    MathTex(
                        r"\lim_{u(n) \to 0}", r"\frac {\sin \left(u(n)\right)} {u(n)}", r"\frac {\tau} {2} r^2",
                        font_size = 15
                    ).move_to(new_limits_ITO_u).set_color(WHITE)
                ),
            )

            equation_for_total_area_inf[2].set_color(YELLOW)
            special_lim = Text("! ! ! Special limit alert ! ! !", color = RED, font_size=17).move_to(self.camera.frame_center)
            self.play(
                ShowCreationThenFadeOut(SurroundingRectangle(equation_for_total_area_inf[2:4], color = YELLOW, buff = .05)),
                ShowCreationThenFadeOut(special_lim)
            )

            self.play(
                ShowCreationThenFadeOut(Line(
                    equation_for_total_area_inf[2:4].get_edge_center(UR),
                    equation_for_total_area_inf[2:4].get_edge_center(DL)
                    )),
                Transform(
                    equation_for_total_area_inf[1:4],
                    MathTex("= 1", font_size = 15).move_to(equation_for_total_area_inf[2:4])
                )
            )
            self.play(
                Transform(equation_for_total_area_inf[4:], MathTex(r"\frac {\tau} {2} r^2")),
                equation_for_total_area_inf[4:].animate.move_to(equation_for_total_area_inf[1:4]),
                FadeOut(equation_for_total_area_inf[1:4]),
                Create(SurroundingRectangle(equation_for_total_area_inf[4:], YELLOW))
            )



            self.wait()



    



class understandingthelimit(MovingCameraScene):
    def construct(self):
        self.camera:MovingCamera
        self.camera.frame.save_state()
        plane = NumberPlane(
            x_range=[-10, 30],
            y_range=[-10, 10]
        )

        self.camera.frame.move_to(plane.c2p(*[5, 0, 0]))

        self.play(
            DrawBorderThenFill(plane),
            plane.animate.add_coordinates()
        )

        self.wait(.5)
        sinx = plane.plot(lambda x: np.sin(x) / x).set_color(RED)
        line_at_zero = Line(
            plane.c2p(*[0, -3, 0]),
            plane.c2p(*[0, 4, 0])
        ).set_color(YELLOW)
        line_at_zero_label = MathTex(
            r"\lim_{x \ \to 0} \frac {\sin x} {x} = 1", 
            color = YELLOW
        ).move_to(line_at_zero.get_bottom() + [0, -.3, 0])


        self.play(
            Create(sinx)
        )



        sinx_label = plane.get_graph_label(
            sinx,
            label = MathTex(r"\frac {\sin x} {x}", color = RED),
            direction=UR,
            x_val=2
        )
        self.play(Write(sinx_label))
        self.play(Create(line_at_zero))
        self.wait(1)

        dot_sin = Dot().set_color(BLUE_A)
        # dot_sin_label = MathTex(f"{dot_sin.get_x()}")
        # dot_sin_label.add_updater(lambda x : x.move_to(dot_sin))
        def moveTozero(dot:Dot, alpha):
            to = interpolate(10, 0.001, alpha)

            dot.move_to(sinx.get_point_from_function(to))


        sinx.reverse_points()
        self.play(
            UpdateFromAlphaFunc(
                dot_sin,
                moveTozero,
                rate_func = rate_functions.rush_into,
                run_time = 2
            ) 
        )
        dot_sin.move_to(plane.c2p(*[0, 1, 0]))
        self.play(Write(line_at_zero_label))
        
        self.wait(1)
        self.play(FadeOut(sinx_label, line_at_zero_label))

        def generate_points_un(x):
            return TAU / x
        u_n:ParametricFunction = plane.plot(lambda x: generate_points_un(x), discontinuities = [0], dt = .5, use_smoothing = False).set_color(PINK)

        
        un_label = plane.get_graph_label(
            u_n,
            label = MathTex(r"u(n) = \frac {\tau} {n}"),
            direction=UR,
            x_val= 5
        )

        self.play(Create(u_n))
        self.play(Write(un_label))

        t_x_dot = Dot().set_color(WHITE).move_to(plane.c2p(*u_n.get_point_from_function(1)))
        self.add(t_x_dot)
        def movedown(dot:Dot, alpha):
            to = interpolate(2, 10, alpha)

            dot.move_to(u_n.get_point_from_function(to))

        lim_of_x = MathTex(
            r"\lim_{n \to \infty} u(n) = 0",
            color = YELLOW,
        ).move_to(plane.c2p(*[9, 3, 0]))

        self.add(t_x_dot)
        self.play(
            UpdateFromAlphaFunc(
                t_x_dot,
                movedown,
                run_time = 5,
                rate_func = rate_functions.rush_from
            ),
            Write(lim_of_x)
        )

        self.play(FadeOut(sinx, line_at_zero, dot_sin))

        sin_un = plane.plot(lambda x: np.sin(TAU / x) / (TAU/ x), discontinuities = [0], dt = .01, use_smoothing = True).set_color(GREEN)
        si_un_label = plane.get_graph_label(
            sin_un,
            label = MathTex(r"\frac {\sin(u(n))} {u(n)}"),
            direction=DR,
            x_val=1
        )

        self.play(Create(sin_un), Write(si_un_label))

        dot_on_sin_ux = Dot().set_color(WHITE).move_to(sin_un.get_point_from_function(1))
        t_x_dot.move_to(plane.c2p(*u_n.get_point_from_function(1)))
        self.add(dot_on_sin_ux)

        self.both_dots = VGroup(dot_on_sin_ux, t_x_dot)

        self.wait(1)
        self.camera.auto_zoom(self.both_dots)

        def continueTOINF(group, alpha):
            to = interpolate(1, 15, alpha)
            group[0].move_to(sin_un.get_point_from_function(to))
            group[1].move_to(u_n.get_point_from_function(to))

        def move_cam_w_points(mob):
            mob.move_to(self.both_dots)

        self.play(Restore(self.camera.frame))

        self.play(
            UpdateFromAlphaFunc(
                self.both_dots,
                continueTOINF,
                run_time = 3,
                rate_func = rate_functions.rush_from
            ),

        )

        sin_un_lim = MathTex(
            r"\lim_{u(n) \to 0} \frac {\sin u(n)} {u(n)} = 1"
        ).move_to(plane.c2p(*[8,-2, 0])).set_color(YELLOW)

        self.play(Write(sin_un_lim))
            
        self.wait()

    
        


