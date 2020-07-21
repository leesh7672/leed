#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hms import hcl
from shell import shell
hclf = open('hcl-entries.tex', 'w', encoding='utf-8')
hclf.write(hcl.build())
hclf.close()
shell('xelatex hcl')
shell('pdf270 hcl.pdf')
