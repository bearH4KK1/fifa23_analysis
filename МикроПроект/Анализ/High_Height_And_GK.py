import pandas as pd
import matplotlib.pyplot as plt
import re

# Загрузка данных
data = pd.read_csv('stats.csv')

# Фильтрация данных только для позиции вратаря (GK)
goalkeepers = data[data['Main_Position'] == 'GK'].copy()

# Извлечение численного значения роста

def extract_height(height):
    pattern = r'(\d+)cm'
    matches = re.findall(pattern, height)

    if matches:
        return int(matches[0])
    else:
        return None

# Применяем функцию extract_height к столбцу "Height" вратарей
goalkeepers.loc[:, 'Height'] = goalkeepers['Height'].apply(extract_height)

# Очистка данных от нулевых и отсутствующих значений
goalkeepers = goalkeepers.dropna(subset=['Height'])

# Параметры для анализа
threshold_height = 185  # Пороговая высота для определения "достаточно высокого" вратаря

# Расчет доли вратарей с высотой выше пороговой
tall_goalkeepers = goalkeepers[goalkeepers['Height'] > threshold_height]
percentage_tall_goalkeepers = (len(tall_goalkeepers) / len(goalkeepers)) * 100

# Вывод результатов
print("Доля вратарей с высотой выше", threshold_height, "см:", percentage_tall_goalkeepers, "%")

# Визуализация данных
plt.hist(goalkeepers['Height'], bins=20, color='blue', edgecolor='black')
plt.axvline(x=threshold_height, color='red', linestyle='--', label='Пороговая высота')
plt.xlabel('Рост (см)')
plt.ylabel('Количество вратарей')
plt.title('Распределение роста вратарей')
plt.legend()
plt.show()