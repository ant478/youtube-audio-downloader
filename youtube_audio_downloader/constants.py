import os

CONFIG_DEFAULT_VALUE_BY_FIELD = {
    'format': 'm4a/bestaudio/best',
    'temp_dir': 'temp\\',
    'output_dir': os.path.expanduser('~') + '\\Music\\',
}
CONFIG_PATH = 'config.yaml'

# Texts
VIDEO_URL_INPUT_TEXT = 'Введите id или url видео.\n'
OPTION_INPUT_TEXT = (
    'Выберете вариант скачивания:\n'
    '1. Одним файлом.\n'
    '2. Каждую главу отдельным файлом.\n'
    '3. Каждую главу отдельным файлом с номером главы в имени.\n'
)

CONFIG_VALUE_INPUT_TEXT_BY_FIELD = {
    'format': 'Введите требуемый формат. ({default})\n',
    'temp_dir': 'Введите путь к директории временных файлов. ({default})\n',
    'output_dir': 'Введите путь к директории куда сохранить файлы. ({default})\n',
}

