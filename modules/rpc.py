from pypresence import Presence  # The simple rich presence client in pypresence
import time

import modules.yandexmusic as ym

client_id = "954472930530709544"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client

last_track = ym.get_current_playing_track()
last_track_data = ym.get_track_info(last_track["track_id"])

RPC.connect()


def _update_status(state: str) -> None:
    RPC.update(state=state)


def poll():
    global last_track
    global last_track_data
    while True:
        _update_status(f"Сейчас слушает {last_track_data['title']}-{','.join(last_track_data['artists'])}")
        time.sleep(15)
        last_track = ym.get_current_playing_track()
        last_track_data = ym.get_track_info(last_track["track_id"])
