from manim import *
import numpy as np

class FixedRectCycle(Scene):
    def construct(self):
        total_duration = 25      # Total duration of the scene in seconds.
        rect_duration = 3        # Duration of each rectangle's cycle (growth + shrink).
        pause_time = 1           # Pause (black screen) between rectangle cycles.
        
        # Set final dimensions for the rectangle.
        rect_width = 1.5
        rect_height = 1.5
        
        # Calculate how many complete cycles fit into total_duration.
        n_rects = int(total_duration // (rect_duration + pause_time))
        
        # Define a fixed list of positions that keep the rectangle within frame bounds.
        fixed_positions = [
            np.array([-6 + rect_width / 2, -3.5 + rect_height / 2, 0]),
            np.array([-3, 0, 0]),
            np.array([0, 3.5 - rect_height / 2, 0]),
            np.array([3, 0, 0]),
            np.array([6 - rect_width / 2, -3.5 + rect_height / 2, 0]),
        ]
        # Log list to record each rectangle’s cycle details.
        rect_log = []
        current_time = 0  # Running time counter in seconds.
        
        for i in range(n_rects):
            # Cycle through fixed_positions if n_rects > len(fixed_positions)
            pos = fixed_positions[i % len(fixed_positions)]
            
            # Create a white rectangle and move it to the fixed position.
            rect = Rectangle(
                width=rect_width,
                height=rect_height,
                color=WHITE,
                fill_color=WHITE,
                fill_opacity=1
            )
            rect.move_to(pos)
            self.add(rect)
            
            # Log the rectangle's cycle details.
            rect_log.append({
                "cycle": i,
                "start_time": current_time,
                "end_time": current_time + rect_duration,
                "position": pos.tolist()
            })
            
            # **Integrate the sound effect:**
            self.add_sound("sounds/new-notification-3-323602.mp3",gain=10,time_offset=1)
            
            # Animate the rectangle's growth (fade in) and then its shrink (fade out).
            self.play(
                GrowFromCenter(rect),
                run_time=rect_duration * 0.3,
                rate_func=smooth
            )
            self.play(
                ShrinkToCenter(rect),
                run_time=rect_duration * 0.7
            )
            
            # Update the running time and wait for the pause period.
            current_time += rect_duration
            self.wait(pause_time)
            current_time += pause_time
        
        # Wait for any remaining time to reach total_duration.
        remaining_time = total_duration - n_rects * (rect_duration + pause_time)
        if remaining_time > 0:
            self.wait(remaining_time)
            current_time += remaining_time