from datetime import datetime
from get_news import get_news_from_keyword


def sample_responses(input_text):
    user_massage = str(input_text).lower()

    if user_massage in ('hello', 'hi', 'helloes'):
        return "Hey hey!"

    if user_massage in ('who are you', 'who are you?'):
        return "I`m a super-duper cool bot!"

    if user_massage in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    else:
        return "I didn`t catch your point =( \n Try to use /help function."


def keyword_responses(input_text):
    keyword = str(input_text).lower()
    to_send = get_news_from_keyword(keyword)
    to_send = to_send if to_send!="" else "There`re no news by the keywords"
    return to_send




