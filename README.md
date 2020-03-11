# nicole_tools

## rename_images.py
#### Parametri
``` -p ``` Percorso della cartella con le immagini da rinominare <br/>
``` -i ``` Percorso delle immagini da rinominare (possibile inserirne più di una separate da spazi) <br/>
``` -n ``` Prefisso che si vuole inserire nel nuovo nome da assegnare alle immagini <br/>
#### Esempi di utilizzo
```
python rename_images.py -p [trascina una CARTELLA qui] -n [prefisso del nome]

python rename_images.py -p /Users/marco/Desktop/prova_nicole -n prefisso
```
oppure
```
python rename_images.py -i [trascina dei FILE IMMAGINE qui] -n [prefisso del nome]

python rename_images.py -i /Users/marco/Desktop/prova_nicole/20200127_081213.jpg /Users/marco/Desktop/prova_nicole/20200127_081246.jpg /Users/marco/Desktop/prova_nicole/20200127_081336.jpg /Users/marco/Desktop/prova_nicole/20200127_081410.jpg /Users/marco/Desktop/prova_nicole/20200127_081440.jpg /Users/marco/Desktop/prova_nicole/20200127_081510.jpg /Users/marco/Desktop/prova_nicole/20200127_081540.jpg /Users/marco/Desktop/prova_nicole/20200127_081610.jpg /Users/marco/Desktop/prova_nicole/20200127_081640.jpg /Users/marco/Desktop/prova_nicole/20200127_081716.jpg -n prefisso
```
## resize_images.py
#### Parametri
``` -p ``` Percorso della cartella con le immagini da ridimensionare <br/>
``` -i ``` Percorso delle immagini da ridimensionare (possibile inserirne più di una separate da spazi) <br/>
``` -w ``` Larghezza desiderata (l'altezza verrà ricalcolata in modo da preservare le proporzioni) <br/>
#### Esempi di utilizzo
```
python resize_images.py -p [trascina una CARTELLA qui] -w [larghezza in pixel] 

python resize_images.py -p /Users/marco/Desktop/prova_nicole -w 512
```
oppure
```
python resize_images.py -i [trascina dei FILE IMMAGINE qui] -w [larghezza in pixel]

python resize_images.py -i /Users/marco/Desktop/prova_nicole/20200127_081213.jpg /Users/marco/Desktop/prova_nicole/20200127_081246.jpg /Users/marco/Desktop/prova_nicole/20200127_081336.jpg /Users/marco/Desktop/prova_nicole/20200127_081410.jpg /Users/marco/Desktop/prova_nicole/20200127_081440.jpg /Users/marco/Desktop/prova_nicole/20200127_081510.jpg /Users/marco/Desktop/prova_nicole/20200127_081540.jpg /Users/marco/Desktop/prova_nicole/20200127_081610.jpg /Users/marco/Desktop/prova_nicole/20200127_081640.jpg /Users/marco/Desktop/prova_nicole/20200127_081716.jpg -w 512
