#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import pandas as pd
import sys

def testcase(xlsx, sheet, csv):

    xlsx_file = str(xlsx)
    sheetname = str(sheet)
    
    data = pd.read_excel(xlsx_file, sheetname=sheetname)
    
    test_case = pd.concat([data['Unnamed: 7'], data['Unnamed: 8'], data['Unnamed: 9'], data['Unnamed: 10'], data['Unnamed: 11']], axis=1)
    
    test_case.to_csv(str(csv))

