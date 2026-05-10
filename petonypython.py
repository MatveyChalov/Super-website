from flask import Flask, render_template_string
import random

app = Flask(__name__)

# ==========================================
# 1. БАЗЫ КОНТЕНТА (можно расширять до бесконечности)
# ==========================================
FACTS = [
    "Средний пользователь разблокирует телефон 150+ раз в день.",
    "90% людей испытывают 'фантомную вибрацию'.",
    "Синий свет экранов подавляет выработку мелатонина.",
    "Соцсети используют механику игровых автоматов для удержания внимания.",
    "Многозадачность с гаджетами временно снижает IQ на 10-15 пунктов.",
    "Термин 'номофобия' официально включён в психологические справочники.",
    "Уведомления вызывают микровыбросы дофамина, формируя петлю зависимости."
]

QUOTES = [
    "«Технологии — отличный слуга, но ужасный хозяин». — Неизвестный автор",
    "«Отключись, чтобы подключиться к реальной жизни». — Digital Detox Manifesto",
    "«Внимание — это самая ценная валюта XXI века». — Тим Ву",
    "«Простота интерфейса часто скрывает сложность манипуляции». — Tech Ethics",
    "«Не позволяй алгоритмам решать, что для тебя важно». — Anonymous"
]

TIPS = [
    "Правило 20-20-20: каждые 20 минут смотри на объект в 6 метрах в течение 20 секунд.",
    "Оставляй телефон в другой комнате во время приёма пищи.",
    "Включи grayscale (чёрно-белый режим) — это снижает привлекательность иконок.",
    "Отключи push-уведомления для всех приложений, кроме звонков и мессенджеров близких.",
    "Заряжай смартфон вне спальни. Купи обычный будильник.",
    "Удали ярлыки соцсетей с главного экрана. Спрячь их в папку на последнем экране.",
    "Попробуй 'цифровой шабат': 12 часов в неделю без интернета."
]

MYTHS = [
    "Миф: Режим 'Не беспокоить' полностью защищает от стресса. Реальность: Тревога ожидания остаётся.",
    "Миф: Чтение с экрана равно чтению с бумаги. Реальность: Бумага улучшает пространственное запоминание текста.",
    "Миф: Многозадачность повышает продуктивность. Реальность: Мозг теряет до 40% времени на переключение контекста.",
    "Миф: 'Я просто проверяю почту'. Реальность: Каждый вход в почтовый клиент затягивает в среднем на 8 минут.",
    "Миф: Детокс нужен только подросткам. Реальность: 68% взрослых испытывают цифровой стресс ежедневно."
]

STATS = [
    "В мире более 4.9 млрд активных пользователей соцсетей.",
    "Среднее время в интернете в день: 6 часов 40 минут.",
    "TikTok удерживает внимание дольше всего: средняя сессия ~95 минут.",
    "Люди касаются экрана смартфона в среднем 2617 раз в день.",
    "54% подростков признают, что проводят в соцсетях слишком много времени."
]

TOOLS = [
    "Forest: выращивай виртуальные деревья, пока не трогаешь телефон.",
    "Freedom: блокирует отвлекающие сайты на всех устройствах одновременно.",
    "One Sec: заставляет сделать глубокий вдох перед открытием соцсети.",
    "Screen Time (iOS) / Digital Wellbeing (Android): встроенные трекеры.",
    "Minimalist Phone: лаунчер, превращающий смартфон в утилитарный инструмент."
]

CHALLENGES = [
    "День 1: Удали одно приложение, которым не пользовался месяц.",
    "День 2: Не бери телефон в туалет. Серьёзно.",
    "День 3: Гуляй 30 минут без наушников и телефона.",
    "День 4: Отключи уведомления для всех групповых чатов.",
    "День 5: Почисти подписки: отпишись от 10 аккаунтов, которые раздражают."
]

BENEFITS = [
    "Улучшение качества и глубины сна.",
    "Снижение уровня кортизола (гормона стресса).",
    "Повышение концентрации на 30-40%.",
    "Больше времени на хобби и живое общение.",
    "Снижение нагрузки на глаза и шейный отдел позвоночника."
]

HISTORY = [
    "1984: Появление первого массового ПК. Люди боялись, что компьютеры заменят книги.",
    "1998: Google меняет способ поиска информации. Начинается эпоха мгновенного доступа.",
    "2007: iPhone делает интернет карманным. Граница между онлайн и офлайн стирается.",
    "2010: Instagram запускает ленту. Визуальный контент становится новым наркотиком.",
    "2016: Алгоритмические ленты окончательно вытесняют хронологический порядок."
]

PSYCHOLOGY = [
    "Дофаминовая петля: ожидание награды (лайка) важнее самой награды.",
    "Эффект Зейгарник: мозг запоминает незавершённые задачи, поэтому бесконечный скролл не даёт 'закрыть вкладку'.",
    "Социальное сравнение: лента создаёт иллюзию, что у других жизнь интереснее.",
    "Цифровой шум: постоянный фон снижает способность к глубокому мышлению.",
    "Страх пропущенного (FOMO): эволюционный механизм, который теперь эксплуатируется маркетологами."
]

# ==========================================
# 2. ГЕНЕРАЦИЯ КОНФИГУРАЦИЙ 50 СТРАНИЦ
# ==========================================
PAGE_CONFIGS = []
categories = [
    ("fact", "Факт", FACTS),
    ("quote", "Цитата", QUOTES),
    ("tip", "Совет", TIPS),
    ("myth", "Миф", MYTHS),
    ("stat", "Статистика", STATS),
    ("tool", "Инструмент", TOOLS),
    ("challenge", "Челлендж", CHALLENGES),
    ("benefit", "Польза", BENEFITS),
    ("history", "История", HISTORY),
    ("psych", "Психология", PSYCHOLOGY)
]

for i in range(1, 51):
    cat_type, cat_name, pool = categories[(i - 1) % 10]
    PAGE_CONFIGS.append({
        "slug": f"page-{i:02d}",
        "title": f"Страница {i:02d}: {cat_name} #{(i-1)//10 + 1}",
        "type": cat_type,
        "pool": pool
    })

# ==========================================
# 3. ЕДИНЫЙ HTML-ШАБЛОН (Jinja2)
# ==========================================
PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; background: #f8f9fa; color: #333; }
        nav { background: #fff; padding: 15px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .nav-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); gap: 6px; max-height: 150px; overflow-y: auto; padding: 5px; }
        .nav-grid a { text-decoration: none; color: #495057; padding: 6px; background: #e9ecef; border-radius: 4px; text-align: center; font-size: 0.85em; transition: 0.2s; }
        .nav-grid a:hover { background: #339af0; color: white; }
        .content { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); min-height: 200px; }
        .card { background: #e7f5ff; padding: 20px; border-left: 5px solid #339af0; font-size: 1.25em; line-height: 1.6; margin: 20px 0; }
        .refresh-btn { display: inline-block; margin-top: 15px; padding: 10px 20px; background: #228be6; color: white; text-decoration: none; border-radius: 5px; }
        h1 { margin-top: 0; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        footer { margin-top: 30px; text-align: center; color: #888; font-size: 0.9em; }
    </style>
</head>
<body>
    <nav>
        <div style="margin-bottom: 8px; font-weight: bold;">🗺 Навигация (50 страниц):</div>
        <div class="nav-grid">
            <a href="/">🏠 Главная</a>
            {% for p in pages %}
            <a href="/{{ p.slug }}">{{ p.title }}</a>
            {% endfor %}
        </div>
    </nav>
    <div class="content">
        <h1>{{ title }}</h1>
        {{ content | safe }}
        <a href="/{{ slug }}" class="refresh-btn">🔄 Обновить содержимое</a>
    </div>
    <footer>Мега-портал цифровой гигиены • Flask Demo • 2026</footer>
</body>
</html>
"""

# ==========================================
# 4. ЛОГИКА ГЕНЕРАЦИИ КОНТЕНТА
# ==========================================
def get_page_content(config):
    item = random.choice(config["pool"])
    styles = {
        "fact": f"<div class='card'>📖 {item}</div>",
        "quote": f"<div class='card' style='border-color:#9775fa'>💬 <i>{item}</i></div>",
        "tip": f"<div class='card' style='border-color:#40c057'>💡 {item}</div>",
        "myth": f"<div class='card' style='border-color:#fa5252'>👾 <b>Миф:</b> {item}</div>",
        "stat": f"<div class='card' style='border-color:#fab005'>📊 {item}</div>",
        "tool": f"<div class='card' style='border-color:#fd7e14'>🛠 {item}</div>",
        "challenge": f"<div class='card' style='border-color:#f76707'>🔥 <b>Задание:</b> {item}</div>",
        "benefit": f"<div class='card' style='border-color:#20c997'>✨ {item}</div>",
        "history": f"<div class='card' style='border-color:#868e96'>📜 {item}</div>",
        "psych": f"<div class='card' style='border-color:#cc5de8'>🧠 {item}</div>"
    }
    return styles.get(config["type"], f"<p>{item}</p>")

# ==========================================
# 5. МАРШРУТЫ
# ==========================================
@app.route("/")
def index():
    content = """
    <h1>🌐 Добро пожаловать в Мега-Портал Цифровой Гигиены!</h1>
    <p>Здесь <b>50 уникальных страниц</b> с фактами, советами, челленджами и инструментами.</p>
    <p>Используй меню выше для навигации. Каждая страница генерирует случайный контент при обновлении.</p>
    <hr>
    <h3>🎲 Быстрый старт:</h3>
    <ul>
        <li>📖 """ + random.choice(FACTS) + """</li>
        <li>💡 """ + random.choice(TIPS) + """</li>
        <li>🔥 """ + random.choice(CHALLENGES) + """</li>
    </ul>
    """
    return render_template_string(PAGE_TEMPLATE, title="Главная страница", content=content, slug="index", pages=PAGE_CONFIGS)

# Фабрика функций-обработчиков (избегает проблемы замыканий в циклах)
def create_page_view(config):
    def view_func():
        return render_template_string(
            PAGE_TEMPLATE,
            title=config["title"],
            content=get_page_content(config),
            slug=config["slug"],
            pages=PAGE_CONFIGS
        )
    return view_func

# Программная регистрация 50 маршрутов
for cfg in PAGE_CONFIGS:
    app.add_url_rule(f"/{cfg['slug']}", cfg['slug'], create_page_view(cfg))

app.run(debug=True)
