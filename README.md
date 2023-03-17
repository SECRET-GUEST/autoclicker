Autoclicker version BETA | Python version 3.11.1 | 🇫🇷 | For OS running autoclickers so better on Windows 
```
██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗     ██████╗ ██████╗ ██╗   ██╗██╗  ██╗
██║  ██║██╔══██╗██╔══██╗██╔══██╗██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗██║   ██║██║  ██║
███████║███████║██████╔╝██║  ██║██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗    ██████╔╝██████╔╝██║   ██║███████║
██╔══██║██╔══██║██╔══██╗██║  ██║██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║    ██╔══██╗██╔══██╗██║   ██║██╔══██║
██║  ██║██║  ██║██║  ██║██████╔╝╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝    ██████╔╝██║  ██║╚██████╔╝██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                                                                                                                              

```


# Autoclicker 

Un autoclicker /keylogger pour répéter l'ensemble des actions sur votre pc

```
___ _  _ ___ ____ ____ _ ____ _    
 |  |  |  |  |  | |__/ | |__| |    
 |  |__|  |  |__| |  \ | |  | |___ 
                                   
```

Voici un tutoriel expliquant les différentes façons d'exécuter les fichiers :


# Pour les utilisateurs de **MAC** & **Linux** :

Comme ce script est conçu pour les utilisateurs de Windows, vous devriez probablement commencer par améliorer le code.

Voici cependant la procédure à suivre pour exécuter le script :

* [ MAC ] ; https://macosx-faq.com/how-to-run-python-script/
* [ LINUX ] ; ouvrir un terminal puis `cd` jusqu'au script et taper :

```
python script.pyw
```
(où `script.pyw` est évidemment le nom de ce que vous avez téléchargé)


# Pour les utilisateurs microsoft;

Comme ce script est créé par pyinstaller, il pourrait être détecté comme un logiciel malveillant puisque non signé, mais il n'en est rien, de toute manières vous avez le code.

Voici les possibilités d'exécuter le script ; 

## 1. En cliquant simplement sur l( APPLICATION.exe

Le fichier `.exe` est une version portable faite pour les utilisateurs de Microsoft avec pyinstaller, vous ne pouvez télécharger que ce fichier et rien d'autre.

## 2. Lancer avec Python

`Script` est un répertoire contenant le script original pour python 3.11. 

Si vous avez une version inférieure, vous devrez peut-être télécharger des modules importés qui ne sont pas inclus dans votre version. 

Il suffit de lire les premières lignes du script sous l'installation avec un editeur de texte (visual studio code, ...) ou autre pour trouver ce qui manque.

Si vous souhaitez utiliser python **Vous aurez besoin de l'image `.png` placée dans le dossier `ico`**.

Vous pouvez également ajouter un `w` à l'extension (comme `script.pyw`). Cela signifie `windowed mode`, pour lancer le script python sans le CMD mais c'est toujours un fichier python commun.


## 3. Compiler le script vous meme

### Instructions 

Pour créer votre propre exécutable à partir du fichier python, vous devez installer pyinstaller et python. 

Voici les étapes à suivre :

* Télécharger python 3.11.1

N'oubliez pas de l'ajouter à votre chemin d'accès avec l'installeur ou dans l'environnement des variables ( donc redémarrez votre PC après l'installation ), voici le lien : https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

* Ouvrez votre CMD en tant qu'administrateur et tapez la commande suivante :

```
python -m pip install pyinstaller
```

* Une fois l'installation terminée, tapez la commande suivante dans votre fenêtre cmd, en remplaçant les chemins d'accès aux fichiers par les vôtres :

```
pyinstaller --onefile --icon="...YOUR PATH.../YOUR ICON.ico" --add-data "...YOUR PATH.../ico;ico" --noconsole test.py

```

Voici l'explication des différentes options :

- `--onefile` : crée un seul exécutable qui inclut toutes les dépendances.

- `--icon=icon.ico` : spécifie l'icône à utiliser pour l'exécutable (remplacez icon.ico par le chemin vers votre fichier d'icône).

- `--add-data "path/to/file;folder_name"` :

ajoute les fichiers externes requis par le programme. Le chemin d'accès au fichier et le nom du dossier dans lequel le fichier sera extrait doivent être séparés par un point-virgule `;`. Vous pouvez ajouter plusieurs fichiers en les séparant par des points-virgules.

- ` script.py` : spécifie le nom de votre script Python.

- ` --noconsole` : cache la console lorsque l'exécutable est lancé.

Veillez à remplacer les parties coupées par les noms de vos fichiers et dossiers. Notez également que le chemin d'accès doit être spécifié en fonction du système d'exploitation sur lequel vous travaillez.

Après avoir exécuté cette commande, vous devriez avoir un seul exécutable qui inclut toutes les dépendances, les fichiers externes et une icône personnalisée, et qui n'affiche pas la console lors de l'exécution.

Vous pouvez également :

## 4. Créer un fichier batch à exécuter 

- [ ] Créer un fichier texte

- [ ] Dans le fichier texte, tapez et écrivez (et changez/complétez le chemin, le premier est pour python, le second pour script.py) ;

```
C:\YOUR PATH TO PYTHON \python.exe" "C:\ **YOUR PATH TO THE SCRIPT** \script.pyw"
```

Si Python est dans le chemin, vous pouvez simplement ; 

```
python "C:\ **YOUR PATH TO THE SCRIPT** \script.pyw"
```

- [ ] Renommez le `new_file.txt` par `script.bat` puis cliquez simplement sur et le programme s'exécutera.

```
     _ ._  _ , _ ._            _ ._  _ , _ ._    _ ._  _ , _ ._      _ ._  _ , _ .__  _ , _ ._   ._  _ , _ ._   _ , _ ._   .---.  _ ._   _ , _ .__  _ , _ ._   ._  _ , _ ._      _ ._  _ , _ .__  _ , _ . .---<__. \ _
   (_ ' ( `  )_  .__)        (_ ' ( `  )_  .__ (_ ' ( `  )_  .__)  (_ '    ___   ._( `  )_  .__)  ( `  )_  .__)   )_  .__)/     \(_ ' (    )_  ._( `  )_  .__)  ( `  )_  .__)  (_ ' ( `  )_  ._( `` )_  . `---._  \ \ \
 ( (  (    )   `)  ) _)    ( (  (    )   `)  ) (  (    )   `)  ) _ (  (   (o o) )     )   `)  ) _    )   `)  ) _    `)  ) \.@-@./(  (    )   `)     )   `)  ) _    )   `)  ) _ (  (    )   `)         `) ` ),----`- `.))  
(__ (_   (_ . _) _) ,__)  (__ (_   (_ . _) _) _ (_   (_ . _) _) ,__ (_   (  V  ) _) (_ . _) _) ,_  (_ . _) _) ,_ . _) _) ,/`\_/`\ (_   (  . _) _) (_ . _) _) ,_  (_ . _) _) ,__ (_   (_ . _) _) (__. _) _)/ ,--.   )  |
    `~~`\ ' . /`~~`           `~~`\ ' . /`~~`   `~~`\ ' . /`~~`     `~~`/--m-m- ~~`\ ' . /`~~`   `\ ' . /`~~`  `\ ' . /  //  _  \\ ``\ '  . /`~~`\ ' . /`~~`   `\ ' . /`~~`     `~~`\ ' . /`~~`\ ' . /`~~/_/    >     |
         ;   ;                     ;   ;             ;   ;               ;   ;      ;   ;          ;   ;         ;   ;  | \     )|_   ;    ;      ;   ;          ;   ;               ;   ;      ;   ;    |,\__-'      |
         /   \                     /   \             /   \               /   \      /   \          /   \         /   \ /`\_`>  <_/ \  /    \      /   \          /   \               /   \      /   \     \__         \
________/_ __ \___________________/_ __ \___________/_ __ \______ __ ___/_ __ \____/_ __ \________/_ __ \_______/_ __ \\__/'---'\__/_/_  __ \____/_ __ \________/_ __ \_____ _______/_ __ \____/_ __ \____ __\___      )
```

