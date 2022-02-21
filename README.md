Sunrise and Sunset
===

A automatic script to take screenshot of every sunset and sunset from a live stream and publish them to your lark status.

# Prepare

## 1. Install ffmpeg

Follow the instruction on [Official Website](https://ffmpeg.org/download.html)

## 2. Install Python dependencies

```bash
pip install -r src/requirements.txt
```

## 3. Add a crontab task

The task should be run every minute. Change the path of Python Interpreter and main file on command below if you use a virtual environment.

```bash
* * * * * export cookie=xxxx && export longitude=xxxx && export latitude=xxxx && export api_key=xxxx && export stream_url=xxxx && python main.py
```
