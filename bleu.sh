#!/bin/sh

POST_DIR=/home/takebayashi/src/Postprocess
HYP_DIR=/media/takebayashi/064AD3034AD2EE85/LSTMEncDecAttn_model
REF_DATA=/home/takebayashi/src/corpus/IWSLT/test2010.iwslt.tok.en
EP=26

for e in `seq $EP`
do
    echo -n "Epoch "
    echo -n ${e}
    echo -n "\t"
    $POST_DIR/multi-bleu.perl $REF_DATA < $HYP_DIR/iwslt.tok.model.epoch${e}.decode_MAX_BEAM5.txt
done

