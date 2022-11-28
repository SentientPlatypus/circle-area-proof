from manim import *




class intro_slide(Scene):
    def construct(self):
        tau_tex = MathTex("\\tau", font_size = 144)
        pi_tex = MathTex("\\pi", font_size = 144).shift(RIGHT * 2)
        greater = MathTex(">", font_size = 144)
        quation = MathTex("?", font_size = 144).shift(RIGHT * 4)
        equals = MathTex("=", font_size = 144)
        two_pi = MathTex("2\\pi", font_size = 144).shift(RIGHT * 2)

        self.add(tau_tex)
        self.play(FadeIn(tau_tex), run_time = .5)
        self.play(tau_tex.animate.shift(LEFT * 2))

        self.add(two_pi)
        self.play(FadeIn(two_pi), run_time = .5)

        self.add(equals)
        self.play(FadeIn(equals), run_time = .5)
        self.wait(1.5)

        self.play(Transform(equals, greater),Transform(two_pi, pi_tex),FadeIn(quation),  run_time = 2)
        self.wait(3)


        



class create_initial_circle(Scene):
    def construct(self):
        self.arccolor = YELLOW


        self.r_text = MathTex("r", font_size = 80, color = ORANGE)
        self.big_c = Circle(
            radius= 3.5,
            color= WHITE
        )
        self.a = self.get_arc(0)
        self.radius_line = self.get_radius_line(0)
        self.r_text.next_to(self.radius_line, RIGHT, buff=1.3)
        self.r_text.add_updater(lambda x: x.next_to(self.radius_line, LEFT, buff=1.3))


        group = VGroup(self.a, self.radius_line)

        def zero_to_pi(thegroup, alpha):
            a, r = group
            theta = interpolate(0, PI, alpha)
            if alpha == .5:
                a.set_color(RED)
            a.become(self.get_arc(theta))
            r.become(self.get_radius_line(theta))
        semi_circumference = MathTex("{\\pi}r", font_size = 100, color = YELLOW).shift(UP * 2)

        self.add(self.big_c)
        self.add(self.r_text)
        self.play(
            UpdateFromAlphaFunc(
                group,
                zero_to_pi,
                run_time = 2.5,
                rate_func = rush_from
            ),
            FadeIn(semi_circumference), run_time = 2.5
        )
        self.wait(3)


        def pi_to_tau(thegroup, alpha):
            a, r = group
            theta = interpolate(PI, TAU, alpha)
            a.become(self.get_arc(theta))
            r.become(self.get_radius_line(theta))
        
        semi_circumference2 = semi_circumference.copy().shift(DOWN * 4)
        self.play(
            UpdateFromAlphaFunc(
                group,
                pi_to_tau,
                run_time = 2.5,
                rate_func = rush_from
            ),
            FadeIn(semi_circumference2), run_time = 2.5
        )

        self.wait(2)
        self.big_c.become(Circle(
            radius=3.5,
            color = RED
        ))
        
        tau = MathTex("{\\tau}r", font_size = 100, color = RED).shift(UP * 1)
        

        self.add(self.big_c)
        self.play(
            Transform(semi_circumference, tau),
            FadeIn(self.big_c),
            FadeOut(semi_circumference2),
            FadeOut(self.r_text)
        )
        
        self.wait(3)

    def get_radius_line(self, angle) -> Line:
        return Line(
            self.big_c.get_center(),
            self.big_c.point_at_angle(angle),
            color = ORANGE
        )
    
    def get_arc(self, angle):
        return Arc(
            radius= 3.5,
            angle = angle,
            color = self.arccolor
        )



class listing_scenes(Scene):
    def construct(self):
        tau = MathTex("\\tau", font_size = 120, color = RED).move_to([-5, 2, 0])
        pi = MathTex("\\pi", font_size = 120, color = YELLOW).move_to([5, 2, 0])

        self.add(tau, pi)

        tau_pros = VGroup(
            Text("Unit circle", font_size=30),
            Text("Sinusoids", font_size=30),
            Text("Circumference", font_size=30),
            Text("Arc length", font_size=30)
        ).move_to([-5, 1, 0])


        pi_pros = VGroup(
            Text("Easier to measure diameter", font_size=30),
            Text("We are already using it", font_size=30),
            Text("aReA oF a cIrClE", font_size=30, color = YELLOW),
        ).move_to([4, 1, 0])

        tau_pros.arrange(DOWN, center=False, aligned_edge=LEFT)

        pi_pros.arrange(DOWN, center=False, aligned_edge=LEFT)

        
        for index in range(len(tau_pros)):
            self.play(Write(tau_pros[index]), run_time = .5)
            self.wait(.5)

        for index in range(len(pi_pros)):
            self.play(Write(pi_pros[index]), run_time = .5)
            self.wait(.5)

        self.wait(2)

