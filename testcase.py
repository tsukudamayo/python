#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import sys
import pandas as pd

def sim_testcase(xlsx, sheet, csv):

    xlsx_file = str(xlsx)
    sheetname = str(sheet)
    
    data = pd.read_excel(xlsx_file, sheetname=sheetname)
    
    test_case = pd.concat([data['Unnamed: 7'], data['Unnamed: 8'], data['Unnamed: 9'], data['Unnamed: 10'], data['Unnamed: 11']], axis=1)
    
    test_case.to_csv(str(csv))


def sav_testcase(xlsx, sheet, csv):

    xlsx_file = str(xlsx)
    sheetname = str(sheet)
    
    data = pd.read_excel(xlsx_file, sheetname=sheetname)
    
    test_case = data.iloc[:,1:17]
    print(test_case)
    
    test_case.to_csv(str(csv))

