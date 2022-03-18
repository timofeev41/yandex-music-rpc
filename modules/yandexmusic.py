import typing as tp

from yandex_music import Client, QueueItem, TrackId


client = Client(token="TOKEN").init()


def get_all_queues() -> list[QueueItem]:
    return client.queues_list()


def get_latest_queue() -> QueueItem:
    return get_all_queues()[0]


def get_current_playing_track() -> TrackId:
    return get_latest_queue().fetch_queue().get_current_track()


def get_track_info(track_id: str) -> dict[str, tp.Any]:
    track: dict[str, tp.Any] = client.tracks(track_ids=track_id)[0]
    return {
        "title": track["title"],
        "track_id": track_id,
        "artists": [artist["name"] for artist in track["artists"]],
        "album": track["albums"][-1]["title"],
        "album_id": track["albums"][-1]["id"],
    }
