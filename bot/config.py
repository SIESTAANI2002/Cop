#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", default=15681388, cast=int)
    API_HASH = config("API_HASH", default="446b56944f74f6b7688175d48cdfa881")
    BOT_TOKEN = "5419649199:AAH3qRlGtk3kEHFeYPm8WdUPfDgSK73w7So"
    DEV = 5074446156
    OWNER = config("OWNER", default="5074446156")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i '''{}''' -map 0:v? -map 0:a? -map 0:s? -map 0:t?  -vf scale=1280:720,"drawtext=fontfile=/content/drive/MyDrive/Font/A.ttf:text=Encoded By @Ani_Animesh:x=1040:y=650:fontsize=8:fontcolor=white:enable=between(t\,0\,240)" -c:v libx265 -pix_fmt yuv420p10le -preset medium -x265-params frame-threads=4:bframes=8:psy-rd=1:aq-mode=3:aq-strength=0.8:deblock=1,1 -s 1280x720 -crf 22.2 -c:a aac -b:a 112k -c:s copy  -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Anime Sakura" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="AnimeSakura.co" -metadata:s:s:0 title="AnimeSakura.co" -metadata:s:s:1 title="@Ani_Animesh" '''{}''''
    )
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
