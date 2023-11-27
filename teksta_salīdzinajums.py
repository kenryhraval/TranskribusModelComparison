# Nepieciešamās Python bibliotēkas
import pandas as pd
from tabulate import tabulate

def levenshtein_distance(s, t):
    m = len(s)
    n = len(t)
    d = [[0] * (n + 1) for i in range(m + 1)]  

    for i in range(1, m + 1):
        d[i][0] = i

    for j in range(1, n + 1):
        d[0][j] = j
    
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,          # deletion
                          d[i][j - 1] + 1,          # insertion
                          d[i - 1][j - 1] + cost)   # substitution   
    return d[m][n]

def tokenize_and_ignore_symbols(text):
    # Noņemt rindu atdalītajus
    text = text.replace('\n', ' ')
    # Neiekļaut tokenos punktuāciju
    ignore_symbols = [",", ".", "-", ";", "¬", "_", "!", "?", ":", "/", "&", "(", ")"]
    
    # Izveidot simbolu virkni, kas satur visus ignorējamos simbolus
    ignore_chars = ''.join(ignore_symbols)

    # Aizstāt ignorējamos simbolus ar tukšumu
    for char in ignore_chars:
        text = text.replace(char, ' ')

    # Sadalīt tekstu pēc tukšuma
    tokens = text.split()

    return tokens

def aprekins(txtM, txt):
    # Teksta apvienošana simbolu virknē, pārvēršot mazajos burtos
    txtM = ''.join(txtM).lower()
    txt = ''.join(txt).lower()
    
    # Teksta tokenizācija, neņemot vērā punktuāciju
    txtM_tokens = tokenize_and_ignore_symbols(txtM)
    txt_tokens = tokenize_and_ignore_symbols(txt)
    
    # CER aprēķināšana ar Levenšteina attālumu
    cer = levenshtein_distance(txtM, txt) / len(txtM)

    # WER aprēķināšana ar Levenšteina attālumu
    wer = levenshtein_distance(txtM_tokens, txt_tokens) / len(txtM_tokens)

    return wer, cer

for burts in ["A", "B", "C", "D", "E"]:
    # Katram modelim izveidots tukšs masīvs
    results = []
    
    # Cikls iziet cauri visiem konkrētā modeļa teksta failiem
    for i in range(1, 101):
        # .txt paplašinajuma failu nolasīšana
        txtM = open(f"pārrakstīti_M/M{i}.txt", 'r', encoding='utf-8').readlines()
        txt = open(f"pārrakstīti_{burts}/{burts}{i}.txt", 'r', encoding='utf-8').readlines()

        # Funkcijas "aprekins" izsaukšana
        wer, cer = aprekins(txtM, txt)
        # Rezultātu masīva ievietošana sākotnējā masīvā 
        results.append([i, wer, cer])

    # Cikla beigās divdimensiju masīvs tiek pārveidots par tabulu 
    # ".csv" failu paplašinājumā izmantojot "pandas" bibliotēku
    df = pd.DataFrame(results, columns=["Attēls", "WER", "CER"])
    df.to_csv(f"rezultāti_{burts}.csv", index=False)

    headers = ["Attēls", "WER", "CER"]
    print(f"Rezultāti modelim {burts}:")
    print(tabulate(results, headers, tablefmt="grid"))
