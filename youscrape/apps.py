import asyncio

from django.apps import AppConfig
import logging

from youscrape.discord.music_bot import start_discord_bot

logger = logging.getLogger(__name__)

class YouscrapeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youscrape'
    print("THOMAS IS ALIVE")
    def ready(self):
        asyncio.run(start_discord_bot())