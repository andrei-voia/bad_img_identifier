import os
from PIL import Image


# defined input
FILE_PATH = "C:\\Users\\PREDATOREL\\Desktop\\Diglett"
bad_mode = ["P"]

# variables
count_registers = 0
count_images = 0
bad_images = 0
mode_array = []
change_array = []


print("\nProgram starting...")
print("Opening \"" + str(FILE_PATH) + "\"...")
print("\nFiles:\n")

for filename in os.listdir(FILE_PATH):
    count_registers += 1
    try:
        im = Image.open(str(FILE_PATH) + "\\" + str(filename))
        image_mode = im.mode
        print(str(filename) + " ->  " + str(image_mode))
        count_images += 1

        for md in mode_array:
            if md[0] == str(image_mode):
                md[1] += 1
                break
        else:
            mode_array.append([image_mode, 1])

        for bad in bad_mode:
            if image_mode == bad:
                bad_images += 1
                current_name = str(FILE_PATH) + "\\" + str(filename)
                new_name = str(FILE_PATH) + "\\bad_image_" + str(bad_images) + ".png"
                change_array.append([current_name, new_name])
                break

    except:
        print("Error: \"" + str(filename) + "\" file not recognized as an image format, skipping...")
print("\nEnd of Files...")


print("\nImage modes:")
for md in mode_array:
    print("[" + str(md[0]) + "] ->  " + str(md[1]) + " images")

print("\nTotal number of files: " + str(count_registers))
print("Total number of images: " + str(count_images))
print("Total number of bad images: " + str(bad_images) + "\n")

if bad_images > 0:
    print("Bad images:")

for bad in change_array:
    print("Image " + str(bad[0]) + "  -(renaming to)->  " + str(bad[1]))
    os.rename(bad[0], bad[1])
    print("Rename completed...")

percent = 100 * (count_images-bad_images) / count_images

print("\nFile %.2f%% good." % percent)