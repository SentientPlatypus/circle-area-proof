from manim import *
class credits(Scene):
    def construct(self):
        credit = Text("Credits").to_edge(UL)

        shaun = ImageMobject("W:\Code\Animations\circle-area-proof\Scenes\shaun.jpg").rotate(3 * PI/2)
        shaun.height = 6
        shaun.length = 4
        shaun.shift(RIGHT * 3, DOWN * .5)
        self.play(Write(credit))
        self.add(shaun)
        self.play(
            Create(SurroundingRectangle(shaun, buff = .1, color = WHITE)),
            Write(Text("@shaunteaches", color = YELLOW).move_to(shaun.get_top() + [0, .6, 0]))
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
            ["Ms Blake not caring during CIM", "Peer tutoring club for chips", "Alex DC for constant input"],
            ["Bel for grapes", "David Riccio for lemon squares", "3b1b"]
        ]


        self.play(Write(list))
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
                    run_time = 2
                )