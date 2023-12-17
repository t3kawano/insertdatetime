# insertdatetime
**231217**

This script is tested only on Mac so far. probably it works on windows.
This Python 3.11 script, launched through Spyder, helps you easily add creation and modification times as YAML front matter to markdown files within a chosen folder.
To use it, Exported evernote data using offical method, and import it by importer plugin of obsidian core-plugins.
Resultant files should have created time and midifed time stamps as you can see on finder. Then, run this script and choose a folder.

While it functions within the selected directory, it currently lacks the ability to process subfolders recursively. 
To address files in nested folders, simply run the script on each relevant directory. 
Please note that the script currently insert new YAML front matter without concidering whether already a YAML front matter exit or not in markdown files. 
To handle existing configurations gracefully, consider implementing merging or substitution functionalities for future versions or use other methods.
