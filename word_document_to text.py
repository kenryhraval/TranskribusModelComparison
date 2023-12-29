"""
Python programma Word dokumenta sadalīšanai atsevišķos teksta failos
Izveidota 26.10.2023
Autors Henrijs Kravals
Apraksts: Par ievadi tiek ņemti 5 DOCX faili. Izmantojot ciklu,
Programma pakāpeniski saglabā dokumentu rindkopas 
atsevišķā masīvā līdz tiek uztverts
teksts "image name"; tad masīvā līdz šim saglabātais teksts tiek 
saglabāts atsevišķā teksta failā un masīvs tiek iztukšots. Programma 
šādi turpina darbību, līdz katrs dokuments ir sadalīts atsevišķos 
teksta failos.
"""
import docx
import os

for burts in ["A", "B", "C", "D", "E"]:
    paragraphs = [] # Saglabā tekstu no vienas lapas
    page_num = 0 # Skaitītājs lapu numuram
    doc = docx.Document(f"{burts}.docx") # Ielādē konkrēto Word dokumentu

    # Pārvietoties cauri visiem dokumenta fragmentiem
    for paragraph in doc.paragraphs:
        # Ja sastop "image name" tekstu
        if "image name" in paragraph.text: 
            # Ja jau pabeigta vismaz viena lapa
            if page_num >= 1:
                output_folder = f"pārrakstīti_{burts}"
                # Izveidot rezultātu mapes
                os.makedirs(output_folder, exist_ok=True) 
                # Noteikt rezultātu faila ceļu
                output_file = os.path.join(output_folder, f"{burts}{int(page_num)}.txt")
                # Ieraksta tekstu failā
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write("\n".join(paragraphs))
                    print(f"WRITTEN IN FILE {burts}{page_num}")
                paragraphs = [] # Iztīrīt lapas tekstu
            page_num += 1 # Palielina lapas numuru
        else:
            # Ignorēt nevajadzīgus teksta fragmentus
            if "original page number:" in paragraph.text: pass
            else:
                # Pievienot tekstu fragmentu sarakstam
                if len(paragraph.text) > 0:
                    paragraphs.append(paragraph.text)
