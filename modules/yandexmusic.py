import typing as tp

from yandex_music import Client


client = Client(token="YOUR TOKEN").init()


def get_all_queues() -> dict[str, str]:
    return client.queues_list()


def get_latest_queue() -> dict[str, str]:
    return get_all_queues()[0]


def get_current_playing_track() -> dict[str, str]:
    return get_latest_queue().fetch_queue().get_current_track()


def get_track_info(track_id: str) -> dict[str, str]:
    track: dict[str, tp.Any] = client.tracks(track_ids=track_id)[0]
    return {
        "title": track["title"],
        "artists": [artist["name"] for artist in track["artists"]],
        "album": track["albums"][-1]["title"],
    }


# print(get_track_info(get_current_playing_track()["track_id"]))
