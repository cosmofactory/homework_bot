<<<<<<< HEAD
import os
import logging
import requests
import time
import telegram
from dotenv import load_dotenv
from exceptions import NoTokenProvidedException, NoHomeworksFromAPI
from exceptions import HTTPStatusNotOk, RequestException
from exceptions import WrongStatusException, MissingHomeworkName
from exceptions import CantSendMessageException
from http import HTTPStatus


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    filemode='w'
)

PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
=======
...

load_dotenv()


PRACTICUM_TOKEN = ...
TELEGRAM_TOKEN = ...
TELEGRAM_CHAT_ID = ...

>>>>>>> 589e95bb1e911131f5a99bd95dbd398d65b5bbdf
RETRY_PERIOD = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}


HOMEWORK_VERDICTS = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


def check_tokens():
<<<<<<< HEAD
    """Checking if tokens exist in env."""
    list_of_tokens = (
        PRACTICUM_TOKEN,
        TELEGRAM_TOKEN,
        TELEGRAM_CHAT_ID
    )
    for i in list_of_tokens:  # checking if all the tokens are here
        if i is None:
            logging.critical('Нет токена.')
            raise NoTokenProvidedException


def send_message(bot, message):
    """Sends megssage with information from main function."""
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        logging.debug('Сообщение успешно отправлено.')
    except Exception:
        logging.error('Не получилось отправить сообщение.')
        raise CantSendMessageException


def get_api_answer(timestamp):
    """Requests homework information from Yandex."""
    PAYLOAD = {'from_date': timestamp}
    try:
        response = requests.get(
            ENDPOINT,
            headers=HEADERS,
            params=PAYLOAD
        )
        if response.status_code != HTTPStatus.OK:
            raise HTTPStatusNotOk('Http status not OK')
        return response.json()
    except requests.RequestException:
        raise RequestException


def check_response(response):
    """Check if response if within the documentation."""
    if not isinstance(response, dict):
        raise TypeError(
            'Неверный тип ответа от Yandex API '
            'Ответ должен быть словарем.'
        )
    if 'homeworks' not in response:
        raise NoHomeworksFromAPI
    if not isinstance(response['homeworks'], list):
        raise TypeError(
            'Неверный тип ответа от Yandex API '
            'Ключ homeworks должен быть списком.'
        )


def parse_status(homework):
    """Parses the information from Yandex.
    to check the result of the homework
    """
    if homework['status'] not in HOMEWORK_VERDICTS:
        raise WrongStatusException
    if 'homework_name' not in homework:
        raise MissingHomeworkName
    homework_name = homework['homework_name']
    verdict = HOMEWORK_VERDICTS[homework['status']]
=======
    ...


def send_message(bot, message):
    ...


def get_api_answer(timestamp):
    ...


def check_response(response):
    ...


def parse_status(homework):
    ...

>>>>>>> 589e95bb1e911131f5a99bd95dbd398d65b5bbdf
    return f'Изменился статус проверки работы "{homework_name}". {verdict}'


def main():
<<<<<<< HEAD
    """Main function of the bot."""
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    timestamp = int(time.time())
    check_tokens()
    message_old = ''
    while True:
        try:
            response = get_api_answer(timestamp)
            check_response(response)
            new_homework = response.get('homeworks')
            if new_homework != []:
                message = parse_status(new_homework[0])
                if message != message_old:
                    send_message(bot, message)
                    message_old = message
        except Exception as error:
            message = f'Сбой в работе программы: {error}'
            if message != message_old:
                send_message(bot, message)
                message_old = message
            logging.error(error, exc_info=True)
        finally:
            time.sleep(RETRY_PERIOD)
=======
    """Основная логика работы бота."""

    ...

    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    timestamp = int(time.time())

    ...

    while True:
        try:

            ...

        except Exception as error:
            message = f'Сбой в работе программы: {error}'
            ...
        ...
>>>>>>> 589e95bb1e911131f5a99bd95dbd398d65b5bbdf


if __name__ == '__main__':
    main()
