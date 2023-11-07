import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY = os.getenv('YOUTUBE_API_KEY')
    youtube = build("youtube", "v3", developerKey=API_KEY)

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        request_channel_data = self.youtube.channels().list(part='snippet,statistics', id=self.channel_id)
        channel_data: object = request_channel_data.execute()
        
        print(json.dump(channel_data, indent=2, ensure_ascii=False))
