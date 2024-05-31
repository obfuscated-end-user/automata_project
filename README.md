# Automata
Simulates [deterministic finite automata](https://en.wikipedia.org/wiki/Deterministic_finite_automaton) (DFA) and [pushdown automata](https://en.wikipedia.org/wiki/Pushdown_automaton) (PDA).  
Runs on Python 3.11.5, 64-bit.

# Installation
* Open the terminal in this directory.
* Type the following commands (I assume you're on Windows):
    ```bat
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
* I can't guarantee that this will work, especially with the `pygraphviz` module.

# How to run the web application
If the installation worked without problems, you may do the following:
* Open the terminal in this directory.
* Type the following commands:
    ```bat
    venv\Scripts\activate
    python flask_app.py
    ```
* It will show you a URL that you can click (something like "`http://127.0.0.1:5000`"). Go there to see the application.
* To close the application, go back to the terminal, and press CTRL+C. This will stop the local server from running.
* Opening any of the HTML files directly in your browser will not work. It may display the usual HTML stuff (text, buttons, textboxes, etc.), but you won't be able to interact with anything as your browser does not know how to read and interpret Python code.

If none of the methods above worked for you, you can go [here](https://automata2024.pythonanywhere.com).  

You can ignore the `misc` folder.