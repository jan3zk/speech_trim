# Prirezovalnik govornih posnetkov

Aplikacija za samodejno prirezovanje začetnih in končnih premorov govornih posnetkov v datotekah WAV.

## Namestitev

Koda je spisana v programskem jeziku Python 3. Zahtevane knjižnice se namesti z ```pip install -r requirements.txt```.

V izogib težavam pri namestitvi zahtevanih programskih knjižnic sta pripravljeni izvršljivi datoteki za okolje [Windows](https://unilj-my.sharepoint.com/:u:/g/personal/janezkrfe_fe1_uni-lj_si/EaNnS2K1PDVBgyxRaBsGDJkBwNoskeiKRn5d0jpYwnWPEA?e=WkiOcG) in [Linux](https://unilj-my.sharepoint.com/:u:/g/personal/janezkrfe_fe1_uni-lj_si/ERn_1ke8rhJDs35dFGoRV6UBoRM8spPcX4BR8TEDmj7fJQ?e=we7aCz), ki ne potrebujeta namestitve knjižnic. Izvršljva datoteka se nahaja znotraj stisnjene mape na prejšnji povezavi in se je ne sme premikati napram ostalim knjižnicam v mapi. Po razširitvi mape .zip, izvršljivo datoteko v okolju Windows kličemo z ukazom ```speech_trim.exe <vhodni argumenti>```, v okolju Linux pa z ```./speech_trim <vhodni argumenti>```, pri čemer so vodni argumenti enaki kot pri klicu Python skripte, opisanem v nadaljevanju.

## Uporaba

Prirez večih posnetkov naenkrat je mogoč s klicem ```python speech_trim.py -i izvorni/posnetki/ -o prirezani/posnetki/```, kjer v vhodnih argumentih podamo mapo s posnetki, ki jih želimo prirezati in mapo, kamor se bodo prirezani posnetki shranili. Prirez posameznega posnetka izvedemo s klicem  ```python speech_trim.py -i izvorni_posnetek.wav -o prirezani_posnetek.wav```.

### Opcijski vhodni argumenti

Argument ```-v``` omogoča vkjučitev izrisa grafa glasnosti obravnavanega govornega posnetka. Z argumentom ```-p <float>``` nastavimo želeno dolžino začetnega/končnega premora, pri čemer je ```<float>``` decimalna vrednost v sekundah (prednastavljena vrednost je ```0,8```). Argument ```-t <int>``` omogoča nastavitev pragu tišine v dBFS (prednastavljena vrednost ```-34```). Z ```-c <int>``` pa lahko nastavimo dolžino odseka v ms znotraj katerega postopek po korakih išče začetek/konec govora (prednastavljena vrednost ```20```).
