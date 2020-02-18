#  This is free and unencumbered software released into the public domain.
#
#  Anyone is free to copy, modify, publish, use, compile, sell, or
#  distribute this software, either in source code form or as a compiled
#  binary, for any purpose, commercial or non-commercial, and by any
#  means.
#
#  In jurisdictions that recognize copyright laws, the author or authors
#  of this software dedicate any and all copyright interest in the
#  software to the public domain. We make this dedication for the benefit
#  of the public at large and to the detriment of our heirs and
#  successors. We intend this dedication to be an overt act of
#  relinquishment in perpetuity of all present and future rights to this
#  software under copyright law.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#  OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#  OTHER DEALINGS IN THE SOFTWARE.
#
#  For more information, please refer to <https://unlicense.org>

from pypresence import Presence
import time

client_id = '679394558232231947'

RPC = Presence(client_id)  # Initialize the Presence client

RPC.connect()  # Start the handshake loop

# start_time = time.time()  # The start time in seconds, maybe like the time of the day (epoch second)

start_time = 1582054003  # static start time

RPC.update(
    details="Current Route",
    state="Hiro Akiba",

    start=start_time,

    large_image="hiro",
    large_text="Day 30",

    small_image="logo",
    small_text="This is a badly cropped logo",

    instance=True
)

# RPC.update(
#     details="Current Route",
#     state="Not known yet",
#
#     start=start_time,
#
#     large_image="campers",
#     large_text="Day 3",
#
#     small_image="logo",
#     small_text="Highest score: Hiro Akiba",
#
#     instance=True
# )

# RPC.update(
#     details="Main menu",
#
#     large_image="logo",
#     large_text="Day 30",
#
#     instance=True
# )

while True:  # The presence will stay on as long as the program is running
    time.sleep(15)  # Can only update rich presence every 15 seconds
