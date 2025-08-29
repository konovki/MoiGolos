from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

url = 'https://moigolos.pro/app/KA6'
# df = pd.read_csv('gen3/opros1.csv')
df = pd.read_csv('opros1.csv')
sleepAfterAnswer, sleeptime = False, 1
WaitingTime = 2 * 60


# Открываем веб-страницу
def AnswerRadio(Qwestion, driver, Counter):
    # time.sleep(0.2)
    element = WebDriverWait(driver, WaitingTime).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'ant-radio-input')]"))
    )
    def FindAnsText(Qwestion, Index):
        if Qwestion == 1:
            An = ['успешно развивающееся предприятие', 'предприятие, работающее стабильно (но не развивающееся)',
                  'предприятие, испытывающее определённые трудности',
                  'предприятие, находящееся в кризисе, упадке']
            return An[df['A1'][Index]]
        elif Qwestion == 2:
            An = ['полностью доверяю', 'скорее доверяю', 'скорее не доверяю', 'полностью не доверяю']
            return An[df['A2'][Index]]
        elif Qwestion == 3:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён', 'не удовлетворён']
            return An[df['A3'][Index]]
        elif Qwestion == 5:
            An = [
                'хорошие условия работы (комфортное рабочее место, условия труда, материально-техническое обеспечение, современное оборудование и пр.)',
                'хороший соцпакет, удовлетворительное количество и качество социальных льгот, предоставляемых организацией',
                'достойный уровень заработной платы', 'хорошее руководство',
                'предприятие работает стабильно сейчас и будет стабильно работать в дальнейшем',
                'на других предприятиях условия работы еще хуже', 'таких причин нет']
            return An[df['A5'][Index]]
        elif Qwestion == 6:
            An = [
                'плохие условия работы (некомфортное рабочее место, плохие условия труда и материально-техническое обеспечение, устаревшее оборудование и пр.)',
                'отсутствует соцпакет, недостаточное количество социальных льгот, предоставляемых организацией',
                'неудовлетворительный уровень заработной платы', 'плохое руководство',
                'предприятие не имеет перспектив в будущем',
                'на других предприятиях условия работы намного лучше',
                'таких причин нет']
            return An[df['A6'][Index]]
        elif Qwestion == 7:
            An = ['да, точно выше', 'скорее выше', 'такая же', 'ниже']
            return An[df['A7'][Index]]
        elif Qwestion == 8:
            An = ['согласен', 'не согласен', 'затрудняюсь ответить']
            return An[df['A8'][Index]]
        elif Qwestion == 9:
            An = ['значительно/несколько улучшилась', 'не изменилась', 'значительно/несколько ухудшилась']
            return An[df['A9'][Index]]
        elif Qwestion == 10:
            An = ['полностью позволяет', 'скорее позволяет', 'скорее не позволяет', 'совсем не позволяет']
            return An[df['A10'][Index]]
        elif Qwestion == 11:
            # print("df['A11'][Index]]",df['A11'][Index])
            An = ['знаю', 'не знаю']
            return An[df['A11'][Index]]
        elif Qwestion == 12:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A12'][Index]]
        elif Qwestion == 13:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён', 'не удовлетворён']
            return An[df['A13'][Index]]
        elif Qwestion == 14:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён', 'не удовлетворён']
            return An[df['A14'][Index]]
        elif Qwestion == 15:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A15'][Index]]
        elif Qwestion == 16:
            An = ['полностью реально', 'скорее реально', 'скорее не реально', 'совсем не реально']
            return An[df['A16'][Index]]
        elif Qwestion == 17:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A17'][Index]]
        elif Qwestion == 18:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A18'][Index]]
        elif Qwestion == 19:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A19'][Index]]
        elif Qwestion == 20:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A20'][Index]]
        elif Qwestion == 21:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A21'][Index]]
        elif Qwestion == 22:
            An = ['полностью удовлетворён (количество конкурсов достаточно)',
                  'скорее удовлетворён (конкурсы проводятся, но хотелось бы больше)',
                  'скорее не удовлетворён (конкурсы проводятся крайне редко)',
                  'полностью не удовлетворён (конкурсы не проводятся)']
            return An[df['A22'][Index]]
        elif Qwestion == 23:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A23'][Index]]
        elif Qwestion == 24:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A24'][Index]]
        elif Qwestion == 25:
            An = ['полностью удовлетворён (предприятие содействует в получении кредита на лучших условиях)',
                  'скорее удовлетворён (предприятие содействует в получении кредита на лучших условиях, но для меня это не актуально)',
                  'скорее не удовлетворён (на предприятии программы есть, но они не лучше тех, что есть на рынке)',
                  'полностью не удовлетворён (на предприятии нет таких программ)']
            return An[df['A25'][Index]]
        elif Qwestion == 26:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A26'][Index]]
        elif Qwestion == 27:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён','Другое']#,'на работу добираюсь пешком, личным или общественным транспортом']
            return An[df['A27'][Index]]
        elif Qwestion == 28:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A28'][Index]]
        elif Qwestion == 29:
            An = ['полностью удовлетворён', 'скорее удовлетворён', 'скорее не удовлетворён',
                  'полностью не удовлетворён']
            return An[df['A29'][Index]]
        elif Qwestion == 30:
            An = ['постоянно', 'часто', 'редко', 'совсем не получаю']
            return An[df['A30'][Index]]
        elif Qwestion == 31:
            An = ['полностью понятно', 'скорее понятно', 'не всегда понятно', 'чаще не понятно']
            return An[df['A31'][Index]]
        elif Qwestion == 32:
            An = ['полностью справедлива', 'скорее справедлива', 'скорее не справедлива', 'совсем не справедлива']
            return An[df['A32'][Index]]
        elif Qwestion == 33:
            An = ['сказываются положительно', 'скорее сказываются положительно', 'скорее не сказываются',
                  'совсем не сказываются']
            return An[df['A33'][Index]]
        elif Qwestion == 34:
            An = ['полностью влияют', 'скорее влияют', 'скорее не влияют', 'совсем не влияют']
            return An[df['A34'][Index]]
        elif Qwestion == 35:
            An = ['меньше 3 месяцев', 'от трёх месяцев до 1 года', '1 - 2 года', '2 - 3 года', '3 - 5 лет',
                  '5 - 10 лет', '10 - 25 лет', '25 лет и больше']
            return An[df['A35'][Index]]
        elif Qwestion == 36:
            An = ['моложе 20 лет', '20-30 лет', '31-40 лет', '41-50 лет', '51-60 лет', '61-70 лет', 'старше70 лет']
            return An[df['A36'][Index]]
        elif Qwestion == 37:
            An = ['мужской', 'женский']
            return An[df['A37'][Index]]
        elif Qwestion == 38:
            An = ['среднее общее (школа)', 'среднее специальное (училище, техникум, колледж, среднее профессиональное )', 'высшее (несколько высших)']
            return An[df['A38'][Index]]
        elif Qwestion == 39:
            An = ['руководитель', 'специалист', 'рабочий']
            return An[df['A39'][Index]]
        elif Qwestion == 4:
            return str(Index)

    Answer = FindAnsText(Qwestion, Counter)
    radio_buttons = driver.find_elements(By.XPATH, "//input[contains(@class, 'ant-radio-input')]")
    for radio_button in radio_buttons:
        if radio_button.accessible_name == Answer:
            radio_button.click()
    if sleepAfterAnswer:
        time.sleep(sleeptime)


def AnswerNPS(driver, Index):
    # time.sleep(2)
    element = WebDriverWait(driver, WaitingTime).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'ballWrapper_9614cd1c3d8059991014d17c5effe8ff'))
    )
    radio_buttons = driver.find_elements(By.CLASS_NAME, 'ballWrapper_9614cd1c3d8059991014d17c5effe8ff')
    # print(radio_buttons)
    # print('df[A4][Index]',df['A4'][Index])
    # print('len(radio_buttons)',len(radio_buttons))
    for radio_button in radio_buttons:
        # print(radio_button.text)
        if radio_button.text == str(df['A4'][Index]):
            radio_button.click()
    if sleepAfterAnswer:
        time.sleep(sleeptime)


def AnswerForm(FormNumber, driver):
    try:
        button = driver.find_element(By.CLASS_NAME, 'ant-btn-primary')
        button.click()
    #     element = WebDriverWait(driver, WaitingTime).until(
    # EC.presence_of_element_located((By.CLASS_NAME, 'ant-btn-primary'))
    # )
        time.sleep(sleeptime)
        # print(f'Вопрос {FormNumber} отвечен')
    except:
        print(f'Вопрос {FormNumber} не отвечен: {driver}')


# Явное ожидание, чтобы убедиться, что кнопка доступна
corr, uncorr = 0, 0
counter = 0
for i in range(len(df['A1'])):
    t1 = datetime.now()
    driver = webdriver.Chrome()
    driver.get(url)
    element = WebDriverWait(driver, WaitingTime).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'ant-radio-input')]"))
    )
    # time.sleep(6)
    try:
        AnswerRadio(1, driver, counter)
        AnswerForm(1, driver)
        AnswerRadio(2, driver, counter)
        AnswerForm(2, driver)
        AnswerRadio(3, driver, counter)
        AnswerForm(3, driver)
        # AnswerRadio(4, driver, counter)
        AnswerNPS(driver, counter)
        AnswerForm(4, driver)
        AnswerRadio(5, driver, counter)
        AnswerForm(5, driver)
        AnswerRadio(6, driver, counter)
        AnswerForm(6, driver)
        AnswerRadio(7, driver, counter)
        AnswerForm(7, driver)
        AnswerRadio(8, driver, counter)
        AnswerForm(8, driver)
        AnswerRadio(9, driver, counter)
        AnswerForm(9, driver)
        AnswerRadio(10, driver, counter)
        AnswerForm(10, driver)
        AnswerRadio(11, driver, counter)
        AnswerForm(11, driver)
        AnswerRadio(12, driver, counter)
        AnswerForm(12, driver)
        AnswerRadio(13, driver, counter)
        AnswerForm(13, driver)
        AnswerRadio(14, driver, counter)
        AnswerForm(14, driver)
        AnswerRadio(15, driver, counter)
        AnswerForm(15, driver)
        AnswerRadio(16, driver, counter)
        AnswerForm(16, driver)
        AnswerRadio(17, driver, counter)
        AnswerForm(17, driver)
        AnswerRadio(18, driver, counter)
        AnswerForm(18, driver)
        AnswerRadio(19, driver, counter)
        AnswerForm(19, driver)
        AnswerRadio(20, driver, counter)
        AnswerForm(20, driver)
        AnswerRadio(21, driver, counter)
        AnswerForm(21, driver)
        AnswerRadio(22, driver, counter)
        AnswerForm(22, driver)
        AnswerRadio(23, driver, counter)
        AnswerForm(23, driver)
        AnswerRadio(24, driver, counter)
        AnswerForm(24, driver)
        AnswerRadio(25, driver, counter)
        AnswerForm(25, driver)
        AnswerRadio(26, driver, counter)
        AnswerForm(26, driver)
        AnswerRadio(27, driver, counter)
        AnswerForm(27, driver)
        AnswerRadio(28, driver, counter)
        AnswerForm(28, driver)
        AnswerRadio(29, driver, counter)
        AnswerForm(29, driver)
        AnswerRadio(30, driver, counter)
        AnswerForm(30, driver)
        AnswerRadio(31, driver, counter)
        AnswerForm(31, driver)
        AnswerRadio(32, driver, counter)
        AnswerForm(32, driver)
        AnswerRadio(33, driver, counter)
        AnswerForm(33, driver)
        AnswerRadio(34, driver, counter)
        AnswerForm(34, driver)
        AnswerRadio(35, driver, counter)
        AnswerForm(35, driver)
        AnswerRadio(36, driver, counter)
        AnswerForm(36, driver)
        AnswerRadio(37, driver, counter)
        AnswerForm(37, driver)
        AnswerRadio(38, driver, counter)
        AnswerForm(38, driver)
        AnswerRadio(39, driver, counter)
        AnswerForm(39, driver)
        print(f'Форма {i} заполнена за {datetime.now() - t1} {datetime.now()}')
        driver.quit()
        time.sleep(sleeptime)
        counter += 1
    except Exception as e:
        counter += 1
        uncorr += 1
        print(f'Форма {i} не заполнена за {datetime.now() - t1} {datetime.now()}')
        # print(f"Ошибка: {e}")

print('Правильно отправлены', corr)
print('Неравильно отправлены', uncorr)

# Закрываем драйвер
