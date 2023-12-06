# TranskribusModelComparison
Faili zinātniski pētnieciskā darba praktiskajai daļai par Transkribus vietnē esošo HTR Transkribus modeļu izmantošanu Latvijas arhīvā esošo vēsturisko dokumentu teksta satura digitalizācijai.

- Mape ierakstu_attēli satur 100 atlasītos baznīcu grāmatu ierakstus atlase no LNA tiešsaistes vietnes. Atlasīti Džūkstes latviešu ev. lut. draudzes kristību ieraksti vācu valodā par laika periodu no 1835. līdz 1880. gadam. No katra piektā gada izvēlēti pirmie 10 ieraksti. Katram ierakstam tika veikts ekrānuzņēmums, saglabāts ar nosaukumu, kas atbilst tā numuram.

- Mape pārrakstīti_M satur manuāli pārrakstītos teksta failus. To nosaukumā esošais kārtas skaitlis atbilst parrakstītā attēla numuram.

- Mapes pārrakstīti_A, pārrakstīti_B, pārrakstīti_C, pārrakstīti_D, pārrakstīti_E satur modeļu pārrakstītos tekstus. Teksta failu nosaukumā ietvers kārtas skaitlis, kas atbilst pārrakstītā attēla numuram. Izmantotie 5 Transkribus programmatūrā esošie vācu valodas HTR modeļi: “German_Kurrent_17th-18th” (A), “Transkribus German handwriting M1” (B), “The Text Titan I” (C), “Early Kurrent Emperor I.” (D) un “The German Giant I” (E).

- Python fails word_document_to_text izmantots pārrakstīto tekstu pārnešanai no .docx faila uz vairākiem .txt failiem jeb tekstu sadalīšanai.

- Mape word_format_ABCDE satur sākotnējos katra modeļa .docx failus. Nosaukumi atbilst konkrētā modeļa burtam.

- Python fails teksta_salīdzinajums izmantots snieguma mēru (CER un WER) vērtību noteikšanai. Tas par ievadi ņem mapju pārrakstīti_A, pārrakstīti_B, pārrakstīti_C, pārrakstīti_D, pārrakstīti_E teksta failus un salīdzina tos ar atbilstošajiem mapē pārrakstīti_M esošajiem teksta failiem. 

- Mape results_csv_format satur faila teksta_salīdzinajums izveidotās, rezultātus saturošās tabulas.
