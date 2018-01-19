# -*- coding: utf-8 -*-

import nltk.translate.bleu_score as bl
import sys


hyp_filename = sys.argv[1]
ref_filename = sys.argv[2]

fi1 = open(hyp_filename, 'r')
fi2 = open(ref_filename, 'r')

hyp_lines = fi1.readlines()
ref_lines = fi2.readlines()

fi1.close()
fi2.close()

hyp = list()
ref = list()
for hyp_line, ref_line in zip(hyp_lines, ref_lines):
    if len(hyp_line.split(' ')) >= 4 and len(ref_line.split(' ')) >= 4:
        hyp.append(hyp_line.split(' '))
        ref.append(ref_line.split(' '))
    # print(hyp_lines[i])
    # print(ref_lines[i])
    # bleu_score = bl.sentence_bleu(ref_lines[i], hyp_lines[i], weights=(0.25, 0.25, 0.25, 0.25))
    # print(bleu_score)

bleu_score = bl.corpus_bleu(ref, hyp, weights=(0.25, 0.25, 0.25, 0.25))
# bleu_score = bl.corpus_bleu([["a", "b", "c", "d", "e"], ["d", "e", "f", "g", "h"]], [["s", "t", "y", "u", "i"], ["sd", "gg", "hh", "sb", "cs"]], weights=(0.25, 0.25, 0.25, 0.25))

print(bleu_score)


