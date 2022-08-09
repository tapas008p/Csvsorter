# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:40:03 2022

@author: tapas
"""

import csv
import operator


class CsvSorter:
    length=0
    
    def __init__(self):
        self.data=[]
        self.file=[]
        self.file1=[]
        self.data1=[]
        self.header=[]
        
    def csvSorter(self,filename):
        self.file=open(filename)
        self.data = csv.reader(self.file,delimiter=',')
        self.header = next(self.data)
        self.length=len(self.header)
        print("Below is a table of index and columnname and the column data type")
        print('_________________________________________________________________')
        for i in range(len(self.header)):
            print("Index -- > {}       column_name-->{}    type-->{}".format(i,self.header[i],type(self.header[i])))
        new=[]
        for i in self.data:
            new.append(i)

        try:
            a=list(map(int,input("Which index data you want to convert to integer (separated by comma)::").split(',')))
            for i in range(len(new)):
                for j in a:
                    new[i][j]=int(new[i][j])

        except ValueError:
            pass
        
        try:            
            b=list(map(int,input("Which index data you want to convert to float (separated by comma)::").split(',')))
            for i in range(len(new)):
                for j in b:
                    new[i][j]=float(new[i][j])
        except ValueError:
            pass
            
        print('_____________________________________________________________________')
        print("After converting the data types of the columns")
        print('_____________________________________________________________________')
        for i in range(len(new[0])):
            print("Index -- > {}       column_name-->{}          type-->{}".format(i,self.header[i],type(new[0][i])))
        self.file.close()
        print('\n')
        print('________________________________________________________________________')
        print('SORTING BASED ON THE INDEX NUMBER ')
        
        index=int(input("Enter the index :: "))
        rev=int(input("Select an option \n 1.ascending order \n 2.descending order \n"))
        self.file.close()
        if rev==1:
             s= sorted(new,key=operator.itemgetter(index),reverse=False)
             self.file.close()
        elif rev==2:
             s= sorted(new,key=operator.itemgetter(index),reverse=True)
             self.file.close()
        print('\n')
        print('_____________________________________________________________')    
        self.file1 = open(filename,'w',newline='')
        self.data1 = csv.writer(self.file1)
             
        self.data1.writerow(self.header)
        self.data1.writerows(s)
        self.file1.close()
        return s
       