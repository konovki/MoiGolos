import pandas as pd
import numpy as np
import math as m

class Generator:
    def __init__(self):
        self.NumberOfPeople = 6234
        columns = [f'A{i+1}' for i in range(39)]
        self.df = df = pd.DataFrame(np.nan, index=range(self.NumberOfPeople) , columns=columns)
        print(self.df)
        self.X = 2
        self.A1 = [57, 32, 10, 1]
        self.A2 = [71, 21,5,3]
        self.A3 = [52, 40, 7, 1]
        self.A4 = [1,3,3,5,6,6,9,34,25,8]
        self.A5 = [9,11,8,12,40,8,1,11]
        self.A6 = [5, 6, 18, 3, 3, 5, 49,11]
        self.A7 = [9, 20, 36, 35]
        self.A8 = [63, 26, 11]
        self.A9 = [51, 42, 7]
        self.A10 = [35, 51, 10, 4]
        self.A11 = [52, 48]
        self.A12 = [23, 58, 11, 8]
        self.A13 = [49, 42, 5, 4]
        self.A14 = [43, 48, 7, 2]
        self.A15 = [45, 38, 14, 3]
        self.A16 = [29, 38, 24, 9]
        self.A17 = [35, 40, 21, 4]
        self.A18 = [36, 40, 19, 5]
        self.A19 = [35, 42, 19, 4]
        self.A20 = [31, 42, 23, 4]
        self.A21 = [32, 43, 19, 6]
        self.A22 = [35, 42, 16, 7]
        self.A23 = [42, 48, 7, 3]
        self.A24 = [30, 48, 17, 5]
        self.A25 = [15, 21, 28, 36]
        self.A26 = [31, 47, 17, 5]
        self.A27 = [6, 4, 6, 11,73]
        self.A28 = [52, 34, 8, 6]
        self.A29 = [55, 40, 3, 2]
        self.A30 = [63, 22, 13, 2]
        self.A31 = [66, 30, 3, 1]
        self.A32 = [28,45, 24, 3]
        self.A33 = [31, 37, 22, 10]
        self.A34 = [28, 46, 20, 6]
        self.A35 = [3, 6, 8, 6, 11, 21, 34, 11]
        self.A36 = [1, 16, 9, 12, 22, 20, 15,5]
        self.A37 = [62, 38]
        self.A38 = [15, 29, 56]
        self.A39 = [20, 40, 40]
        #1
        self.df = self.setColumn(self.A1,self.NumberOfPeople,self.df,'A1')
        self.checkStats(self.df,'A1')
        #2
        self.df = self.setColumn(self.A2,self.NumberOfPeople,self.df,'A2')
        self.checkStats(self.df,'A2')
        

        #36
        self.df = self.setColumn(self.A36,self.NumberOfPeople,self.df,'A36')
        self.checkStats(self.df,'A36')
        #3
        filtered_df = self.df[self.df['A36'].isin([1,2,3])]
        print('Yang\n',filtered_df)
        #39
        self.df = self.setColumn(self.A39,self.NumberOfPeople,self.df,'A39')
        self.checkStats(self.df,'A39')

        print(self.df)
        # Получение количества уникальных значений
        
    @staticmethod
    def checkStats(df,col):
        counts = df[col].value_counts()
        # Получение процентного соотношения
        percentages = df[col].value_counts(normalize=True) * 100
        # Объединение в один DataFrame
        result = pd.DataFrame({'Count': counts, 'Percentage': percentages})
        print(result['Count'].sum(),result['Percentage'].sum())
        print(result)
    @staticmethod
    def setColumn(Stats,Num,df,col):#self.A39,self.NumberOfPeople,self.df,'A39'
        s_ind,ind = 0,0  # инициализация начального индекса
        for i, proc in enumerate(Stats):
            ind = s_ind + m.floor(proc/100 * Num)  # округление вниз текущего значения
            # Правильное присваивание значения в DataFrame
            df.loc[s_ind:ind, col] = int(i + 1)
            s_ind = ind + 1  # обновление начального индекса для следующей итерации
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
        return df.sample(frac=1).reset_index(drop=True)
    @staticmethod
    def setColumnNoMix(Stats,Num,df,col):#self.A39,self.NumberOfPeople,self.df,'A39'
        s_ind,ind = 0,0  # инициализация начального индекса
        for i, proc in enumerate(Stats):
            ind = s_ind + m.floor(proc/100 * Num)  # округление вниз текущего значения
            # Правильное присваивание значения в DataFrame
            df.loc[s_ind:ind, col] = int(i + 1)
            s_ind = ind + 1  # обновление начального индекса для следующей итерации
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
        return df
gen = Generator()