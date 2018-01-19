#
#
#
# usage:
# cat result_train_data | python extLoss.py | tee result_file  


import sys
from collections import Counter

word_count = Counter()


print("Epoch \tDev_LL   \tDev_PPL   \tBLEU   \tTrain_LL   \tTrain_PPL")
for line in sys.stdin:
    line = line.strip("\n")
    if "Dev.Data" in line:
        words = line.split(' ')
        words = [w for w in words if w != '']
        sys.stdout.write(words[words.index("Epoch:") + 1] + "\t")
        sys.stdout.write(words[words.index("LL:") + 1] + '\t' + words[words.index("PPL:") + 1] + '    \t')
    if "BLEU" in line:
        words = line.split(' ')
        words = [w for w in words if w != '']
        sys.stdout.write(words[words.index("BLEU") + 2].strip(',') + "\t")
    if "Train END" in line:
        words = line.split(' ')
        words = [w for w in words if w != '']
        sys.stdout.write(words[words.index("LL:") + 1] + "\t" + words[words.index("PPL:") + 1] + '\n')


