#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Contains test cases for the downloaders.py module."""


import sys
import time
from pathlib import Path
from typing import List, Dict
import unittest
from unittest import mock

PATH = Path(__file__).parent
sys.path.insert(0, str(PATH.parent))

from youtube_dl_gui import downloaders


YOUTUBEDL_OUTPUT_VIDEO = PATH.joinpath(
    "fixtures/extract_data_video_output.txt"
).read_text(encoding="utf-8")
YOUTUBEDL_OUTPUT_PLAYLIST = PATH.joinpath(
    "fixtures/extract_data_playlist_output.txt"
).read_text(encoding="utf-8")

OUTPUT_VIDEO_EXPECTED = [
    {"status": "Pre Processing"},
    {"status": "Pre Processing"},
    {
        "status": "Downloading",
        "path": "",
        "filename": "Among Us Momentos Divertidos-among-us-momentos-divertidos-2020-09-24-18-28-12-525257.f0",
        "extension": ".mp4",
    },
    {
        "status": "Downloading",
        "percent": "0.1%",
        "filesize": "1.13MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.3%",
        "filesize": "1.13MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.6%",
        "filesize": "1.13MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "1.3%",
        "filesize": "1.13MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "2.7%",
        "filesize": "1.13MiB",
        "speed": "330.59KiB/s",
        "eta": "00:03",
    },
    {
        "status": "Downloading",
        "percent": "5.4%",
        "filesize": "1.13MiB",
        "speed": "192.02KiB/s",
        "eta": "00:05",
    },
    {
        "status": "Downloading",
        "percent": "10.9%",
        "filesize": "1.13MiB",
        "speed": "198.19KiB/s",
        "eta": "00:05",
    },
    {
        "status": "Downloading",
        "percent": "22.0%",
        "filesize": "1.13MiB",
        "speed": "211.94KiB/s",
        "eta": "00:04",
    },
    {
        "status": "Downloading",
        "percent": "41.6%",
        "filesize": "1.13MiB",
        "speed": "261.50KiB/s",
        "eta": "00:02",
    },
    {
        "status": "Downloading",
        "percent": "72.2%",
        "filesize": "1.13MiB",
        "speed": "314.87KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "100.0%",
        "filesize": "1.13MiB",
        "speed": "370.95KiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "speed": "",
        "eta": "",
        "percent": "100%",
        "filesize": "1.13MiB",
    },
    {
        "status": "Downloading",
        "path": "",
        "filename": "Among Us Momentos Divertidos-among-us-momentos-divertidos-2020-09-24-18-28-12-525257.f3",
        "extension": ".m4a",
    },
    {
        "status": "Downloading",
        "percent": "0.2%",
        "filesize": "569.83KiB",
        "speed": "64.50KiB/s",
        "eta": "00:08",
    },
    {
        "status": "Downloading",
        "percent": "0.5%",
        "filesize": "569.83KiB",
        "speed": "193.50KiB/s",
        "eta": "00:02",
    },
    {
        "status": "Downloading",
        "percent": "1.2%",
        "filesize": "569.83KiB",
        "speed": "451.50KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "2.6%",
        "filesize": "569.83KiB",
        "speed": "967.50KiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "5.4%",
        "filesize": "569.83KiB",
        "speed": "1.95MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "11.1%",
        "filesize": "569.83KiB",
        "speed": "672.93KiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "22.3%",
        "filesize": "569.83KiB",
        "speed": "739.49KiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "44.8%",
        "filesize": "569.83KiB",
        "speed": "859.19KiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "89.7%",
        "filesize": "569.83KiB",
        "speed": "884.08KiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "100.0%",
        "filesize": "569.83KiB",
        "speed": "810.46KiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "speed": "",
        "eta": "",
        "percent": "100%",
        "filesize": "569.83KiB",
    },
    {
        "status": "Post Processing",
        "path": "",
        "filename": "Among Us Momentos Divertidos-among-us-momentos-divertidos-2020-09-24-18-28-12-525257",
        "extension": ".mp4",
    },
    {},
    {},
]
OUTPUT_PLAYLIST_EXPECTED = [
    {"status": "Pre Processing"},
    {"status": "Pre Processing"},
    {"status": "Downloading"},
    {"status": "Pre Processing"},
    {"status": "Pre Processing"},
    {"status": "Pre Processing"},
    {"status": "Pre Processing"},
    {"status": "Pre Processing"},
    {"status": "Downloading", "playlist_index": "1", "playlist_size": "3"},
    {"status": "Pre Processing"},
    {"status": "Pre Processing"},
    {
        "status": "Downloading",
        "path": "",
        "filename": "USO EFICIENTE DE DATOS-uso-eficiente-datos-2021-04-21-08-42-41-766550.f2",
        "extension": ".mp4",
    },
    {
        "status": "Downloading",
        "percent": "0.0%",
        "filesize": "2.62MiB",
        "speed": "64.07KiB/s",
        "eta": "00:41",
    },
    {
        "status": "Downloading",
        "percent": "0.1%",
        "filesize": "2.62MiB",
        "speed": "192.20KiB/s",
        "eta": "00:13",
    },
    {
        "status": "Downloading",
        "percent": "0.3%",
        "filesize": "2.62MiB",
        "speed": "448.46KiB/s",
        "eta": "00:05",
    },
    {
        "status": "Downloading",
        "percent": "0.6%",
        "filesize": "2.62MiB",
        "speed": "960.98KiB/s",
        "eta": "00:02",
    },
    {
        "status": "Downloading",
        "percent": "1.2%",
        "filesize": "2.62MiB",
        "speed": "1.94MiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "2.4%",
        "filesize": "2.62MiB",
        "speed": "672.02KiB/s",
        "eta": "00:03",
    },
    {
        "status": "Downloading",
        "percent": "4.7%",
        "filesize": "2.62MiB",
        "speed": "739.22KiB/s",
        "eta": "00:03",
    },
    {
        "status": "Downloading",
        "percent": "9.5%",
        "filesize": "2.62MiB",
        "speed": "1.06MiB/s",
        "eta": "00:02",
    },
    {
        "status": "Downloading",
        "percent": "19.1%",
        "filesize": "2.62MiB",
        "speed": "1.39MiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "38.2%",
        "filesize": "2.62MiB",
        "speed": "1.73MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "76.4%",
        "filesize": "2.62MiB",
        "speed": "2.13MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "100.0%",
        "filesize": "2.62MiB",
        "speed": "2.46MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "speed": "",
        "eta": "",
        "percent": "100%",
        "filesize": "2.62MiB",
    },
    {
        "status": "Downloading",
        "path": "",
        "filename": "USO EFICIENTE DE DATOS-uso-eficiente-datos-2021-04-21-08-42-41-766550.f5",
        "extension": ".m4a",
    },
    {
        "status": "Downloading",
        "percent": "0.1%",
        "filesize": "1.28MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.2%",
        "filesize": "1.28MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.5%",
        "filesize": "1.28MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "1.1%",
        "filesize": "1.28MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "2.4%",
        "filesize": "1.28MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "4.8%",
        "filesize": "1.28MiB",
        "speed": "807.38KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "9.7%",
        "filesize": "1.28MiB",
        "speed": "813.19KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "19.4%",
        "filesize": "1.28MiB",
        "speed": "1020.19KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "38.9%",
        "filesize": "1.28MiB",
        "speed": "991.25KiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "77.8%",
        "filesize": "1.28MiB",
        "speed": "1.52MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "100.0%",
        "filesize": "1.28MiB",
        "speed": "1.79MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "speed": "",
        "eta": "",
        "percent": "100%",
        "filesize": "1.28MiB",
    },
    {
        "status": "Post Processing",
        "path": "",
        "filename": "USO EFICIENTE DE DATOS-uso-eficiente-datos-2021-04-21-08-42-41-766550",
        "extension": ".mp4",
    },
    {},
    {},
    {"status": "Downloading", "playlist_index": "2", "playlist_size": "3"},
    {"status": "Pre Processing"},
    {"status": "Pre Processing"},
    {
        "status": "Downloading",
        "path": "",
        "filename": "VIDEOTUTORIAL APKLIS-videotutorial-apklis-2021-04-21-08-32-02-115958.f2",
        "extension": ".mp4",
    },
    {
        "status": "Downloading",
        "percent": "0.0%",
        "filesize": "3.51MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.1%",
        "filesize": "3.51MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.2%",
        "filesize": "3.51MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.4%",
        "filesize": "3.51MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.9%",
        "filesize": "3.51MiB",
        "speed": "1.94MiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "1.8%",
        "filesize": "3.51MiB",
        "speed": "671.81KiB/s",
        "eta": "00:05",
    },
    {
        "status": "Downloading",
        "percent": "3.5%",
        "filesize": "3.51MiB",
        "speed": "738.85KiB/s",
        "eta": "00:04",
    },
    {
        "status": "Downloading",
        "percent": "7.1%",
        "filesize": "3.51MiB",
        "speed": "960.07KiB/s",
        "eta": "00:03",
    },
    {
        "status": "Downloading",
        "percent": "14.2%",
        "filesize": "3.51MiB",
        "speed": "1.33MiB/s",
        "eta": "00:02",
    },
    {
        "status": "Downloading",
        "percent": "28.4%",
        "filesize": "3.51MiB",
        "speed": "1.64MiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "56.9%",
        "filesize": "3.51MiB",
        "speed": "1.85MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "100.0%",
        "filesize": "3.51MiB",
        "speed": "1.74MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "speed": "",
        "eta": "",
        "percent": "100%",
        "filesize": "3.51MiB",
    },
    {
        "status": "Downloading",
        "path": "",
        "filename": "VIDEOTUTORIAL APKLIS-videotutorial-apklis-2021-04-21-08-32-02-115958.f5",
        "extension": ".m4a",
    },
    {
        "status": "Downloading",
        "percent": "0.1%",
        "filesize": "1.57MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.2%",
        "filesize": "1.57MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.4%",
        "filesize": "1.57MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.9%",
        "filesize": "1.57MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "1.9%",
        "filesize": "1.57MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "3.9%",
        "filesize": "1.57MiB",
        "speed": "1008.08KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "7.9%",
        "filesize": "1.57MiB",
        "speed": "812.77KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "15.9%",
        "filesize": "1.57MiB",
        "speed": "1020.26KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "31.8%",
        "filesize": "1.57MiB",
        "speed": "1.23MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "63.6%",
        "filesize": "1.57MiB",
        "speed": "1.78MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "100.0%",
        "filesize": "1.57MiB",
        "speed": "2.39MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "speed": "",
        "eta": "",
        "percent": "100%",
        "filesize": "1.57MiB",
    },
    {
        "status": "Post Processing",
        "path": "",
        "filename": "VIDEOTUTORIAL APKLIS-videotutorial-apklis-2021-04-21-08-32-02-115958",
        "extension": ".mp4",
    },
    {},
    {},
    {"status": "Downloading", "playlist_index": "3", "playlist_size": "3"},
    {"status": "Pre Processing"},
    {"status": "Pre Processing"},
    {
        "status": "Downloading",
        "path": "",
        "filename": "ENRED2 CORTAFUEGOS WIFI-enred2-cortafuegos-wifi-2021-04-14-09-49-03-477520.f2",
        "extension": ".mp4",
    },
    {
        "status": "Downloading",
        "percent": "0.0%",
        "filesize": "2.40MiB",
        "speed": "32.08KiB/s",
        "eta": "01:16",
    },
    {
        "status": "Downloading",
        "percent": "0.1%",
        "filesize": "2.40MiB",
        "speed": "96.24KiB/s",
        "eta": "00:25",
    },
    {
        "status": "Downloading",
        "percent": "0.3%",
        "filesize": "2.40MiB",
        "speed": "224.56KiB/s",
        "eta": "00:10",
    },
    {
        "status": "Downloading",
        "percent": "0.6%",
        "filesize": "2.40MiB",
        "speed": "481.20KiB/s",
        "eta": "00:05",
    },
    {
        "status": "Downloading",
        "percent": "1.3%",
        "filesize": "2.40MiB",
        "speed": "661.86KiB/s",
        "eta": "00:03",
    },
    {
        "status": "Downloading",
        "percent": "2.6%",
        "filesize": "2.40MiB",
        "speed": "672.30KiB/s",
        "eta": "00:03",
    },
    {
        "status": "Downloading",
        "percent": "5.2%",
        "filesize": "2.40MiB",
        "speed": "625.53KiB/s",
        "eta": "00:03",
    },
    {
        "status": "Downloading",
        "percent": "10.4%",
        "filesize": "2.40MiB",
        "speed": "709.79KiB/s",
        "eta": "00:03",
    },
    {
        "status": "Downloading",
        "percent": "20.8%",
        "filesize": "2.40MiB",
        "speed": "1.10MiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "41.6%",
        "filesize": "2.40MiB",
        "speed": "1.45MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "83.3%",
        "filesize": "2.40MiB",
        "speed": "1.58MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "100.0%",
        "filesize": "2.40MiB",
        "speed": "1.71MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "speed": "",
        "eta": "",
        "percent": "100%",
        "filesize": "2.40MiB",
    },
    {
        "status": "Downloading",
        "path": "",
        "filename": "ENRED2 CORTAFUEGOS WIFI-enred2-cortafuegos-wifi-2021-04-14-09-49-03-477520.f5",
        "extension": ".m4a",
    },
    {
        "status": "Downloading",
        "percent": "0.1%",
        "filesize": "1.29MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.2%",
        "filesize": "1.29MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "0.5%",
        "filesize": "1.29MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "1.1%",
        "filesize": "1.29MiB",
        "speed": "Unknown",
        "eta": "ETA",
    },
    {
        "status": "Downloading",
        "percent": "2.3%",
        "filesize": "1.29MiB",
        "speed": "1.95MiB/s",
        "eta": "00:00",
    },
    {
        "status": "Downloading",
        "percent": "4.8%",
        "filesize": "1.29MiB",
        "speed": "672.94KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "9.6%",
        "filesize": "1.29MiB",
        "speed": "739.59KiB/s",
        "eta": "00:01",
    },
    {
        "status": "Downloading",
        "percent": "19.2%",
        "filesize": "1.29MiB",
        "speed": "1020.62KiB/s",
        "eta": "00:01",
    },
]


class TestDownloaders(unittest.TestCase):
    def setUp(self) -> None:
        self.expected_output = {
            "video": OUTPUT_VIDEO_EXPECTED,
            "playlist": OUTPUT_PLAYLIST_EXPECTED,
        }

    def process_data(self, output: str, expected: str) -> None:
        lines = [line for line in output.splitlines() if line]

        STEPS = int(len(lines) / 10)

        for step in range(STEPS):
            for num, line in enumerate(lines[step * 10 : (step + 1) * 10]):
                data = downloaders.extract_data(line)
                # print(data)
                self.assertDictEqual(
                    self.expected_output[expected][num + (step * 10)], data
                )

    def test_extract_data_video(self):
        self.process_data(YOUTUBEDL_OUTPUT_VIDEO, "video")

    def test_extract_data_playlist(self):
        self.process_data(YOUTUBEDL_OUTPUT_PLAYLIST, "playlist")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
