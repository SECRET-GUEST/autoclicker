[![Download autoclicker](https://img.shields.io/sourceforge/dt/hardworkingbruh.svg)](https://sourceforge.net/projects/hardworkingbruh/files/latest/download) Autoclicker version BETA | Python version 3.11.2 | For OS running autoclickers so better on Windows 
```
██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗     ██████╗ ██████╗ ██╗   ██╗██╗  ██╗
██║  ██║██╔══██╗██╔══██╗██╔══██╗██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗██║   ██║██║  ██║
███████║███████║██████╔╝██║  ██║██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗    ██████╔╝██████╔╝██║   ██║███████║
██╔══██║██╔══██║██╔══██╗██║  ██║██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║    ██╔══██╗██╔══██╗██║   ██║██╔══██║
██║  ██║██║  ██║██║  ██║██████╔╝╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝    ██████╔╝██║  ██║╚██████╔╝██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                                                                                                                              

```
![Python](https://img.shields.io/badge/Python-3.x-blue)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

#  New version coming soon

You can already run a stable version directly from the scripts.

## news :
- Tables to set the autoclicker manually
- Upload commands for table in a text file that you can manually rewrite easyly with a text editor for example
- Overlay that you can also find alone in here : https://github.com/SECRET-GUEST/Layer-one


I fixed common issues,  the recorder is now stable on my equipements, but the new table system is way more powerful than it, you can save and load the script you used, they are adding each one to each others then read the command one by one.

I would like to put random delay time that could be set, also make a handler for issues, and add possibility to customize easily themes and more ideas, I will relase the whole app soon so stay tuned even if I know nobody will read this ^^


## :scroll: License

This repository is released under the [MIT License](LICENSE). Please see the `LICENSE` file for more information.

## :question: Support & Questions

If you have any questions or need support, please feel free to open an issue or join my twitter.

riginal script for python 3.11.

In case you have a lower version, you may have to download module imported not included with your version. Just read the first lines of the script in Alexandria with a notepad or whatever to find what's missing.

If you would like to run with python **YOU WILL NEED THE IMAGE .png PLACED IN THE SAME DIRECTORY OF THE RUNNING SCRIPT**.

Also, you can add a `w` to the extension (like `script.pyw`). It means `windowed mode`, to launch the python script without the CMD, but it's still a common python file.

## :large_orange_diamond: 3. Compile the script by yourself

### :gear: Instructions :gear: 

To create your own executable from the python file, you will need to install pyinstaller and python.

Here are the steps you should follow:

   :small_red_triangle: Download python 3.11.1 

Don't forget to add it to your path with the installer or in variables environment (so reboot your PC after the installation), here is the link: 

:crossed_flags: https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe :crossed_flags:

:small_red_triangle: Open your CMD as an administrator and type the following command:

```
python -m pip install pyinstaller
```

:small_red_triangle: You can now run it using a ruby `.spec` file by entering the following command in the project directory:

```bash
pyinstaller YOUR_FILE.spec
```
Normally, I place a blank.spec file in the "script" folder, if there isn't one let's watch over here:

:crossed_flags: https://github.com/SECRET-GUEST/tiny-scripts/tree/ALL/useful%20for%20python/pyinstaller :crossed_flags:

:small_red_triangle: You can also run it directly with your OS, type the following command, replacing the file paths with your own:

```
pyinstaller --onefile --icon="...YOUR PATH.../YOUR ICON.ico" --add-data "...YOUR PATH.../ico;ico" --noconsole test.py
```
#### Here are the explanations of the different options:



- `--onefile`: creates a single executable that includes all dependencies.

- `--icon=icon.ico`: specifies the icon to use for the executable (replace icon.ico with the path to your icon file).

- `--add-data "path/to/file;folder_name"`: adds external files required by the program. The path to the file and the name of the folder in which the file will be extracted should be separated by a semicolon `;`. You can add multiple files by separating them with semicolons.

- `script.py`: specifies the name of your Python script.

- `--noconsole`: hides the console when the executable is run.



Make sure to replace the snipped parts with the names of your files and folders. Also note that the path should be specified based on the operating system you are working on.

After running this command, you should have a single executable that includes all dependencies, external files, and a custom icon, and does not show the console when running.

Alternatively, you can also :

## :large_orange_diamond: 4. Create a batch file to run

- [ ] Create a text file

- [ ] In the text file type and write (and change/complete the path, first is for python, 2nd is for script.py):

```
C:\YOUR PATH TO PYTHON\python.exe" "C:\**YOUR PATH TO THE SCRIPT**\script.pyw"
```


If Python is in the path, you can just:

```
python "C:\**YOUR PATH TO THE SCRIPT**\script.pyw"
```

- [ ] Rename the `new_file.txt` to `script.bat` then just click on it, and it will run the program


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
