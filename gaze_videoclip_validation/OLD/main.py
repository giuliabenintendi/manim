from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips
from utils import find_manim_outputs  # The helper function above
import os

# Suppose we want to load "FixedPositionsCycle" scene outputs.
scene_name = "FixedPositionsCycle"

video_path, sound_path = find_manim_outputs(scene_name, resolution="1080p60")

if video_path is None:
    raise FileNotFoundError(f"Unable to locate video for scene {scene_name}.")

# Load the video with MoviePy.
clip = VideoFileClip(video_path)

# If the sound path exists, attach the audio to the clip.
if sound_path and os.path.exists(sound_path):
    audio = AudioFileClip(sound_path)
    clip = clip.set_audio(audio)

# At this point, clip has the video and audio from the Manim render.
clip.preview()  

# Write out a combined video if you need to:
clip.write_videofile("final_output.mp4", fps=24, codec="libx264")