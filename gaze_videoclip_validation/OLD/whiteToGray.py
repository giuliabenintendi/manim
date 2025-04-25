from manim import *

class DotDrawingRectangle(Scene):
    def construct(self):
        
        # Define the four corners of the rectangle
        bottom_left = LEFT*3 + DOWN*2
        bottom_right = RIGHT*3 + DOWN*2
        top_right = RIGHT*3 + UP*2
        top_left = LEFT*3 + UP*2
        total_perimeter = 20
        
        # Create a large white dot starting at the bottom left corner
        dot = Dot(point=top_left, color=WHITE, radius=1.2)
        
        # Create a traced path that follows the dot's center (its trajectory)
        path = TracedPath(dot.get_center, stroke_color=BLACK, stroke_width=2)
        self.add(path, dot)
        
        # Create a label that continuously displays the dot's position
        #pos_label = always_redraw(lambda: Text(
         #   f"Position: {np.around(dot.get_center(), 2)}", font_size=24
        #).to_edge(UP))
        #self.add(pos_label)
                
        # The gradient transitions:
        #   - [0, total_perimeter/3]: from YELLOW to RED
        #   - [total_perimeter/3, 2*total_perimeter/3]: from RED to BLUE
        #   - [2*total_perimeter/3, total_perimeter]: from BLUE to YELLOW
        def get_gradient_color(s):
            segment_length = total_perimeter / 3
            if s < segment_length:
                progress = s / segment_length
                return interpolate_color(WHITE, GRAY_B, progress)
            elif s < 2 * segment_length:
                progress = (s - segment_length) / segment_length
                return interpolate_color(GRAY_B, GRAY_D, progress)
            else:
                progress = (s - 2 * segment_length) / segment_length
                return interpolate_color(GRAY_D, WHITE, progress)
            
        # Define a function that maps an arc-length parameter s (from 0 to total_perimeter) to a point along the rectangle
        def rectangle_path(s):
            # First segment: from bottom_left to bottom_right (s in [0,6])
            if s < 6:
                ratio = s / 6
                return interpolate(top_left, top_right, ratio)
            # Second segment: from bottom_right to top_right (s in [6,10])
            elif s < 10:
                ratio = (s - 6) / 4
                return interpolate(top_right, bottom_right, ratio)
            # Third segment: from top_right to top_left (s in [10,16])
            elif s < 16:
                ratio = (s - 10) / 6
                return interpolate(bottom_right, bottom_left, ratio)
            # Fourth segment: from top_left to bottom_left (s in [16,20])
            else:
                ratio = (s - 16) / 4
                return interpolate(bottom_left, top_left, ratio)
        
        # Create a ValueTracker to control the progression along the path
        s_tracker = ValueTracker(0)
        
        # Define an updater for the dot that moves it along the rectangle and updates its colour.
        def update_dot(m, dt):
            current_s = s_tracker.get_value()
            m.move_to(rectangle_path(current_s))
            m.set_color(get_gradient_color(current_s))

        dot.add_updater(update_dot)
        
        self.play(s_tracker.animate.set_value(total_perimeter), run_time=10, rate_func=linear)
        # Remove the updater if you want the dot to stop moving afterward
        dot.clear_updaters()
        self.wait(1)