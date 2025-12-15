import re
import sys

# Usage:
#   python annotate.py <text_file> <vocab_file> <output_file>
# Example:
#   python annotate.py original_text.txt vocab_list.txt output.txt

if len(sys.argv) != 4:
    print("Usage: python annotate.py <text_file> <vocab_file> <output_file>")
    sys.exit(1)

TEXT_FILE = sys.argv[1]
VOCAB_FILE = sys.argv[2]
OUTPUT_FILE = sys.argv[3]


# ---------- load vocabulary ----------
vocab = {}

with open(VOCAB_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or ":" not in line:
            continue
        # Expected format:
        # original word: base form: phonics: meaning
        parts = [p.strip() for p in line.split(":", 3)]
        if len(parts) != 4:
            continue
        original, base, phonics, meaning = parts
        vocab[original] = f" _({base} {phonics}: {meaning})_"


# ---------- process text ----------
def replace_marked_words(line):
    def repl(match):
        word = match.group(1)
        explanation = vocab.get(word)
        if explanation:
            return f"{word}{explanation}"
        else:
            # If vocab entry is missing, just remove ** **
            return word

    return re.sub(r"\*\*(.*?)\*\*", repl, line)


# ---------- read / write ----------
with open(TEXT_FILE, "r", encoding="utf-8") as fin, \
     open(OUTPUT_FILE, "w", encoding="utf-8") as fout:
    for line in fin:
        fout.write(replace_marked_words(line))


print("Done.")
print("Input text :", TEXT_FILE)
print("Vocab file :", VOCAB_FILE)
print("Output     :", OUTPUT_FILE)
