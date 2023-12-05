import pandas as pd
import matplotlib.pyplot as plt



# Задание 1

# Шаг 1: Загрузка данных
file_path = 'data2.csv'
data = pd.read_csv(file_path)
print()
print(data.head())

# 2.2. Простой анализ данных
numeric_summary = data.describe()
print("\n")
print(numeric_summary)

# Шаг 3: Визуализация данных
# 3.1. Гистограмма распределения данных
data['numeric_column'].hist(bins=20)
plt.title('1')
plt.xlabel('2')
plt.ylabel('3')
plt.show()

# 3.2. График зависимости между двумя столбцами
plt.scatter(data['column1'], data['column2'])
plt.title('График зависимости между column1 и column2')
plt.xlabel('column1')
plt.ylabel('column2')
plt.show()

# Шаг 4: Отчет
# 4.1. Теперь я знаю как подключать библиотеки в питоне, устанавливать pandas и matplotlib, читать csv файл, извлекать из него значение


