#main
import os
import time
import cv2

#imports
from generate_pdf import GeneratePdf
from chrome import chrome
import subprocess
frames_dir = f"bad_apple_frames"

#wsl bad
def take_screenshot_windows(save_path):
    subprocess.run([
        "powershell.exe",
        "-Command",
        f"Add-Type -AssemblyName System.Windows.Forms; "
        f"$bmp = New-Object System.Drawing.Bitmap([System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width, [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height); "
        f"$graphics = [System.Drawing.Graphics]::FromImage($bmp); "
        f"$graphics.CopyFromScreen(0, 0, 0, 0, $bmp.Size); "
        f"$bmp.Save('{save_path}');"
    ])

def main():
    GenPdf = GeneratePdf(rf"bad_apple.pdf")
    image_files = sorted(os.listdir(frames_dir), key=lambda x: int(x.split('-')[0]))

    for count, image in enumerate(image_files, 1):
        imgpath = os.path.join(frames_dir, image)
        
        if ((count % 30) == 0):
            GenPdf.generate(imgpath)
            print("Found file! make pdf")
            Chrome = chrome(rf"\\wsl.localhost\Ubuntu\home\tegran\Documents\bad_apple\bad_apple.pdf")
            Chrome.open_chrome()
            print("opened")
            time.sleep(3)  
            screenshot_path = rf"C:\Users\boysg\Pictures\bad_apple\bad_apple_image{count // 30}.png"
            take_screenshot_windows(screenshot_path)
            print("time ended making screenshot")
            
            #avoid race condition and pipe blow up
            time.sleep(0.5)  
            Chrome.close_chrome()
            print(f"Did {screenshot_path}")

        else:
            print("ignore")
    print("yay!")


#run main
main()
