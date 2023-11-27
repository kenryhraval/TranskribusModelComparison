import docx
import os

# Programmas darbībai Word dokumenta 
# beigās iekopēt "image name"
for burts in ["A", "B", "C", "D", "E"]:
    paragraphs = []
    page_num = 0
    doc = docx.Document(f"{burts}.docx")

    for paragraph in doc.paragraphs:
        if "image name" in paragraph.text: 
            if page_num >= 1:
                output_folder = f"pārrakstīti_{burts}"
                os.makedirs(output_folder, exist_ok=True)
                output_file = os.path.join(output_folder, f"{burts}{int(page_num)}.txt")
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write("\n".join(paragraphs))
                    print(f"WRITTEN IN FILE {burts}{page_num}")
                paragraphs = []
            page_num += 1
        else:
            if "original page number:" in paragraph.text: pass
            else:
                if len(paragraph.text) > 0:
                    paragraphs.append(paragraph.text)
                    print(f"Adding {paragraph.text} to page {page_num}")

    print(f'MODEL {burts} FINISHED')
print("Done.")

