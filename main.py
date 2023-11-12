import auth
from processor import processor
sp = auth.auth()
proc_object = processor(spotipy_auth=sp)

print(f"hello, {proc_object.get_display_name()}")

while(1):
    inp = input("spotify-cli>")
    print(proc_object.adjust_volume(adj=inp))
    