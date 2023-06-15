import requests


class News:
    def __init__(self, parameters):
        response = requests.get(url=' https://newsapi.org/v2/everything', params=parameters)

        data = response.json()

        self.top_three = []

        for _ in range(3):
            title = data['articles'][_]['title']
            description = data['articles'][_]['description']
            url = data['articles'][1]['url']
            news_dict = {
                'title': title,
                'description': description,
                'url': url
            }

            self.top_three.append(news_dict)
