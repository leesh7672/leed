#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hms import hcl
freeze_support()
hclf = open('hcl-entries.tex', 'w', encoding='utf-8')
hclf.write(hcl.build())
hclf.close()
