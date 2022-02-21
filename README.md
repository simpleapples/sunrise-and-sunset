Sunrise And Sunset
===

A automatic script to take screenshot of every sunset and sunset from a live stream and publish them to your lark status.

# Prepare

## 1. Install ffmpeg

Follow the instruction on [Official Website](https://ffmpeg.org/download.html)

## 2. Add a crontab task

The task should be run every minute.

```bash
* * * * * export cookie=xxxx && export longitude=xxxx && export latitude=xxxx && export api_key=xxxx && export stream_url=xxxx && /home/ubuntu/Documents/workspace/sunrise-and-sunset/venv/bin/python /home/ubuntu/Documents/workspace/sunrise-and-sunset/src/main.py >> /home/ubuntu/Documents/workspace/sunrise-and-sunset/run.log
```
