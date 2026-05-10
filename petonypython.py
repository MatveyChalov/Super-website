from flask import Flask
import random

app = Flask(__name__)

# --- БАЗЫ ДАННЫХ ДЛЯ СТРАНИЦ ---

facts_list = [
    "Средний пользователь проверяет смартфон 150+ раз в день.",
    "90% людей испытывают 'фантомную вибрацию'.",
    "Синий свет экранов блокирует мелатонин.",
    "Соцсети используют механику игровых автоматов.",
    "Многозадачность снижает IQ во время задачи.",
    "Номофобия — страх остаться без телефона.",
    "Уведомления вызывают микродозы дофамина."
]

quotes_list = [
    "«Технологии — отличный слуга, но ужасный хозяин». — неизвестный автор",
    "«Отключись, чтобы подключиться к жизни». — Digital Detox Manifesto",
    "«Внимание — это новая валюта». — Тим Ву",
    "«Простота — это высшая форма утонченности». – Леонардо да Винчи",
    "«Не позволяй экрану заменять тебе мир». – Anonymous"
]

tips_list = [
    "Правило 20-20-20: Каждые 20 минут смотри на 20 футов вдаль на 20 секунд.",
    "Оставляй телефон в другой комнате во время еды.",
    "Используй черно-белый режим экрана, чтобы снизить привлекательность иконок.",
    "Отключи все уведомления, кроме звонков от близких.",
    "Заряжай телефон вне спальни.",
    "Удали приложения соцсетей с главного экрана.",
    "Попробуй 'цифровой шабат' — один день без гаджетов в неделю."
]

myths_list = [
    "Миф: Режим 'не беспокоюсь' полностью защищает от стресса. (Реальность: Тревожность ожидания остается).",
    "Миф: Мы используем только 10% мозга. (Реальность: Это миф, но гаджеты действительно перегружают когнитивные функции).",
    "Миф: Чтение с экрана так же полезно, как с бумаги. (Реальность: Бумага улучшает запоминание контекста).",
    "Миф: Многозадачность эффективна. (Реальность: Мозг просто быстро переключается, теряя энергию)."
]

stats_list = [
    "В мире более 4.9 миллиарда пользователей соцсетей.",
    "Среднее время в интернете в день: 6 часов 40 минут.",
    "TikTok имеет самое высокое среднее время сессии — 95 минут.",
    "Люди касаются своего телефона в среднем 2617 раз в день.",
    "54% подростков чувствуют, что проводят в соцсетях слишком много времени."
]

tools_list = [
    "Forest: Выращивай виртуальные деревья, пока не трогаешь телефон.",
    "Freedom: Блокирует отвлекающие сайты на всех устройствах.",
    "One Sec: Заставляет тебя сделать глубокий вдох перед открытием соцсети.",
    "Screen Time (iOS) / Digital Wellbeing (Android): Встроенные анализаторы.",
    "Minimalist Phone: Лаунчер, превращающий смартфон в инструмент, а не игрушку."
]

challenges_list = [
    "День 1: Удали одно приложение, которым не пользуешься.",
    "День 2: Не бери телефон в туалет.",
    "День 3: Гуляй 30 минут без наушников и телефона.",
    "День 4: Отключи push-уведомления для всех чатов.",
    "День 5: Почисти подписки: отпишись от 10 аккаунтов, которые раздражают.",
    "День 6: Прочитай 10 страниц бумажной книги.",
    "День 7: Полный цифровой детокс с утра до обеда."
]

benefits_list = [
    "Улучшение качества сна.",
    "Снижение уровня тревожности.",
    "Повышение концентрации внимания.",
    "Больше времени на хобби.",
    "Улучшение отношений с близкими.",
    "Снижение нагрузки на глаза.",
    "Ощущение контроля над своей жизнью."
]

quiz_data = {
    "question": "Сколько часов в день ты проводишь в смартфоне?",
    "answers": [
        "< 2 часов (Ты киборг или монах? 🧘)",
        "2-4 часа (Золотая середина ⚖️)",
        "4-6 часов (Зона риска ⚠️)",
        "> 6 часов (Пора на детокс! 🚑)"
    ]
}

about_text = """
Этот сайт создан для тех, кто хочет вернуть контроль над своим вниманием.
Мы собрали факты, инструменты и советы, чтобы помочь тебе жить в гармонии с технологиями, 
а не быть их рабом.
<br><br>
Версия сайта: 1.0 (Mega-Edition)
"""

# --- ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ---

def generate_page(title, content_html):
    """Создает красивую страницу с единым меню"""
    menu = '''
    <nav style="background: #f0f0f0; padding: 10px; border-bottom: 2px solid #ddd;">
        <a href="/">🏠 Главная</a> |
        <a href="/facts">📚 Факты</a> |
        <a href="/quotes">💬 Цитаты</a> |
        <a href="/tips">💡 Советы</a> |
        <a href="/myths">👾 Мифы</a> |
        <a href="/stats">📊 Статистика</a> |
        <a href="/tools">🛠 Инструменты</a> |
        <a href="/challenge">🏆 Челлендж</a> |
        <a href="/benefits">✨ Польза</a> |
        <a href="/quiz">❓ Тест</a> |
        <a href="/about">ℹ️ О нас</a>
    </nav>
    '''
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{ font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; }}
            h1 {{ color: #2c3e50; }}
            .content {{ background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
            .random-box {{ background: #e8f4f8; padding: 15px; border-left: 5px solid #3498db; margin: 20px 0; font-size: 1.2em; }}
        </style>
    </head>
    <body>
        {menu}
        <div class="content">
            <h1>{title}</h1>
            {content_html}
        </div>
    </body>
    </html>
    '''

# --- 10 МАРШРУТОВ (СТРАНИЦ) ---

@app.route("/")
def index():
    content = "<p>Добро пожаловать в центр цифровой осознанности.</p>"
    content += "<p>Выбери раздел в меню выше, чтобы начать путешествие.</p>"
    content += "<div class='random-box'>💡 <b>Совет дня:</b> " + random.choice(tips_list) + "</div>"
    return generate_page("Главная страница", content)

@app.route("/facts")
def facts():
    fact = random.choice(facts_list)
    content = f"<div class='random-box'>{fact}</div>"
    content += "<p><i>Нажми обновить страницу, чтобы увидеть другой факт!</i></p>"
    return generate_page("Интересные факты", content)

@app.route("/quotes")
def quotes():
    quote = random.choice(quotes_list)
    content = f"<div class='random-box' style='border-color: #9b59b6;'>{quote}</div>"
    return generate_page("Мудрые цитаты", content)

@app.route("/tips")
def tips():
    tip = random.choice(tips_list)
    content = f"<div class='random-box' style='border-color: #2ecc71;'>{tip}</div>"
    content += "<ul>" + "".join([f"<li>{t}</li>" for t in random.sample(tips_list, 3)]) + "</ul>"
    return generate_page("Полезные советы", content)

@app.route("/myths")
def myths():
    myth = random.choice(myths_list)
    content = f"<div class='random-box' style='border-color: #e74c3c;'>{myth}</div>"
    return generate_page("Разрушение мифов", content)

@app.route("/stats")
def stats():
    stat = random.choice(stats_list)
    content = f"<div class='random-box' style='border-color: #f39c12;'>📈 {stat}</div>"
    return generate_page("Статистика зависимостей", content)

@app.route("/tools")
def tools():
    tool = random.choice(tools_list)
    content = f"<p>Рекомендуем попробовать: <b>{tool}</b></p>"
    content += "<hr><h3>Другие популярные приложения:</h3><ul>"
    for t in tools_list:
        if t != tool:
            content += f"<li>{t}</li>"
    content += "</ul>"
    return generate_page("Инструменты контроля", content)

@app.route("/challenge")
def challenge():
    day_task = random.choice(challenges_list)
    content = f"<div class='random-box' style='border-color: #e67e22;'>🔥 Твоя задача на сегодня:<br><b>{day_task}</b></div>"
    return generate_page("Челлендж детокса", content)

@app.route("/benefits")
def benefits():
    benefit = random.choice(benefits_list)
    content = f"<div class='random-box' style='border-color: #1abc9c;'>🌟 Ты получишь: {benefit}</div>"
    return generate_page("Преимущества жизни оффлайн", content)

@app.route("/quiz")
def quiz():
    answer = random.choice(quiz_data["answers"])
    content = f"<h3>{quiz_data['question']}</h3>"
    content += f"<p style='font-size: 1.5em; color: green;'>Твой результат (случайный прогноз): {answer}</p>"
    content += "<p><small>(Это шуточный тест, но задуматься стоит!)</small></p>"
    return generate_page("Мини-тест", content)

@app.route("/about")
def about():
    return generate_page("О проекте", f"<p>{about_text}</p>")

app.run(debug=True)
