# CodeHUB Text Editor

## Summary

CodeHUB is a lightweight text editor developed using Python and the Tkinter library. The primary goal of this project was to create a functional and efficient text editor that can run smoothly on less powerful PCs, addressing the challenges faced when using heavy Integrated Development Environments (IDEs) or text editor software. The project incorporates various technologies, including JSON for data storage and the Pygments library for syntax highlighting. 

## Features

- **Syntax Highlighting:** Utilizes the Pygments library to provide syntax highlighting for various programming languages.
- **File Operations:** Supports opening, editing, and saving text files.
- **Customizable Interface:** Users can adjust themes and fonts according to their preferences.
- **Keyboard Shortcuts:** Various shortcuts for common text editing operations to enhance productivity.

## Requirements

1. **Python 3.4 or Higher**
2. **Windows 7 or Higher**
3. **Required Libraries:**
   - pygments
   - csv (pre-installed)
   - json (pre-installed)
   - tkinter (pre-installed)

## Installation

### Checking Installed Libraries

To check if the required libraries are installed, open IDLE and type `import library_name`. Replace `library_name` with the names of the libraries listed above (e.g., `pygments`, `csv`, `json`, `tkinter`). If an error occurs, it means the library is not installed.

### Installing Missing Libraries

If any libraries are missing, you can install them using the following commands in the command prompt:

```sh
pip install pygments
```

Libraries like `csv`, `json`, and `tkinter` come pre-installed with Python. If they are not available, consider reinstalling Python.


## Project Structure

- `codehub.py`: Main entry point for the application.
- `highlighter.py`: Handles syntax highlighting using Pygments.
- `settings.py`: Manages user settings and themes.
- `menu.py`: Implements the menu and its functionalities.
- `statusbar.py`: Displays the status bar with line and column information.
- `textarea.py`: Main text area for editing text.

## ScreenShots
![ide1](https://github.com/user-attachments/assets/70d48a78-955d-4bb3-8d3d-cc664a6e3816)
![ide2](https://github.com/user-attachments/assets/f30c5aff-6f11-49b9-bace-c382955a85ff)
![ide3](https://github.com/user-attachments/assets/afb531c9-aa23-4900-a8f1-07c38646d979)
![ide4](https://github.com/user-attachments/assets/72f231fb-ed51-4d2d-a03b-bd188649b3e7)
