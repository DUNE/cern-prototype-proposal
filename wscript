#!/usr/bin/env python

import os

top='.'

def configure(cfg):
    cfg.load('tex')
    pass


def build(bld):

    bld(features='tex',
        type='pdflatex',
        source = 'CERNproto.tex',
        outs = 'pdf',
    )
    bld.install_files('${PREFIX}','CERNproto.pdf')
    return


