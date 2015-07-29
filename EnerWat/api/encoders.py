import news.models


class NewsEncoder:
    @staticmethod
    def encode(news: news.models.News):
        retval = {}
        retval['content'] = news.content
        retval['date'] = news.date.isoformat()
        retval['keyword'] = news.keyword
        retval['subject'] = news.subject
        return retval
