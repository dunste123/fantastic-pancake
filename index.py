from pypresence import Presence
import time

# https://qwertyquerty.github.io/pypresence/

client_id = '679394558232231947'

RPC = Presence(client_id)  # Initialize the Presence client

RPC.connect()  # Start the handshake loop

start_time = time.time()  # The start time in seconds, maybe like the time of the day (epoch second)

RPC.update(
    details="Current Route",
    state="Hiro Akiba",

    start=start_time,

    large_image="hiro",
    large_text="Day whatever",

    small_image="logo",
    small_text="This is a badly cropped logo",

    instance=True
)  # Updates our presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15)  # Can only update rich presence every 15 seconds
