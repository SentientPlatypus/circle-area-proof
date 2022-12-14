from manim import *







class conclusion(Scene):
    def construct(self):
        tau_area = MathTex(
            r"\frac {\tau} {2} r^2",
            font_size =70,
            color = RED
        )

        self.play(Write(tau_area))
        self.wait(1)

        self.play(
            Transform(
                tau_area,
                MathTex(
                    r"\frac {\tau r} {2} r",
                    font_size =70,
                    color = RED
                )
            )
        )
        our_c = Text("The circumference!").shift(UP * 2)

        self.play(
            ShowCreationThenFadeOut(SurroundingRectangle(tau_area[0][0:2], YELLOW, buff = .15)),
            FadeIn(our_c),
            run_time = 2.5
        )

        pi_area = MathTex(
            r"\pi r^2",
            font_size =70,
            color = YELLOW
        )
        self.play(
            FadeOut(tau_area, our_c)
        )
        self.play(Write(pi_area))
        ito_d = Text("In proportion to diameter!").shift(UP * 2)
        arrow_to_pi = Arrow(ito_d, pi_area[0][0])


        raidii = Text("but also multiplies by radius!").shift(DOWN * 2)
        arrow_to_r = Arrow(raidii, pi_area[0][1])

        self.wait(1)
        self.play(
            FadeIn(ito_d),
            Create(arrow_to_pi)
        )
        self.wait(2)
        self.play(
            FadeIn(raidii),
            Create(arrow_to_r)
        )
        self.wait(2)

        gross = Text("Thats disgusting!", color = YELLOW).shift(DOWN * 3)
        self.play(FadeIn(gross))
        self.wait()










class credits(Scene):
    def construct(self):
        credit = Text("Credits").to_edge(UL)

        shaun = ImageMobject("W:\Code\Animations\circle-area-proof\Scenes\shaun.jpg").rotate(3 * PI/2)
        shaun.height = 6
        shaun.length = 4
        shaun.shift(RIGHT * 3, DOWN * .5)
        self.play(Write(credit))
        self.add(shaun)
        surrshaun = SurroundingRectangle(shaun, buff = .1, color = WHITE)
        surrshaun.add_updater(lambda x: x.become(SurroundingRectangle(shaun, buff = .1, color = WHITE)))
        shaunteaches = Text("@shaunteaches", color = YELLOW).move_to(shaun.get_top() + [0, .6, 0])
        shaunteaches.add_updater(lambda x: x.move_to(shaun.get_top() + [0, .6, 0]))
        self.play(
            Create(surrshaun),
            Write(shaunteaches)
            )
        self.wait(2)
        list = BulletedList(
            "Tau vs Pi project",
            "Shaun Errichiello",
            "manim animation gallery",
        ).shift(LEFT * 3)

        list[0].set_color(YELLOW)
        list[1].set_color(RED)
        list[2].set_color(BLUE)

        bullets = [
            ["Ms Blake not caring", "Peer tutoring club snacks", "Alex DC for constant input"],
            ["Bel for grapes", "Project extensions", "Test extension"],
            ["David Riccio for lemon squares", "Lyndon Hess for wearing shoes", "Kieran Shulman for cheez-its"],
            ["Chargers in the library", "Lucine", "chiken nuggets"]
        ]


        self.play(Write(list))
        self.wait(3)
        for bullet in bullets:
            new_list = BulletedList(
                bullet[0],
                bullet[1],
                bullet[2],
            ).move_to(list)
            new_list[0].set_color(YELLOW)
            new_list[1].set_color(RED)
            new_list[2].set_color(BLUE)

            for i in range(len(bullet)):
                self.play(
                    Transform(
                        list[i],
                        new_list[i]
                    ),
                    run_time = 1
                )
                self.wait(2)
        self.play(FadeOut(list))
        self.play(shaun.animate.move_to(ORIGIN))
        self.play(FadeOut(shaun, surrshaun, shaunteaches, credit))
        self.play(Write(Text("Thanks for watching!")))
        self.wait()