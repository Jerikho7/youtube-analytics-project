import os
from googleapiclient.discovery import build

API_KEY = os.getenv('YOUTUBE_API_KEY')


class Video:
    def __init__(self, video_id):
        self.__video_id = video_id
        self.url = f"https://www.youtube.com/{video_id}"

        data_video = self.get_service().videos().list(part='snippet,statistics', id=self.__video_id).execute()
        item = data_video["items"][0]

        self.title = item["snippet"]["title"]

        self.view_count = int(item["statistics"]["viewCount"])
        self.like_count = int(item["statistics"]["likeCount"])

    def __str__(self):
        return f"{self.title}"

    @property
    def video_id(self):
        return self.__video_id

    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=API_KEY)
        return service


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id