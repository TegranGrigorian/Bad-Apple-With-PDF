#main
import os
import asyncio
import pyautogui
from generate_pdf import GeneratePdf
from chrome import chrome

#global -> change these if you want
frames_dir = f"bad_apple_frames"
video_dir = f"bad_apple_video"

# Ensure the screenshot directory exists
os.makedirs(video_dir, exist_ok=True)

def take_screenshot_linux(save_path):
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)

async def main():
    GenPdf = GeneratePdf(rf"bad_apple.pdf")
    image_files = sorted(os.listdir(frames_dir), key=lambda x: int(x.split('-')[0]))

    Chrome = chrome(rf"/home/tegran-grigorian/Documents/Projects/Summer-2025/Bad-Apple-With-PDF/bad_apple.pdf")
    Chrome.open_chrome()
    await asyncio.sleep(2)
    for count, image in enumerate(image_files, 1):
        imgpath = os.path.join(frames_dir, image)
        
        if ((count % 1) == 0): #count % 1 mean its every frame, 30 fps, if you wnat 15 fps you would do % 2
            GenPdf.generate(imgpath)
            print("Found file! make pdf")
            Chrome.reload()
            await asyncio.sleep(1)
            screenshot_path = os.path.join(video_dir, f"frame_{count:04d}.png")
            take_screenshot_linux(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
        else:
            print("Kendale")


main()
asyncio.run(main())