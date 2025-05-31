#!/bin/bash

# This script extracts frames from a video file and saves them as images in a specified directory.
ffmpeg -i bad_apple.mp4 bad_apple_frames/%d-video_img.png