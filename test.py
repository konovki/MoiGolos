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
def setColumnIndex(Stats,df,col):
    index = df.index
    Num = len(df)
    df = df.reset_index(drop =True)
    s_ind,ind = 0,0  # инициализация начального индекса
    for i, proc in enumerate(Stats):
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