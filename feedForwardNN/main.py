from manim import *

class FeedforwardNNNNNN(ThreeDScene):
    def construct(self):
        # 🎥 Fix Camera Orientation for a Proper 3D Perspective
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)   # Proper 3D Perspective

        # 🔹 Step 1: Title
        title = Paragraph("How Does a Feedforward", "Neural Network (FNN) Work?",
                          font_size=45, alignment="center", line_spacing=1)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        # 🔹 Step 2: Introduce Brick Wall Concept
        helpers_text = Text("Imagine building a wall, brick by brick...", font_size=32)
        helpers_text.to_edge(UP, buff=1)
        self.play(Write(helpers_text), run_time=1)
        self.wait(1)

        # 🔹 Step 3: Arrows and Processing Data
        task_arrow = Arrow(LEFT * 4, LEFT * 2, buff=0.2, stroke_width=5, color=WHITE)
        task_text = Text("Processing Data", font_size=24).next_to(task_arrow, UP, buff=0.2)

        #self.play(Create(task_arrow), Write(task_text))
        self.play(Write(task_text), run_time=2)

        # 🔹 Step 4: Build the Brick Wall
        BRICK_COLORS = ["#A67B5B", "#8B5A2B", "#6F4F28", "#4E3629"]  # Different shades of brown
        BRICK_STROKE_COLOR = "#3B2E25"  # Dark brown stroke for contrast

        brick_height = 1
        brick_width = 1
        brick_depth = 1

        bricks = VGroup()

        for i in range(4):
            # Create a 3D Brick
            brick = Cube(side_length=brick_width)
            brick.set_fill(color=BRICK_COLORS[i])  # Gradient Effect
            brick.set_stroke(color=BRICK_STROKE_COLOR, width=2)  # Bordeaux Stroke
            # 📌 Align Bricks Perfectly in a Stack
            brick.move_to(UP * (1.5 - i * brick_height))  # Proper Y-axis stacking
            brick.rotate(PI / 1.5, axis=UP)  # Ensure Proper 3D Rotation
            
            # Add Brick to Group and Animate
            bricks.add(brick)
            self.play(DrawBorderThenFill(brick), run_time=0.5)
            # 📌 Center the Entire Brick Wall
        #bricks.move_to(ORIGIN)

        # 🔹 Step 5: Arrows Leading to Final Answer
        processed_data_arrow = Arrow(RIGHT* 2, RIGHT * 4, buff=0.2, stroke_width=5, color=GREEN)
        output_text = Text("to Get the Final Answer!", font_size=24, color=GREEN).next_to(processed_data_arrow,UP, buff=0.2)

        self.play(Create(processed_data_arrow), Write(output_text))
        self.wait(1)

        # 🔹 Step 7: Bricks Dissolve into Neural Network
        self.play(FadeOut(helpers_text, task_text, processed_data_arrow, output_text))

        # 2️⃣ Convert Bricks into Neural Network Nodes (Smooth Morphing)
        input_neurons = VGroup(*[Dot(color=BLUE).shift(LEFT * 3 + UP * y) for y in range(-1, 2)])
        hidden_neurons = VGroup(*[Dot(color=GREEN).shift(UP * y) for y in range(-2, 3)])
        output_neuron = Dot(color=RED).shift(RIGHT * 3)

        neurons = VGroup(input_neurons, hidden_neurons, output_neuron)

        # 🎬 **Bricks Morph into Neurons**
        self.play(Transform(bricks, neurons), run_time=1.5)  # Morphing transition!
        self.wait(1)

        # 🔹 Step 7: Connect the Neurons (Edges Grow in Animation)
        connection_opacity = 0.5  # Adjust opacity (1 = full, 0 = invisible)

        connections = VGroup(
            *[
                Line(inp.get_center(), hid.get_center(), 
                    stroke_color=WHITE,  # Color for each connection
                    stroke_width=2)  # Adjust line thickness if needed
                .set_stroke(opacity=connection_opacity)  # ✅ Correct way to set opacity
                for i, (inp, hid) in enumerate([(i, h) for i in input_neurons for h in hidden_neurons])
            ],
            *[
                Line(hid.get_center(), output_neuron.get_center(), 
                    stroke_color=WHITE, 
                    stroke_width=2)
                .set_stroke(opacity=connection_opacity)  # ✅ Correct opacity setting
                for hid in hidden_neurons
            ]
        )

        # 🎬 **Animate connections appearing smoothly**
        self.play(LaggedStart(*[Create(edge) for edge in connections], lag_ratio=0.1))
        self.wait(1)

        # 🔹 Step 8: Introduce Layer Labels (2D)
        input_label = Text("Input Layer", font_size=24).next_to(input_neurons, LEFT, buff=0.5)
        hidden_label = Text("Hidden Layer", font_size=24).next_to(hidden_neurons, UP, buff=0.35)
        output_label = Text("Output Layer", font_size=24).next_to(output_neuron, RIGHT, buff=0.5)

        self.play(Write(input_label), Write(hidden_label), Write(output_label))
        self.wait(1)

         # 🎬 Step 9: Data Flow Begins (Simulated Input Activation)
        colors = [YELLOW, ORANGE, PURPLE, PINK, BLUE]  # Different input signals
        moving_dots = VGroup()
        # Create dots at input neuron positions
        for i in range(len(hidden_neurons)):  # Ensure we create a dot for each hidden neuron
            dot = Dot(color=colors[i % len(colors)], radius=0.15).move_to(input_neurons[i % len(input_neurons)].get_center())
            moving_dots.add(dot)

        # First, add all dots to the scene
        self.play(FadeIn(moving_dots))

        # Move all dots simultaneously to the hidden neurons
        self.play(
            *[dot.animate.move_to(hidden_neurons[i].get_center()) for i, dot in enumerate(moving_dots)],
            run_time=1
        )

                # Move all dots **simultaneously** to the hidden neurons
        self.play(
            *[dot.animate.move_to(hidden_neurons[i].get_center()) for i, dot in enumerate(moving_dots)],
            run_time=1
        )
        self.wait(0.5)

        # Move dots **from hidden layer to the output neuron**
        self.play(
            *[dot.animate.move_to(output_neuron.get_center()) for dot in moving_dots],
            run_time=1
        )

        self.wait(1)

        # 🎬 Step 13: Highlight Parts of the Formula as Data Moves
        formula_base = MathTex(r"y = f(w \cdot x + b)", font_size=36)  # Use \cdot for multiplication clarity
        formula_base.next_to(hidden_neurons, DOWN, buff=0.2)
        self.play(Write(formula_base), run_time=1)
        self.wait(1)

        # 🎬 Step 10: Highlight Weights & Arrows ONLY WHEN w is Highlighted
        animations_in = []
        animations_out = []

        def highlight_weights(self, connections):
            # 🎬 Step 10: Arrows Light Up + Weights Appear + Reset Color (Sequentially)
            for i, edge in enumerate(connections):
                # Create weight label
                weight_label = MathTex(f"w_{{{i+1}}}", font_size=30).move_to(edge.get_center() + UP * 0.2)

                # **Animate arrow turning yellow & weight appearing**
                self.play(
                    edge.animate.set_color(YELLOW),  # Turn arrow yellow
                    FadeIn(weight_label),  # Show weight
                    run_time=0.3
                )
                # **Fade out weight & reset arrow immediately after showing it**
                self.play(
                    FadeOut(weight_label),  # Remove weight immediately
                    edge.animate.set_color(WHITE),  # Reset arrow color
                    run_time=0.15
                )
                #self.wait(0.1)  # Slight delay before moving to the next weight

        def animate_bias(self, output_neuron):
            # 🎯 **Step 1: Create Bias Arrow & Label**
            bias_arrow = Arrow(
                start=output_neuron.get_bottom() + DOWN * 0.6,  # Start below the output neuron
                end=output_neuron.get_bottom(),  
                color=PINK, stroke_width=4, buff=0.1
            )
        # 🎯 **Step 2: Create Bias Label with Surrounding Box**
            bias_text = Text("Bias", font_size=28, color=PINK)
            bias_box = SurroundingRectangle(bias_text, color=PINK, buff=0.15)
            bias_label = VGroup(bias_text, bias_box).next_to(bias_arrow, DOWN, buff=0.2)

            # 🎯 **Step 3: Animate Bias Arrow & Label**
            self.play(Create(bias_arrow), Write(bias_text), Create(bias_box), run_time=1)
            self.wait(1)

            # 🎯 **Step 4: Optionally Fade Out (Can Remove If You Want It to Stay)**
            self.play(FadeOut(bias_arrow, bias_label), run_time=1)

        # 🎬 Step 11: Highlight Formula Parts (w, x, b) in Correct Order
        highlight_steps = [
            ("w", YELLOW, "Weight (w): Strength of connection", lambda: highlight_weights(self,connections)),
            ("x", BLUE, "Input (x): Data entering the neuron", None),  # x includes cube animation separately
            ("b", PINK, "Bias (b): Helps adjust predictions", lambda: animate_bias(self, output_neuron)),
        ]

        for tex_symbol, color, explanation, extra_animation in highlight_steps:
            new_formula = MathTex(r"y = f(w \cdot x + b)", font_size=36)
            new_formula.next_to(hidden_neurons, DOWN, buff=0.2)
            new_formula.set_color_by_tex(tex_symbol, color)  # Highlight only the specific symbol

            # **Smooth Transition to New Formula**
            self.play(Transform(formula_base, new_formula), run_time=0.5)

            # **Explanation Text**
            explanation_text = Text(explanation, font_size=24, color=color).next_to(formula_base, DOWN, buff=0.25)
            self.play(Write(explanation_text), run_time=2)
            self.wait(0.5)

            # 🎯 Special Animation for "x" (Cubes Representing Inputs)
            if tex_symbol == "x":
                self.play(FadeOut(input_label), run_time=0.3)  # Fade out input layer label
                
                # 🎯 **Create Input Cubes** (Each corresponding to an input neuron)
                input_cubes = VGroup()
                for i, dot in enumerate(input_neurons):
                    cube = Cube(side_length=0.5)
                    cube.set_fill(color=dot.get_color(), opacity=1)
                    cube.set_stroke(color=WHITE, width=2)
                    cube.move_to(dot.get_center() + LEFT * 1.2)  # Offset left for visibility
                    input_cubes.add(cube)

                # 🎯 **Arrows Pointing to Input Neurons**
                input_arrows = VGroup()
                for i, (dot, cube) in enumerate(zip(input_neurons, input_cubes)):
                    arrow = Arrow(start=cube.get_right(), end=dot.get_center(), color=cube.get_fill_color(), buff=0.1)
                    input_arrows.add(arrow)

                # Animate Cubes & Arrows
                self.play(LaggedStart(*[Create(cube) for cube in input_cubes], lag_ratio=0.2), run_time=1.5)
                self.play(LaggedStart(*[Create(arrow) for arrow in input_arrows], lag_ratio=0.2), run_time=1.5)
                self.wait(0.5)

                # 🎯 **Fade Out Input Cubes & Restore Input Label**
                self.play(FadeOut(input_cubes, input_arrows), FadeIn(input_label), run_time=1)

            # 🎯 Special Animation for "w" (Triggers Weight Highlighting)
            if extra_animation:
                extra_animation()  # Call highlight_weights() for w

            # **Fade Out Highlight & Reset**
            self.play(FadeOut(explanation_text), run_time=1)

        # **Final Fade Out**
        self.play(FadeOut(formula_base))

        # 🎬 Step 14: Data Reaches the Output Neuron (Glow Effect)
        self.play(output_neuron.animate.set_color(GREEN), run_time=1)

        # 🎬 Step 15: Change Output Label to "Prediction Made!"
        output_label = Text("Prediction Made!", font_size=32, color=GREEN)
        output_label.to_edge(DOWN, buff=1)
        self.play(Write(output_label), run_time=1)
        self.play(FadeOut(output_label))

        # 🎬 Step 16: Final Summary Text
        final_text = Text("This is how a neural network processes data!", font_size=28)
        final_text.to_edge(DOWN, buff=1)
        self.play(Write(final_text), run_time=1)

        self.wait(0.5)

        # 🎬 Step 17: Fade Out to Prepare for the Next Section
        self.play(FadeOut(neurons, connections, moving_dots,final_text))
        self.wait()