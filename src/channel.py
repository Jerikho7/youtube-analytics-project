import os
import json
from googleapiclient.discovery import build

API_KEY = os.getenv('YOUTUBE_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.url = f'https://www.youtube.com/channel/{channel_id}'

        data_channel = self.get_service().channels().list(part='snippet,statistics', id=self.__channel_id).execute()
        item = data_channel["items"][0]

        self.title = item["snippet"]["title"]
        self.description = item["snippet"]["description"]

        self.subscriber_count = int(item["statistics"]["subscriberCount"])
        self.video_count = int(item["statistics"]["videoCount"])
        self.viewing_count = int(item["statistics"]["viewCount"])

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __ne__(self, other):
        return self.subscriber_count != other.subscriber_count

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=API_KEY)
        return service

    def to_json(self, json_file):
        request_channel_data = self.get_service().channels().list(part='snippet,statistics', id=self.__channel_id)
        channel_data_to_load = request_channel_data.execute()
        with open(json_file, "w") as file:
            json.dump(channel_data_to_load, file)

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        request_channel_data = self.get_service().channels().list(part='snippet,statistics', id=self.__channel_id)
        channel_data: object = request_channel_data.execute()

        print(json.dumps(channel_data, indent=2, ensure_ascii=False))
