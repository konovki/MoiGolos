import pandas as pd

df = pd.read_csv('opros1.csv')

for column in df.columns:
    if column.startswith('A'):  # Проверяем, что столбец начинается с 'A'
        print(f"\nВероятности для столбца {column}:")
        
        # Получаем количество каждого уникального значения в столбце
        value_counts = df[column].value_counts()
        
        # Вычисляем вероятности (доли)
        probabilities = value_counts / len(df[column])
        
        # Сортируем по значениям для удобства чтения
        probabilities = probabilities.sort_index()
        
        # Выводим результаты
        for value, prob in probabilities.items():
            print(f"  Цифра {value}: {prob:.2%} ({value_counts[value]}/{len(df[column])})")