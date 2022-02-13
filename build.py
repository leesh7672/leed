#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hms import hcl

if __name__ == '__main__':
    hclf = open('leed-entries.tex', 'w', encoding='utf-8')
    hclf.write(hcl.build())
    hclf.close()
