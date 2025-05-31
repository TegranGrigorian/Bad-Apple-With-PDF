#main
import os
import time
import cv2
import asyncio


#imports
from generate_pdf import GeneratePdf
from chrome import chrome
import subprocess
frames_dir = f"bad_apple_frames"

#wsl bad
# def take_screenshot_windows(save_path):
#     subprocess.run([
#         "powershell.exe",
#         "-Command",
#         f"Add-Type -AssemblyName System.Windows.Forms; "
#         f"$bmp = New-Object System.Drawing.Bitmap([System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width, [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height); "
#         f"$graphics = [System.Drawing.Graphics]::FromImage($bmp); "
#         f"$graphics.CopyFromScreen(0, 0, 0, 0, $bmp.Size); "
#         f"$bmp.Save('{save_path}');"
#     ])
async def main():
    GenPdf = GeneratePdf(rf"bad_apple.pdf")
    image_files = sorted(os.listdir(frames_dir), key=lambda x: int(x.split('-')[0]))

    Chrome = chrome(rf"C:\Users\tsarb\Downloads\Bad-Apple-With-PDF-main\bad_apple.pdf")
    Chrome.open_chrome()
    for count, image in enumerate(image_files, 1):
        imgpath = os.path.join(frames_dir, image)
        
        if ((count % 1) == 0):
            GenPdf.generate(imgpath)
            print("Found file! make pdf")
            Chrome.reload()
            await asyncio.sleep(0.2)
            
            
            # async def open_tab(): 
            #     Chrome = chrome(rf"C:\Users\tsarb\Downloads\Bad-Apple-With-PDF-main\bad_apple.pdf")
            #     Chrome.open_chrome()
            #     print("opened")
            #     # time.sleep(3)  
            #     await asyncio.sleep(1)
            #     screenshot_path = rf"./bad_apple_frames/bad_apple_image{count // 30}.png"
            #     # take_screenshot_windows(screenshot_path)
            #     print("time ended making screenshot")
                
            #     #avoid race condition and pipe blow up
            #     Chrome.close_chrome()
            #     print(f"Did {screenshot_path}")
            # await open_tab()
            
        else:
            print("Kendale")




main();
asyncio.run(main())
