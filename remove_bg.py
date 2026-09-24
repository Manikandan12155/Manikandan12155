from PIL import Image
import os

files = [
    "ChatGPT Image Sep 24, 2026, 05_17_29 PM.png",
    "ChatGPT Image Sep 24, 2026, 05_19_15 PM.png",
    "ChatGPT Image Sep 24, 2026, 05_20_24 PM.png"
]

out_files = ["img1.png", "img2.png", "img3.png"]

for idx, f in enumerate(files):
    if not os.path.exists(f): 
        print(f"File not found: {f}")
        continue
    img = Image.open(f).convert("RGBA")
    datas = img.getdata()
    new_data = []
    for item in datas:
        # Check if color is close to black
        if item[0] < 20 and item[1] < 20 and item[2] < 20:
            # Optionally blend the alpha to avoid hard edges, but strict cutoff is safer for purely black BG
            new_data.append((item[0], item[1], item[2], 0)) 
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save(out_files[idx], "PNG")
    print(f"Processed {out_files[idx]}")
