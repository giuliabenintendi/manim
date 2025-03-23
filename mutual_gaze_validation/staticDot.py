from manim import *
import numpy as np

class PulsingDot(Scene):
    def construct(self):
        # Parameters for the pulsing effect:
        base_radius = 1.2       # Average radius of the dot
        amplitude = 0.2         # Maximum deviation from the base radius
        frequency = 0.5           # Pulses per second (1 Hz means one full cycle per second)

        # Create the dot at the center (ORIGIN) with an initial radius of base_radius.
        dot = Dot(point=ORIGIN, color=PURE_RED, radius=base_radius)
        self.add(dot)

        # Create a ValueTracker to accumulate time.
        time_tracker = ValueTracker(0)

        # Updater that increments time and updates the dot's size.
        def update_dot(m, dt):
            # Increment the time tracker by the time elapsed since the last frame.
            time_tracker.increment_value(dt)
            t = time_tracker.get_value()

            # Calculate the new radius using a sine function for smooth pulsing.
            # The formula: new_radius = base_radius + amplitude * sin(2π * frequency * t)
            new_radius = base_radius + amplitude * np.sin(2 * np.pi * frequency * t)
            
            # Update the dot's size (width is twice the radius).
            m.set_width(new_radius * 2)
        
        dot.add_updater(update_dot)

        # Let the animation run for 5 seconds to see the pulsing effect.
        self.wait(5)
        dot.clear_updaters()
        self.wait(1)