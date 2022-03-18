import typing as tp

from pypresence import Presence  # The simple rich presence client in pypresence
import time

import modules.yandexmusic as ym

client_id = "CLIENT ID"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client

last_track = ym.get_current_playing_track()
last_track_data = ym.get_track_info(last_track["track_id"])


RPC.connect()


def _update_status(state: str, details: str, song: dict[str, tp.Any]) -> None:
    RPC.update(
        state=details,
        details=state,
        buttons=[
            {
                "label": "Listen on Yandex.Music",
                "url": f"https://music.yandex.ru/album/{song['album_id']}/track/{song['track_id']}",
            },
            {
                "label": "Album on Yandex.Music",
                "url": f"https://music.yandex.ru/album/{song['album_id']}",
            },
        ],
    )


def poll() -> None:
    global last_track
    global last_track_data
    while True:
        _update_status(
            f"Сейчас слушает:", f"{last_track_data['title']} - {', '.join(last_track_data['artists'])}", last_track
        )
        time.sleep(15)
        last_track = ym.get_current_playing_track()
        last_track_data = ym.get_track_info(last_track["track_id"])
