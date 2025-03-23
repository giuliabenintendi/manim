from manim import *

class DotDrawingRectangle(Scene):
    def construct(self):
        
        # Define the four corners of the rectangle
        bottom_left = LEFT * 3 + DOWN * 2
        bottom_right = RIGHT * 3 + DOWN * 2
        top_right = RIGHT * 3 + UP * 2
        top_left = LEFT * 3 + UP * 2
        total_perimeter = 20
        
        # Create a large dot starting at the top left corner with PURE_RED color.
        base_radius = 1.2
        # PULSING PARAMETERS
        pulse_tracker = ValueTracker(0)
        amplitude = 0.2
        frequency = 0.35  
        dot = Dot(point=top_left, color=PURE_RED, radius=base_radius)
        
        # Create a traced path that follows the dot's center (its trajectory)
        path = TracedPath(dot.get_center, stroke_color=BLACK, stroke_width=2)
        self.add(path, dot)
        
        # gradient transitions
        def get_gradient_color(s):
            segment_length = total_perimeter / 3
            if s < segment_length:
                progress = s / segment_length
                return interpolate_color(PURE_RED, YELLOW_C, progress)
            elif s < 2 * segment_length:
                progress = (s - segment_length) / segment_length
                return interpolate_color(YELLOW_C, PURE_BLUE, progress)
            else:
                progress = (s - 2 * segment_length) / segment_length
                return interpolate_color(PURE_BLUE, PURE_RED, progress)
            
        # Define a function that maps an arc-length parameter s (from 0 to total_perimeter) to a point along the rectangle
        def rectangle_path(s):
            # First segment: from top_left to top_right (s in [0,6])
            if s < 6:
                ratio = s / 6
                return interpolate(top_left, top_right, ratio)
            # Second segment: from top_right to bottom_right (s in [6,10])
            elif s < 10:
                ratio = (s - 6) / 4
                return interpolate(top_right, bottom_right, ratio)
            # Third segment: from bottom_right to bottom_left (s in [10,16])
            elif s < 16:
                ratio = (s - 10) / 6
                return interpolate(bottom_right, bottom_left, ratio)
            # Fourth segment: from bottom_left to top_left (s in [16,20])
            else:
                ratio = (s - 16) / 4
                return interpolate(bottom_left, top_left, ratio)
        
        # Create a ValueTracker to control the progression along the path
        s_tracker = ValueTracker(0)
        
        # with pulsing effect
        def update_dot(m, dt):
            current_s = s_tracker.get_value()
            m.move_to(rectangle_path(current_s))
            m.set_color(get_gradient_color(current_s))
            pulse_tracker.increment_value(dt)
            new_radius = base_radius + amplitude * np.sin(2 * np.pi * frequency * pulse_tracker.get_value())
            # Set the dot's width to be twice the current radius (i.e. diameter)
            m.set_width(new_radius * 2)
            
        dot.add_updater(update_dot)
        
        # Animate the ValueTracker from 0 to total_perimeter over 10 seconds.
        self.play(s_tracker.animate.set_value(total_perimeter), run_time=10, rate_func=linear)
        dot.clear_updaters()
        self.wait(1)