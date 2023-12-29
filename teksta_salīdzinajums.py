"""
Python programma CER un WER vērtību noteikšanai
Izveidota 25.10.2023
Autors Henrijs Kravals
Apraksts: Par ievadi tiek ņemta mape ar 100 teksta failiem 
(manuāli pārrakstītie teksti) un 5 mapes, kurās katrā ir
100 teksta faili (modeļu atpazītie teksti). Izmantojot funkciju 
token_ign, iegūti teksta failu vārdus saturoši masīvi, izmantojot funkciju lev_att,
aprēķināti Levenšteina attālumi, funkcija aprekins aprēķina CER
un WER vērtības starp modeļu atpazītajiem tekstiem un manuāli
pārrakstītiem tekstiem. Rezultāti saglabāti 5 CSV failos.

Levenšteina attālumam izmantotais algoritms:
https://python-course.eu/applications-python/levenshtein-distance.php
"""

import pandas as pd

def lev_att(s, t):
    # Aprēķina Levenšteina attālumu starp virknēm s un t
    m = len(s)
    n = len(t)
    d = [[0] * (n + 1) for i in range(m + 1)]  

    # Inicializē matricas pirmo rindu un kolonnu
    for i in range(1, m + 1):
        d[i][0] = i

    for j in range(1, n + 1):
        d[0][j] = j
    
    # Aizpilda matricu, izmantojot dinamisko programmēšanu
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,          # dzēšana
                          d[i][j - 1] + 1,          # ievietošana
                          d[i - 1][j - 1] + cost)   # aizvietošana   
    
    # Atgriež Levenšteina attālumu starp divām virknēm
    return d[m][n]

def token_ign(text):
    # Noņemt rindu atdalītajus
    text = text.replace('\n', ' ')
    # Neiekļaut tokenos punktuāciju
    ign_punkt = [",", ".", "-", ";", "¬", "_", "!", "?", ":", "/", "&", "(", ")"]
    
    # Izveidot simbolu virkni, kas satur visus ignorējamos simbolus
    ign_virkne = ''.join(ign_punkt)

    # Aizstāt ignorējamos simbolus ar tukšumu
    for char in ign_virkne:
        text = text.replace(char, ' ')

    # Sadalīt tekstu pēc tukšuma
    tokens = text.split()

    return tokens

def aprekins(txtM, txt):
    # Teksta apvienošana simbolu virknē, pārvēršot mazajos burtos
    txtM = ''.join(txtM).lower()
    txt = ''.join(txt).lower()
    
    # Teksta tokenizācija, neņemot vērā punktuāciju
    txtM_tokens = token_ign(txtM)
    txt_tokens = token_ign(txt)
    
    # CER aprēķināšana ar Levenšteina attālumu
    cer = lev_att(txtM, txt) / len(txtM)

    # WER aprēķināšana ar Levenšteina attālumu
    wer = lev_att(txtM_tokens, txt_tokens) / len(txtM_tokens)

    return wer, cer

for burts in ["A", "B", "C", "D", "E"]:
    # Katram modelim izveidots tukšs masīvs
    rezult = []
    
    # Cikls iziet cauri visiem konkrētā modeļa teksta failiem
    for i in range(1, 101):
        # .txt paplašinajuma failu nolasīšana
        txtM = open(f"pārrakstīti_M/M{i}.txt", 'r', encoding='utf-8').readlines()
        txt = open(f"pārrakstīti_{burts}/{burts}{i}.txt", 'r', encoding='utf-8').readlines()

        # Funkcijas "aprekins" izsaukšana
        wer, cer = aprekins(txtM, txt)
        # Rezultātu masīva ievietošana sākotnējā masīvā 
        rezult.append([i, wer, cer])

    # Cikla beigās divdimensiju masīvs tiek pārveidots par tabulu 
    # CSV failu paplašinājumā izmantojot "pandas" bibliotēku
    df = pd.DataFrame(rezult, columns=["Attēls", "WER", "CER"])
    df.to_csv(f"rezultāti_{burts}.csv", index=False)
