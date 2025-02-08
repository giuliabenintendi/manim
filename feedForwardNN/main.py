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

        self.play(
            Create(processed_data_arrow), Write(output_text))
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

        # 🎯 **Display Each Layer Name with Highlight**
        input_label = Text("Input Layer", font_size=24).next_to(input_neurons, LEFT, buff=0.5)
        hidden_label = Text("Hidden Layer", font_size=24).next_to(hidden_neurons, UP, buff=0.35)
        output_label = Text("Output Layer", font_size=24).next_to(output_neuron, RIGHT, buff=0.5)

        # 🎯 **Create Surrounding Rectangles for Each Layer**
        input_box = SurroundingRectangle(input_neurons, color=BLUE, buff=0.2)
        hidden_box = SurroundingRectangle(hidden_neurons, color=GREEN, buff=0.2)
        output_box = SurroundingRectangle(output_neuron, color=RED, buff=0.2)

        # 🎯 **Animate Input Layer Highlight**
        self.play(Create(input_box), Write(input_label), run_time=0.8)
        self.wait(0.5)
        self.play(FadeOut(input_box), run_time=0.5)

        # 🎯 **Animate Hidden Layer Highlight**
        self.play(Create(hidden_box), Write(hidden_label), run_time=0.8)
        self.wait(0.5)
        self.play(FadeOut(hidden_box), run_time=0.5)

        # 🎯 **Animate Output Layer Highlight**
        self.play(Create(output_box), Write(output_label), run_time=0.8)
        self.wait(0.5)
        self.play(FadeOut(output_box), run_time=0.5)

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
        self.play(FadeOut(moving_dots), run_time=0.5)

        # 🎬 Step 13: Highlight Parts of the Formula as Data Moves
        formula_base = MathTex(r"y = f(w \cdot x + b)", font_size=36)  # Use \cdot for multiplication clarity
        formula_base.next_to(hidden_neurons, DOWN, buff=0.4)
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
                    run_time=0.35
                )
                # **Fade out weight & reset arrow immediately after showing it**
                self.play(
                    FadeOut(weight_label),  # Remove weight immediately
                    edge.animate.set_color(WHITE),  # Reset arrow color
                    run_time=0.25
                )
                self.wait(0.1)  # Slight delay before moving to the next weight

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
            new_formula.next_to(hidden_neurons, DOWN, buff=0.4)
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
        self.play(Transform(new_formula, formula_base.set_color(WHITE)), run_time=0.6)
            
## PART 3      
        # 🎯 Step 3: Create Moving Dots
        moving_dots = VGroup()
        for i in range(len(hidden_neurons) * 2):  # More dots for smoother effect
            dot = Dot(color=BLUE, radius=0.12).move_to(input_neurons[i % len(input_neurons)].get_center())
            moving_dots.add(dot)
        # First, add all dots to the scene
        self.play(FadeIn(moving_dots))
        self.wait(0.5)

        # 🎬 Step 4: Move Dots from Input → Hidden while Activating Edges
        input_to_hidden_animations = []
        for i, dot in enumerate(moving_dots[:len(hidden_neurons)]):  # First set of dots
            edge = connections[i]  # Get corresponding edge (input → hidden)

            input_to_hidden_animations.append(
                AnimationGroup(
                    dot.animate.move_to(hidden_neurons[i % len(hidden_neurons)].get_center()),  # Move dot
                    edge.animate.set_color(BLUE),  # Highlight edge
                    run_time=0.5
                )
            )

        # Play all input → hidden activations in sync
        self.play(LaggedStart(*input_to_hidden_animations, lag_ratio=0.1))

        # Reset connections back to white
        self.play(*[edge.animate.set_color(WHITE) for edge in connections[:len(hidden_neurons)]], run_time=0.3)
        self.wait(0.5)

        # 🎬 Step 5: Move Dots from Hidden → Output while Activating Edges
        hidden_to_output_animations = []
        for i, dot in enumerate(moving_dots[:len(hidden_neurons)]):  
            edge = connections[len(hidden_neurons) + i]  # Get corresponding edge (hidden → output)

            hidden_to_output_animations.append(
                AnimationGroup(
                    dot.animate.move_to(output_neuron.get_center()),  # Move dot to output
                    edge.animate.set_color(BLUE),  # Highlight edge
                    run_time=0.5
                )
            )

        # Play all hidden → output activations in sync
        self.play(LaggedStart(*hidden_to_output_animations, lag_ratio=0.1))

        # Reset connections back to white
        self.play(*[edge.animate.set_color(WHITE) for edge in connections[len(hidden_neurons):]], run_time=0.3)
        self.wait(0.5)

        # 🎯 Step 4: Fade Out Moving Dot
        self.play(FadeOut(moving_dots), run_time=0.5)
        
        original_color = output_neuron.get_color()  # Store original color
        bright_color = YELLOW  # Activation color
        # 🎬 **Pulse Effect Before Activation Formula Appears**
        for _ in range(3):  # Three pulses
            self.play(
                output_neuron.animate.scale(2).set_color(bright_color).set_opacity(0.7),  # Pulse + Glow
                run_time=0.35
            )
            self.play(
                output_neuron.animate.scale(1/2).set_color(original_color).set_opacity(1),  # Reset
                run_time=0.35
            )

        # 🎬 **Build Anticipation at Output Neuron**
        output_glow = output_neuron.copy().scale(2.5).set_color(YELLOW).set_opacity(0.8)  # Persistent Glow

        final_text = Paragraph("Final Computation", "Occurs Here!", 
                               font_size=22, color=YELLOW, alignment="center", line_spacing=1)
        final_text.next_to(output_neuron, UP, buff=0.6)

        self.play(
                Transform(output_neuron, output_glow),
                FadeIn(output_glow), 
                Write(final_text), run_time=1.2)
        self.play(FadeOut(output_glow, final_text), run_time=1)

        # 3️⃣ **Final Text for Clarity**
        explanation_text = Paragraph("The network applies WEIGHTS & BIAS ","to compute the final OUTPUT!", 
                                font_size=20, color=WHITE, alignment="center", line_spacing=1)
        explanation_text.next_to(output_label, DOWN, buff=0.4).shift(RIGHT*0.3)
        self.play(Write(explanation_text), run_time=2)
        self.wait(1)
        self.play(FadeOut(explanation_text), run_time=1)
  
        # Network Activation Function
        network_group = VGroup( input_neurons, hidden_neurons, output_neuron, connections,
                                input_label, hidden_label, output_label, formula_base, new_formula)
        original_network = network_group.copy()  # Store original network for later
        output_neuron = original_network[2][0]  # Get output neuron

         # 📌 Fade Out Network & Prepare for Graph
        self.play(FadeOut(network_group, *self.mobjects))
        self.wait(0.5)

        # 📌 Create the Large Graph (White Background, No Grid)
        activation_graph = Axes(
            x_range=[-6, 6, 1], y_range=[-6, 6, 1], x_length=6, y_length=3,
            tips=True, axis_config={"color": WHITE}  
        ).scale(1.2).move_to(ORIGIN)

        # Add just X and Y axes, **no grid or tick labels**
        x_axis = Line(start=LEFT * 3, end=RIGHT * 3, color=WHITE, stroke_width=3)
        y_axis = Line(start=DOWN * 1.5, end=UP * 1.5, color=WHITE, stroke_width=3)

        # 📌 Define Activation Functions (All in BLUE for consistency)
        activation_functions = [
            ("Sigmoid", lambda x: 1 / (1 + np.exp(-x)), r"Sigmoid: \sigma(x) = \frac{1}{1+e^{-x}}", [-6, 6], [0, 1]),
            ("Linear", lambda x: x, r"Linear: f(x) = x", [-3, 3], [-3, 3]),
            ("ReLU", lambda x: np.maximum(0, x), r"ReLU: f(x) = \max(0, x)", [-3, 3], [-1, 3]),
            ("Tanh", lambda x: np.tanh(x), r"Tanh: \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}", [-3, 3], [-1, 1]),
        ]

        # 📌 Fade in Axes
        activation_title = Text("ACTIVATION FUNCTIONS", font_size=32, color=WHITE)
        activation_title.next_to(activation_graph, UP, buff=1)  # Properly position the text
        self.play(Write(activation_title),
                  Create(x_axis), Create(y_axis), run_time=1)
        self.wait(0.5)

        # Placeholder for function curve & labels
        previous_curve = None
        previous_label = None

        for name,func, formula,x_lim, y_lim in activation_functions:
            # 📌 Create the new function curve
            curve = activation_graph.plot(func, color=BLUE, stroke_width=3)

            # 📌 Position formula label below the graph
            curve_label = MathTex(formula, font_size=30, color=WHITE)
            curve_label.next_to(activation_graph, DOWN, buff=0.5)  # Better positioning

            # 📌 **Smooth Transition Between Functions**
            if previous_curve:
                self.play(
                    FadeOut(previous_curve, previous_label, run_time=1),
                    Transform(previous_curve,curve, run_time= 2), 
                    Transform(previous_label,curve_label, run_time= 2) # Fade out old function
                )
            else:
                self.play(
                    Create(curve),  # Always create new curve
                    Write(curve_label),  # Always write new label
                    run_time=1.5
                )

            previous_curve = curve
            previous_label = curve_label

        # 📌 Fade Out Graph & Restore the Network (Keep Axes)
        self.play(FadeOut(previous_curve, previous_label, *self.mobjects))  
        self.play(Transform(previous_curve, original_network), run_time=1)

        # 📌 Final Prediction Highlight
        output_box = SurroundingRectangle(output_neuron, color=GREEN, buff=0.2)
        prediction_text = Text("FINAL OUTPUT: 87%", font_size=24, color=GREEN).next_to(output_box, UP, buff=0.3)    

        self.play(Create(output_box), Write(prediction_text), run_time=1)
        self.wait(1)
        self.play(FadeOut(formula_base, new_formula), run_time=0.5)

        # 🎯 **Step 4: Fade Out Everything Except Summary Message**
        final_text = Text("This is how a neural network processes data!", font_size=32, color=WHITE)
        final_text.to_edge(DOWN, buff=0.5)

        self.play(Write(final_text), run_time=1.5)
        self.wait(2)

        # 🎯 **Final Fade Out**
        self.play(FadeOut(final_text))
        self.wait(1)