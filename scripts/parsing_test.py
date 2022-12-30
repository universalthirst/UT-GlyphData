# -*- coding: utf-8 -*-

from numbers_parser import Document

my_doc = Document("/Users/UT-development/Documents/UniversalThirst/04_dataAndTools/UT-GlyphData/GlyphsApp/Gujarati/BiConsonantConjuncts_Gujarati_Edited.numbers")
my_sheet = my_doc.sheets
#all_tables = my_sheet[0].tables
#all_rows = tables[0].row()

sheet_1 = my_doc.sheets[0]
print(sheet_1.name)
