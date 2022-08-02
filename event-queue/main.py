# "When you receive an event, you have to be careful not to assume the current state of the world
# reflects how the world was when the event was raised. This means queued events tend to be more data heavy
# than events in synchronous systems. With the latter, the notification can say “something happened” and
# the receiver can look around for the details. "
