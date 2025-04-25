from manim import *
import random
import numpy as np

def random_bright_color():
    colors = [PURE_RED, BLUE_C, YELLOW, PURE_GREEN, PINK, ORANGE]
    return random.choice(colors)

class FixedPositionsCycle(Scene):
    def construct(self):
        total_duration = 25      # Total duration of the scene in seconds.
        dot_duration = 3         # Duration of one dot cycle (growth + fade-out).
        pause_time = 1           # Pause after a dot cycle.
        n_dots = int(total_duration // (dot_duration + pause_time))
        dot_radius = 1           # Radius for our dot; ensures valid position bounds.
        
        # Define fixed positions (within a frame with x in [-6+radius, 6-radius], 
        # and y in [-3.5+radius, 3.5-radius]).
        fixed_positions = [
            np.array([-5, -2.5, 0]),
            np.array([-3,  0.0,  0]),
            np.array([-1,  2.5,  0]),
            np.array([ 1, -2.5, 0]),
            np.array([ 3,  0.0,  0]),
            np.array([ 5,  2.5, 0])
        ]
        
        # Log list to record each dot's display details.
        dot_log = []
        current_time = 0  
        
        for i in range(n_dots):
            pos = fixed_positions[i]
            color = random_bright_color()  
            
            # Create the dot at the fixed position.
            dot = Dot(point=pos, color=color, radius=dot_radius)
            star = Star(color=color, radius=dot_radius)
            self.add(dot)
            
            # Log the dot cycle with start and end times.
            dot_log.append({
                "cycle": i,
                "start_time": current_time,
                "end_time": current_time + dot_duration,
                "position": pos.tolist()
            })

            # Play the sound as soon as the dot appears.
            self.add_sound("sounds/new-notification-3-323602.mp3",gain=10,time_offset=1)
            # Animate the dot growth (fade in) and shrink (fade out).
            self.play(
                GrowFromCenter(dot),
                run_time=dot_duration * 0.6,
                rate_func=smooth
            )
            self.play(
                ShrinkToCenter(dot),
                run_time=dot_duration * 0.4
            )
            
            # Update time and wait for the pause period.
            current_time += dot_duration
            self.wait(pause_time)
            current_time += pause_time
        
        remaining_time = total_duration - n_dots * (dot_duration + pause_time)
        if remaining_time > 0:
            self.wait(remaining_time)
            current_time += remaining_time