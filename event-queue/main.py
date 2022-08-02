# "When you receive an event, you have to be careful not to assume the current state of the world
# reflects how the world was when the event was raised. This means queued events tend to be more data heavy
# than events in synchronous systems. With the latter, the notification can say “something happened” and
# the receiver can look around for the details. "

# "All event and message systems have to worry about cycles:
# - A sends an event.
# - B receives it and responds by sending an event.
# - That event happens to be one that A cares about, so it receives it. In response, it sends an event…
# - Go to 2."

# When your messaging system is synchronous, you find cycles quickly
#  — they overflow the stack and crash your game. With a queue, the asynchrony unwinds the stack,
# so the game may keep running even though spurious events are sloshing back and forth in there.
# A common rule to avoid this is to avoid sending events from within code that’s handling one.
