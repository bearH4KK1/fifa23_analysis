import pandas as pd
import re
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv('stats.csv', encoding='utf-8')

# Функция для извлечения численного значения роста из строки
def extract_height(height):
    pattern = r'(\d+)cm'
    matches = re.findall(pattern, height)

    if matches:
        return int(matches[0])
    else:
        return None


# Применяем функцию extract_height к столбцу "Height"
data['Height'] = data['Height'].apply(extract_height)

# Статистический анализ среднего роста
average_height = data['Height'].mean()
average_height_men = 175

# Разница в росте
height_diff = average_height - average_height_men

# Визуализация данных
heights = [average_height, average_height_men]
labels = ['Футболисты', 'Обычные мужчины']

plt.figure(figsize=(8, 6))
plt.bar(labels, heights, color=['blue', 'green'])
plt.xlabel('Категория')
plt.ylabel('Средний рост (в см)')
plt.title('Сравнение средних ростов')

# Добавление разницы в росте на график
plt.text(0, average_height + 1, '+{:.1f} см'.format(height_diff), ha='center', color='black')

# Расчет среднего роста вратарей
goalkeepers = data[data['Main_Position'] == 'GK']
average_height_goalkeepers = goalkeepers['Height'].mean()

# Разница в росте вратарей
height_diff_goalkeepers = average_height_goalkeepers - average_height_men

# Визуализация данных по росту вратарей
plt.figure(figsize=(8, 6))
plt.bar(['Вратари', 'Обычные мужчины'], [average_height_goalkeepers, average_height_men], color=['red', 'green'])
plt.xlabel('Категория')
plt.ylabel('Средний рост (в см)')
plt.title('Сравнение среднего роста вратарей и обычных мужчин')
plt.ylim(0, 200)

# Добавление разницы в росте вратарей на график
plt.text(0, average_height_goalkeepers + 1, '+{:.1f} см'.format(height_diff_goalkeepers), ha='center', color='black')

plt.show()

# Фильтрация данных
top_50_players = data.nlargest(50, 'Rating') #Первые 50 футболистов по рейтингу Fifa23
top_50_players_without_ICONS = data[(data['Club'] != 'FUT ICONS') & (data['Club'] != 'HERO')].nlargest(50, 'Rating') #Первые 50

# Вывод ТОП-50 рейтинга футболистов
print("ТОП-50 рейтинга футболистов:")
for i, player in enumerate(top_50_players.itertuples(), start=1):
    print(f"{i}. {player.Name}")

# Вывод ТОП-50 рейтинга футболистов без учета легенд и героев
print("\nТОП-50 рейтинга футболистов без учета легенд и героев:")
for i, player in enumerate(top_50_players_without_ICONS.itertuples(), start=1):
    print(f"{i}. {player.Name}")

print()

european_countries = ['England', 'Spain', 'Germany', 'Italy', 'France', 'Portugal', 'Poland', 'Netherlands', 'Belgium',
                      'Sweden', 'Austria', 'Greece', 'Denmark']  # Здесь перечислите страны ЕС
european_players = data[(data['Rating'] >= 85) & (data['Nation'].isin(european_countries))]
print("Процент игроков с европейским гражданством в рейтинге 85+: {:.2f}%".format(
    len(european_players) / len(data[data['Rating'] >= 85]) * 100))