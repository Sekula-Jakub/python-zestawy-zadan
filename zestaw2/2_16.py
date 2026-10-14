# W tekście znajdującym się w stringu line zamienić
# ciąg znaków "GvR" na "Guido van Rossum".

def zamien_gvr(line):
    line = line.replace("GvR", "Guido van Rossum")
    return line

line1 = "Nie taki diabeł GvR straszny\njak go malują."
line2 = "Jak się człowiek spieszy\nto się diabeł GvR cieszy."

assert zamien_gvr(line1) == "Nie taki diabeł Guido van Rossum straszny\njak go malują."
assert zamien_gvr(line2) == "Jak się człowiek spieszy\nto się diabeł Guido van Rossum cieszy."