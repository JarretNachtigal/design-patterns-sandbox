# "When you receive an event, you have to be careful not to assume the current state of the world
# reflects how the world was when the event was raised. This means queued events tend to be more data heavy
# than events in synchronous systems. With the latter, the notification can say “something happened” and
# the receiver can look around for the details. "

# "All event and message systems have to worry about cycles:
# - A sends an event.
# - B receives it and responds by sending an event.
# - That event happens to be one that A cares about, so it receives it. In response, it sends an event…
# - Go to 2."
