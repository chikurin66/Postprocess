#
#
# usage : 
# $ sh bleu.sh | python bleu_filter.py




import sys
from collections import Counter

word_count = Counter()


for line in sys.stdin:
    line = line.strip("\n")
    words = line.split(' ')
    words = [w for w in words if w != '']
    sys.stdout.write(words[words.index("=") + 1].rstrip(',') + "\n")

