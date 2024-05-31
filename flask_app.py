import re

# ignore the warnings
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from flask import Flask, render_template, request
from pathlib import Path
from typing import FrozenSet

THIS_FOLDER = Path(__file__).parent.resolve()
# STATIC_FOLDER = f"/{THIS_FOLDER}/static"  # use this if the line below doesn't work
STATIC_FOLDER = f"{THIS_FOLDER}/static" # use this if the line above doesn't work
app = Flask(__name__, static_url_path=STATIC_FOLDER)
methods=["GET", "POST"]

regex1_pda = f"{STATIC_FOLDER}/regex1_pda.png"
regex2_pda = f"{STATIC_FOLDER}/regex2_pda.png"

@app.route("/", methods=methods)
@app.route("/home", methods=methods)
@app.route("/index", methods=methods)
@app.route("/dfa", methods=methods)
def dfa():
    """Home page."""

    alphabet = "a, b"
    regex = "(bab|bbb)a*b*(a*|b*)(ba)*(aba)(bab|aba)*bb(a|b)*(bab|aba)(a|b)*"

    nfa = NFA.from_regex(regex,
                        input_symbols=frozenset(list(dict
                        .fromkeys(re.sub("[\s'\]\[]", "", alphabet)
                        .split(",")))))
    dfa = DFA.from_nfa(nfa)
    path = f"{STATIC_FOLDER}/dfa.png"
    dfa.show_diagram(path=path)

    return render_template("dfa.html",
                            alphabet=alphabet,
                            regex=regex,
                            path=path,
                            regex1_pda=regex1_pda,
                            regex2_pda=regex2_pda)


@app.route("/generate_dfa", methods=methods)
def generate_dfa():
    """Generate DFA based on a given alphabet and regular expression."""

    try:
        # retrieve form contents
        output = request.form.to_dict()
        # get whatever is in the name="alphabet" in the forms
        alphabet = output["alphabet"]
        # remove all whitespace and duplicates, and convert into a list
        alphabet_modified = list(dict
                                .fromkeys(re.sub("[\s'\]\[]", "", alphabet)
                                .split(",")))
        # do the same but do not convert it into a list
        # for showing the alphabet on the html page
        alphabet = re.sub("[\s'\]\[]",
                        "",
                        str(alphabet_modified)).strip(",").replace(",", ", ")
        # remove epsilons and lambdas, and replace "+" with "|" in given regex
        regex = re.sub("[\sελΛ\]\[]",
                        "",
                        output["regex"].replace("+", "|")
                        .strip())

        # handle empty string cases
        if regex in {""}:
            regex = "()"

        # generate the PDA and save it in an image file
        nfa = NFA.from_regex(regex, input_symbols=frozenset(alphabet_modified))
        dfa = DFA.from_nfa(nfa)
        path = f"{STATIC_FOLDER}/dfa.png"
        dfa.show_diagram(path=path)

        return render_template("dfa.html",
                                alphabet=alphabet,
                                regex=regex,
                                path=path,
                                regex1_pda=regex1_pda,
                                regex2_pda=regex2_pda)
    except Exception as e:
        return render_template("dfa.html",
                                exception=e,
                                regex1_pda=regex1_pda,
                                regex2_pda=regex2_pda)


@app.route("/track_regex_dfa", methods=methods)
def track_regex_dfa():
    """Simulate a string in the generated DFA."""

    try:
        output = request.form.to_dict()

        dfa_string = output["dfa_string"]
        alphabet = output["alphabet"]
        alphabet_modified = list(dict
                            .fromkeys(re.sub("[\s'\]\[]", "", alphabet)
                            .split(",")))
        alphabet = re.sub("[\s'\]\[]", "",
                            str(alphabet_modified)).strip(",").replace(",", ", ")
        regex = re.sub("[\sελΛ\]\[]", "",
                        output["regex"].replace("+", "|").strip())

        if regex in {""}:
            regex = "()"

        nfa = NFA.from_regex(regex, input_symbols=frozenset(alphabet_modified))
        dfa = DFA.from_nfa(nfa)
        path = f"{STATIC_FOLDER}/dfa.png"
        dfa.show_diagram(input_str=dfa_string, path=path)

        accept = dfa.accepts_input(dfa_string)

        return render_template("dfa.html",
                                alphabet=alphabet,
                                regex=regex,
                                path=path,
                                dfa_string=dfa_string,
                                accept=accept,
                                regex1_pda=regex1_pda,
                                regex2_pda=regex2_pda)
    except Exception as e:
        return render_template("dfa.html",
                                exception=e,
                                regex1_pda=regex1_pda,
                                regex2_pda=regex2_pda)


if __name__ == "__main__":
    app.run()
