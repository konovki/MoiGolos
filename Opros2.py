from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# url = 'https://moigolos.pro/app/KA6' #Almaz
url = 'https://moigolos.pro/app/KB1' #Almaz_2
# url = 'https://moigolos.pro/app/K6B' #Concern

# df = pd.read_csv('gen3/opros1.csv')
df = pd.read_csv('opros1.csv')
# df = pd.read_csv('test.csv')
sleepAfterAnswer, sleeptime = False, 0.1
st1,st2 = 0.1,0.1
sleep = False
WaitingTime = 60
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
            An = ['моложе 20 лет', '20-30 лет', '31-35 лет', '36-40 лет', '41-50 лет', '51-60 лет', '61-70 лет', 'старше70 лет']
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



# Открываем веб-страницу



def AnswerNPS(driver, Index):
    element = WebDriverWait(driver, WaitingTime).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'ballWrapper_9614cd1c3d8059991014d17c5effe8ff'))
    )
    radio_buttons = driver.find_elements(By.CLASS_NAME, 'ballWrapper_9614cd1c3d8059991014d17c5effe8ff')

    for radio_button in radio_buttons:
        if radio_button.text == str(df['A4'][Index]):
            radio_button.click()

class text_to_be_equal_to:
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text
        
    def __call__(self, driver):
        try:
            element_text = driver.find_element(*self.locator).text
            return element_text == self.text
        except:
            return False




# Явное ожидание, чтобы убедиться, что кнопка доступна
corr, uncorr = 0, 0
errors = []
counter = 0
FormsNumber = df.shape[0]

for i in range(FormsNumber):
    t1 = datetime.now()
    flag = False
    while not flag:
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            element = WebDriverWait(driver, WaitingTime).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'ant-radio-input')]"))
            )
            flag = True
        except:
            print(f'Reload Form: {datetime.now().time()}')
            driver.quit()

    try:
        k = 1
        while k < 40:
            if k == 4:
                AnswerNPS(driver, counter)
            else:
                WebDriverWait(driver, WaitingTime).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'ant-radio-input')]")))
                buttons = driver.find_elements(By.XPATH, "//input[contains(@class, 'ant-radio-input')]")
                if sleep:
                    time.sleep(st1)
                button = buttons[df[f'A{k}'][counter]]
                if sleep:
                    time.sleep(st2)                
                button.click()
                
            WebDriverWait(driver, WaitingTime).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ant-btn-primary')))
            button = driver.find_element(By.CLASS_NAME, 'ant-btn-primary')
            button.click()
            if k != 39:
                WebDriverWait(driver,WaitingTime).until(text_to_be_equal_to((By.CLASS_NAME, 'surveyProgress_a8176cece3ddc9b524a852b2d9ca295e'), f'{k+1} / 39'))
            k += 1
        driver.quit()
        counter += 1
        corr += 1 
        print(f'Форма {i+1} из {FormsNumber} заполнена за {int((datetime.now() - t1).total_seconds())} {datetime.now().time()} {corr} {uncorr } {counter}')
    except Exception as e:
        counter += 1
        uncorr += 1
        driver.quit()
        print(f'Форма {i+1} из {FormsNumber} не заполнена за {int((datetime.now() - t1).total_seconds())} {datetime.now()} {datetime.now().time()} {corr} {uncorr } {counter}')
        print(f"Ошибка: {e}")
        errors.append(i)

print('Правильно отправлены', corr)
print('Неравильно отправлены', uncorr)
print('errors',errors)

# Закрываем драйвер
