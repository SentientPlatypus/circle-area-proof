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


class pid(Scene):
    def construct(self):
        self.circ = Circle(
            radius = 3.5,
            fill_opacity = 0,
            color = WHITE
        )
        pid = MathTex(r"\pi d")

        self.play(Create(self.circ))
        self.play(Write(pid))
        self.wait()


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

class SineCurveUnitCircle(MovingCameraScene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.camera:MovingCamera
        self.camera.frame.save_state()


        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

        self.circle = Circle(radius=1)
        self.circle.move_to(self.origin_point)
        self.add(self.circle)
        self.camera.frame.set(width = self.circle.radius * 2 + 1, height = self.circle.radius * 2 + 1)
        # ghost_circle = Circle(radius=1.2, fill_opacity = 0)
        # self.add(ghost_circle)
        self.play(
            self.camera.frame.animate.move_to(self.circle)
        )
        self.play(Write(MathTex(r"\frac {\tau} {4}", font_size = 20).move_to(self.circle.get_top())))
        self.play(Write(MathTex(r"\frac {\tau} {2}", font_size = 20).move_to(self.circle.get_left())))
        self.play(Write(MathTex(r"\frac {3\tau} {4}", font_size = 20).move_to(self.circle.get_bottom())))
        self.play(Write(MathTex(r"\tau", font_size = 20).move_to(self.circle.get_right())))
        self.show_axis()
        self.play(Restore(self.camera.frame))

        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.play(Create(x_axis), Create(y_axis))
        self.add_x_labels()

    def add_x_labels(self):
        x_labels = [
            MathTex(r"\frac {\tau} {2}"), MathTex(r"\tau}"),
            MathTex(r"\frac {3\tau} {2}"), MathTex(r"2\tau"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])


    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

class exampleSine(Scene):
    def construct(self):
        sinfunc = MathTex(
            r"f(x) = \sin\left(",
            r"\frac {\tau} {4}",
            r"x \right)",
            color = WHITE
        )
        sinfunc[1].set_color(RED)
        self.play(Write(sinfunc))
        self.wait(1)
        self.play(
            ShowCreationThenFadeOut(SurroundingRectangle(sinfunc[1][0]))
        )
        self.play(ShowCreationThenFadeOut(SurroundingRectangle(sinfunc[1][2])))
        
        self.play(
            Transform(
                sinfunc[1],
                MathTex(
                    r"\frac {\pi} {2}",
                    color = YELLOW
                ).move_to(sinfunc[1])
            )
        )
        self.wait()

