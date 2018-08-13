# Twitch Live Conky / polybar

This should only be used when using conky or polybar.

# Polybar

For polybar you are going to have edit and comment lines 13 -15 and uncomment line 16

```
[module/TwitchLive]
type = custom/script
interval = 3
format = <label>
exec = python /path/to/twitchlive/script
format-underline = #9575CD

```

# Conky

I haven't tested on conky yet...

# Why?

Because when I stream I want to know how many viewers are currently watching. Oh and have it popup on my bar when I go live
but it doesn't show up when I don't stream.


# Know bug

Error's when user runs the script without internet.


# Requirments
- python-twitch-client
- Python 3.7