import os
import sys
import rawpy
import imageio

directory = input("Directory path: ").rstrip("//")

if not os.path.isdir(directory):
    sys.exit("You have entered an invalid directory...")

directory_files = os.listdir(directory)
directory_upload_path = directory + "/converted/"

if not os.path.isdir(directory_upload_path):
    os.mkdir(directory_upload_path)

for fn in os.listdir(directory):
    if fn.endswith(".ARW"):
        print("Converting " + fn + "... ", end = "", flush=True)

        path = os.path.join(directory, fn) 
        filename = fn[:-3] + "JPEG"

        with rawpy.imread(path) as raw:
            rgb = raw.postprocess(use_camera_wb=True)
            raw.close()
        imageio.imwrite(directory_upload_path + filename, rgb, "JPEG")
        print("[COMPLETED]")
    else:
        continue