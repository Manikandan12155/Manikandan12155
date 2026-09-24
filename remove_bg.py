from PIL import Image
import os

files = [
    r"C:\Users\ATL-037\.gemini\antigravity-ide\brain\75a979ce-96f7-488a-82e9-e2df8c69844b\intro_avatar_1_1790253685679.jpg",
    r"C:\Users\ATL-037\.gemini\antigravity-ide\brain\75a979ce-96f7-488a-82e9-e2df8c69844b\intro_avatar_2_1790253697582.jpg",
    r"C:\Users\ATL-037\.gemini\antigravity-ide\brain\75a979ce-96f7-488a-82e9-e2df8c69844b\intro_avatar_3_1790253710784.jpg",
    r"C:\Users\ATL-037\.gemini\antigravity-ide\brain\75a979ce-96f7-488a-82e9-e2df8c69844b\intro_avatar_4_1790253724873.jpg"
]
out_files = ["intro1.png", "intro2.png", "intro3.png", "intro4.png"]

for idx, f in enumerate(files):
    if not os.path.exists(f): 
        print(f"File not found: {f}")
        continue
    img = Image.open(f).convert("RGBA")
    datas = img.getdata()
    new_data = []
    for item in datas:
        if item[0] < 20 and item[1] < 20 and item[2] < 20:
            new_data.append((item[0], item[1], item[2], 0)) 
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save(out_files[idx], "PNG")
    print(f"Processed {out_files[idx]}")
