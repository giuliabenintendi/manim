import os
import sys
import subprocess
from moviepy import VideoFileClip, ColorClip, CompositeVideoClip

# ---------------------------
# Configuration Parameters
# ---------------------------
cartoons_folder = "/Users/giuliabenintendi/Documents/manim/gaze_videoclip_validation/cartoons"
output_folder = "/Users/giuliabenintendi/Documents/manim/gaze_videoclip_validation/output"
os.makedirs(output_folder, exist_ok=True)

# Loop over all .mp4 files in the cartoons folder
for video_name in sorted(os.listdir(cartoons_folder)):
    if video_name.lower().endswith(".mp4"):
        input_file = os.path.join(cartoons_folder, video_name)
        # Build new filenames for the re-encoded and composite video
        reencoded_file = os.path.join(cartoons_folder, f"reencoded_{video_name}")
        output_file = os.path.join(output_folder, f"resized_{video_name}")

        # Check if the current input file exists (should be true in the loop)
        if not os.path.exists(input_file):
            sys.exit(f"Error: The input file {input_file} does not exist. Please check the path and filename.")

        # ---------------------------
        # Re-encode and Scale the Video Using ffmpeg
        # ---------------------------
        # The ffmpeg command scales the video so that it fits within a 320x180 box while preserving its aspect ratio.
        ffmpeg_command = [
            "ffmpeg",
            "-i", input_file,
            "-vf", "scale=320:180:force_original_aspect_ratio=decrease",
            "-c:v", "libx264",
            "-c:a", "aac",
            reencoded_file
        ]
        print(f"\nProcessing file: {input_file}")
        print("Re-encoding and scaling the video using ffmpeg...")
        subprocess.run(ffmpeg_command, check=True)
        print("Re-encoding and scaling completed.")

        # ---------------------------
        # Process the Re-encoded Video with MoviePy
        # ---------------------------
        # Load the re-encoded video.
        clip = VideoFileClip(reencoded_file)

        # Create a black background of size 1280x720.
        background = ColorClip((1280, 720), color=(0, 0, 0), duration=clip.duration)

        # Compute composite position:
        #   Center horizontally and shift vertically downward (offset of 50 pixels).
        offset = 50  # Change this value to adjust vertical position.
        pos_x = (1280 - clip.w) / 2
        pos_y = (720 - clip.h) / 2 + offset

        # Composite the scaled video onto the background at the computed position.
        final_clip = CompositeVideoClip(
            [background, clip.with_position((pos_x, pos_y))],
            size=(1280, 720)
        )

        # ---------------------------
        # Write the Output Video
        # ---------------------------
        print(f"Writing the composite video file: {output_file} ...")
        final_clip.write_videofile(output_file, fps=24, codec="libx264")
        print(f"Composite video has been saved as: {output_file}")