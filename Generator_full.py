import pandas as pd
import numpy as np
import math as m

class Generator:
    def __init__(self):
        self.NumberOfPeople = 1000
        columns = [f'A{i+1}' for i in range(39)]
        self.df = pd.DataFrame(np.nan, index=range(self.NumberOfPeople) , columns=columns)
        self.X = 30
        self.A1 = [57, 32, 10, 1]
        self.A2 = [71, 21,5,3]
        self.A3 = [52, 40, 7, 1] #удовл 51
        self.A4 = [1,3,3,5,6,6,9,34,25,8] #лоялтность 49
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
        categories = {'yang':[0,1],'profi':[2,3,4],'Sprofi':[5,6],'old':[7]}
        satisfaction = {'yang':[49, 32, 16, 3],'profi':[54, 38, 6, 2],'Sprofi':[55, 32, 6, 5],'old':[62, 31, 4, 3]}
        gender = {'yang':[58,42],'profi':[62,38],'Sprofi':[71,29],'old':[75,25]}
        loyality= {'yang':[0,2,2,3,5,5,7,7,30,22,17]
                        ,'profi':[0,2,3,3,5,5,7,9,29,26,11],
                        'Sprofi':[0,1,3,3,3,5,6,9,34,26,10],
                           'old':[0,0,0,0,3,3,4,4,34,31,20]}
        #36
        self.df = self.setColumn(self.A36,self.NumberOfPeople,self.df,'A36')
        self.checkStatsAge(self.df,'A36')
        #1
        self.df = self.setColumn(self.A1,self.NumberOfPeople,self.df,'A1')
        # self.checkStats(self.df,'A1')
        #2
        self.df = self.setColumn(self.A2,self.NumberOfPeople,self.df,'A2')
        # self.checkStats(self.df,'A2')
        #3
        self.df = Generator.answ_by_categories(categories,'A36','A3',satisfaction,self.df)
        self.checkStats(self.df,'A3')
        #4
        self.df = Generator.answ_by_categories(categories,'A36','A4',loyality,self.df)
        self.checkStats(self.df,'A4')
        #5
        self.df = self.setColumn(self.A5,self.NumberOfPeople,self.df,'A5')
        self.checkStats(self.df,'A5')
        #6
        self.df = self.setColumn(self.A6,self.NumberOfPeople,self.df,'A6')
        self.checkStats(self.df,'A6')
        #7
        self.df = self.setColumn(self.A7,self.NumberOfPeople,self.df,'A7')
        self.checkStats(self.df,'A7')
        #8
        self.df = self.setColumn(self.A8,self.NumberOfPeople,self.df,'A8')
        self.checkStats(self.df,'A8')
        #9
        self.df = self.setColumn(self.A9,self.NumberOfPeople,self.df,'A9')
        self.checkStats(self.df,'A9')
        #10
        self.df = self.setColumn(self.A10,self.NumberOfPeople,self.df,'A10')
        self.checkStats(self.df,'A10')
        #11
        self.df = self.setColumn(self.A11,self.NumberOfPeople,self.df,'A11')
        self.checkStats(self.df,'A11')
        #12
        self.df = self.setColumn(self.A12,self.NumberOfPeople,self.df,'A12')
        self.checkStats(self.df,'A12')
        #13
        self.df = self.setColumn(self.A13,self.NumberOfPeople,self.df,'A13')
        self.checkStats(self.df,'A13')
        #14
        self.df = self.setColumn(self.A14,self.NumberOfPeople,self.df,'A14')
        self.checkStats(self.df,'A14')
        #15
        self.df = self.setColumn(self.A15,self.NumberOfPeople,self.df,'A15')
        self.checkStats(self.df,'A15')
        #16
        self.df = self.setColumn(self.A16,self.NumberOfPeople,self.df,'A16')
        self.checkStats(self.df,'A16')
        #17
        self.df = self.setColumn(self.A17,self.NumberOfPeople,self.df,'A17')
        self.checkStats(self.df,'A17')
        #18
        self.df = self.setColumn(self.A18,self.NumberOfPeople,self.df,'A18')
        self.checkStats(self.df,'A18')
        #19
        self.df = self.setColumn(self.A19,self.NumberOfPeople,self.df,'A19')
        self.checkStats(self.df,'A19')
        #20
        self.df = self.setColumn(self.A20,self.NumberOfPeople,self.df,'A20')
        self.checkStats(self.df,'A20')
        #21
        self.df = self.setColumn(self.A21,self.NumberOfPeople,self.df,'A21')
        self.checkStats(self.df,'A21')
        #22
        self.df = self.setColumn(self.A22,self.NumberOfPeople,self.df,'A22')
        self.checkStats(self.df,'A22')
        #23
        self.df = self.setColumn(self.A23,self.NumberOfPeople,self.df,'A23')
        self.checkStats(self.df,'A23')
        #24
        self.df = self.setColumn(self.A24,self.NumberOfPeople,self.df,'A24')
        self.checkStats(self.df,'A24')
        #25
        self.df = self.setColumn(self.A25,self.NumberOfPeople,self.df,'A25')
        self.checkStats(self.df,'A25')
        #26
        self.df = self.setColumn(self.A26,self.NumberOfPeople,self.df,'A26')
        self.checkStats(self.df,'A26')
        #27
        self.df = self.setColumn(self.A27,self.NumberOfPeople,self.df,'A27')
        self.checkStats(self.df,'A27')
        #28
        self.df = self.setColumn(self.A28,self.NumberOfPeople,self.df,'A28')
        self.checkStats(self.df,'A28')
        #29
        self.df = self.setColumn(self.A29,self.NumberOfPeople,self.df,'A29')
        self.checkStats(self.df,'A29')
        #30
        self.df = self.setColumn(self.A30,self.NumberOfPeople,self.df,'A30')
        self.checkStats(self.df,'A30')
        #31
        self.df = self.setColumn(self.A31,self.NumberOfPeople,self.df,'A31')
        self.checkStats(self.df,'A31')
        #32
        self.df = self.setColumn(self.A32,self.NumberOfPeople,self.df,'A32')
        self.checkStats(self.df,'A32')
        #33
        self.df = self.setColumn(self.A33,self.NumberOfPeople,self.df,'A33')
        self.checkStats(self.df,'A33')
        #34
        self.df = self.setColumn(self.A34,self.NumberOfPeople,self.df,'A34')
        self.checkStats(self.df,'A34')
        #35
        self.df = self.setColumn(self.A35,self.NumberOfPeople,self.df,'A35')
        self.checkStats(self.df,'A35')
        #37
        self.df = Generator.answ_by_categories(categories,'A36','A37',gender,self.df)
        self.checkStats(self.df,'A37')
        #38
        self.df = self.setColumn(self.A38,self.NumberOfPeople,self.df,'A38')
        self.checkStats(self.df,'A38')
        
        #39
        self.df = self.setColumn(self.A39,self.NumberOfPeople,self.df,'A39')
        self.checkStats(self.df,'A39')
        
        Generator.check_satisfaction(self.df)
        Generator.check_loyality(self.df)
        # for col in self.df.columns:
        #     self.df[col] = pd.to_numeric(self.df[col], errors='coerce').astype('Int64')
        # print(self.df)
        
        # print(self.df)
        any_nan = self.df.isna().any().any()
        if any_nan:
            df = self.df
            # print('ERROR GOT NANS')
            nan_rows_any = df[df.isna().any(axis=1)]
            self.df['A4'] = self.df['A4'].fillna(int(10))
            self.df['A3'] = self.df['A3'].fillna(int(0))
            self.df['A37'] = self.df['A37'].fillna(int(0))
            # print("Rows with at least one NaN:")
            # print(nan_rows_any)
        # any_nan = self.df.isna().any().any()
        # nan_rows_any = df[df.isna().any(axis=1)]
        # print('again Nans\n',nan_rows_any)
        self.df = self.df.astype(int) 
        # print(self.df)
        self.df.to_csv('opros1.csv')
        # Получение количества уникальных значений
    @staticmethod
    def answ_by_categories(categories,colPoint,colAnsw,answers,df):
        '''
        colPoint - по какой колонке выборка
        colAnsw - в нее записываем значения 
        '''
        for cat in categories.keys():
            tmp0 = df[df[colPoint].isin(categories[cat])]
            index = tmp0.index
            tmp = Generator.setColumnIndex(answers[cat],tmp0,colAnsw)
            df.loc[index,:] = tmp
        df[colAnsw] = pd.to_numeric(df[colAnsw], errors='coerce').astype('Int64')
        return df
    @staticmethod
    def check_satisfaction(df):#лоялтность 43-44 
        categories = {'yang':[0,1],'profi':[2,3,4],'Sprofi':[5,6],'old':[7]}
        counts = categories.keys()
        vals = []
        vPositive = (df[df['A4'].isin([8,9,10])]).shape[0]/df.shape[0]
        vNegative = (df[df['A4'].isin([0,1,2,3,4,5])]).shape[0]/df.shape[0]
        print('Целевое значение 49 \n Full loyality:',vPositive-vNegative)
        for cat in categories.keys():
            tmp = df[df['A36'].isin(categories[cat])]
            vPositive = (tmp[tmp['A4'].isin([8,9,10])]).shape[0]/tmp.shape[0]
            vNegative = (tmp[tmp['A4'].isin([0,1,2,3,4,5])]).shape[0]/tmp.shape[0]
            val = vPositive-vNegative
            vals.append(val)
        result = pd.DataFrame({'Category': counts, 'Percentage': vals})
        print('check loyality\n',result)

        
    @staticmethod
    def check_loyality(df):#удовл 51
        
        categories = {'yang':[0,1],'profi':[2,3,4],'Sprofi':[5,6],'old':[7]}
        counts = categories.keys()
        vals = []
        vPositive = (df[df['A3'].isin([0])]).shape[0]/df.shape[0]
        vNegative = (df[df['A3'].isin([3])]).shape[0]/df.shape[0]
        print('Целевое значение 51 \n Full satisfaction:',vPositive-vNegative)
        for cat in categories.keys():
            tmp = df[df['A36'].isin(categories[cat])]
            vPositive = (tmp[tmp['A3'].isin([0])]).shape[0]/tmp.shape[0]
            vNegative = (tmp[tmp['A3'].isin([3])]).shape[0]/tmp.shape[0]
            val = vPositive-vNegative
            vals.append(val)
        result = pd.DataFrame({'Category': counts, 'Percentage': vals})
        print(result['Percentage'].sum())
        print('check satisfaction\n',result)
        

    @staticmethod
    def checkStats(df,col):
        counts = df[col].value_counts()
        # Получение процентного соотношения
        percentages = df[col].value_counts(normalize=True) * 100
        # Объединение в один DataFrame
        result = pd.DataFrame({'Count': counts, 'Percentage': percentages})
        # print('\n',col,result['Count'].sum(),result['Percentage'].sum())
        print(df.shape)
        # print('Nan\n',df[df[col].isna()])
        print('\n',result)
    @staticmethod
    def checkStatsAge(df,col):
        print('checkStatsAge')
        ages = {'yang':[0,1],'profi':[2,3,4],'Sprofi':[5,6],'old':[7]}
        counts = df[col].value_counts()
        # Получение процентного соотношения
        percentages = df[col].value_counts(normalize=True) * 100
        # Объединение в один DataFrame
        result = pd.DataFrame({'Count': counts, 'Percentage': percentages})
        print(col,result['Count'].sum(),result['Percentage'].sum())
        print(result)
        proc,num = [],[]
        for age in ages.keys():
            val = len(df[df['A36'].isin(ages[age])])
            num.append(val)
            proc.append(val/len(df))
        print(pd.DataFrame(data={'age':ages.keys(),'num':num,'%':proc}))

        # print(df.shape)
        # print('Nan\n',df[df[col].isna()])
        
    @staticmethod
    def setColumnIndex(Stats,df,col):
        index = df.index
        Num = len(df)
        df = df.reset_index(drop =True)
        s_ind,ind = 0,0  # инициализация начального индекса
        for i, proc in enumerate(Stats): #может быть равно 0
            ind = s_ind + m.floor(proc/100 * Num)  # округление вниз текущего значения
            # Правильное присваивание значения в DataFrame
            df.loc[s_ind:ind, col] = int(i)
            s_ind = ind + 1  # обновление начального индекса для следующей итерации
        df.loc[df[col].isna(), col] = 0
        # print('Nan0\n',df[df[col].isna()])
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
        # df = df.sample(frac=1)
        df.index = index
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
        return df

    @staticmethod
    def setColumn(Stats,Num,df,col):#self.A39,self.NumberOfPeople,self.df,'A39'
        s_ind,ind = 0,0  # инициализация начального индекса
        for i, proc in enumerate(Stats):
            ind = s_ind + m.floor(proc/100 * Num)  # округление вниз текущего значения
            # Правильное присваивание значения в DataFrame
            df.loc[s_ind:ind, col] = int(i)
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