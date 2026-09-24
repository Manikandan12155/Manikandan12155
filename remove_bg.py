from PIL import Image
import os

in_file = "ChatGPT Image Sep 24, 2026, 05_59_19 PM.png"
out_file = "img5.png"

if os.path.exists(in_file):
    img = Image.open(in_file).convert("RGBA")
    datas = img.getdata()
    new_data = []
    for item in datas:
        if item[0] < 20 and item[1] < 20 and item[2] < 20:
            new_data.append((item[0], item[1], item[2], 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save(out_file, "PNG")
    print(f"Processed {out_file}")
else:
    print(f"File not found: {in_file}")
