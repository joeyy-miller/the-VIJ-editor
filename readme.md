## VIJ: Open VI
A free lazy loading open source VI command line text editor clone built by Joey Miller for UNIX systems; as a project. Free to download, edit, and change.

# How to:
Fork this repository to edit, change, or add commands that you want to add to the edtior. Use this as a base to create your own VI inspired editor.

Find a file you want to edit, use `python3 vij.py file.txt`. Replace `python3` with your Python complier. Change `file.txt` to the name of the file that you want to edit. 

# Commands:
+ `a`: Append a new line at the end of the document.
+ `i`, `i#`: Insert a new line BEFORE the number you specify. The number field is optional.
+ `d`, `d#`: Delete the line that you specify.
+ `r`, `r#`: Replace a line that you specify.
+ `s`, `sq`: Save the file. s+q is save and quit the editor.
+ `h`: Help, tell about the ediotr.
+ `q`: Quit the editor

# Versions
`v03252023c`
+ Added a new save command `s`, to save without quiting. 
+ Added a double command `sq` to save then quit, replacing the old `s` command.
+ Added an about command `h`, to tell about the file and version.
+ Added an Insert# command `i[number to insert]`, to quickly insert a number without having to do it in two commands.
+ Added REGEX module.

`v04012023a`
+ Changed the insert, delete, and replace command to be able to take the line number after to speed up editing.
+ Changed the formatting of the menus. 
