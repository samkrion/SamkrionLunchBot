#! /bin/bash

WORKDIR=`mktemp -d`
if [ -z $SRCDIR ]; then
    SRCDIR="/mount/code"
fi
if [ -z $OUTDIR ]; then
    OUTDIR="/mount"
fi

rm -rf $OUTDIR/function.zip
cd $WORKDIR
cp -r $SRCDIR/* .
pip install -r requirements.txt --target .
zip -r9 $OUTDIR/function.zip .
