from datetime import datetime, timedelta
import requests
import os
import subprocess
from git import Repo


def get_sunrise_and_sunset_time(key, latitude, longitude):
    resp = requests.get(
        f"https://api.caiyunapp.com/v2.5/{key}/{latitude},{longitude}/weather.json?lang=zh_CN&granu=daily&fields=astro"
    )
    resp_json = resp.json()
    astro = resp_json.get("result", {}).get("daily", {}).get("astro", [])
    if astro:
        sunrise = astro[0].get("sunrise", {}).get("time")
        sunset = astro[0].get("sunset", {}).get("time")
    return sunrise, sunset


def update_lark_status(cookie, content):
    headers = {"cookie": cookie}
    json_data = {"descriptionType": 0, "description": content}
    return requests.put(
        "https://internal-api-lark-api.feishu.cn/passport/users/details/",
        headers=headers,
        json=json_data,
    )


def get_screeshot(stream_url, output_folder, filename):
    output_filename = f"{filename}"
    r = subprocess.run(
        [
            "ffmpeg",
            "-i",
            f"{stream_url}",
            "-y",
            "-frames:v",
            "1",
            f"{output_folder}/{output_filename}",
            "-hide_banner",
        ]
    )
    return f"{output_folder}/{output_filename}"


def update_screenshot(filepath):
    repo = Repo(f"{os.getcwd()}")
    g = repo.git
    g.add(filepath)
    g.commit(f"-m data: upload {filepath}")
    g.push()


def main():
    latitude = os.getenv("latitude")
    longitude = os.getenv("longitude")
    cookie = os.getenv("cookie")
    api_key = os.getenv("api_key")
    stream_url = os.getenv("stream_url")

    sunrise, sunset = get_sunrise_and_sunset_time(api_key, latitude, longitude)

    now = datetime.utcnow() + timedelta(hours=8)
    now_str = now.strftime("%H:%M")
    now_str_with_date = now.strftime("%Y%m%d%H%M")

    content = ""
    if now_str == sunrise:
        screenshot_path = get_screeshot(stream_url, "data", f"{now_str_with_date}.jpg")
        update_screenshot(screenshot_path)
        content = f"太阳在{now_str}升起了: https://raw.githubusercontent.com/simpleapples/sunrise-and-sunset/master/data/{now_str_with_date}.jpg"
    elif now_str == sunset:
        screenshot_path = get_screeshot(stream_url, "data", f"{now_str_with_date}.jpg")
        update_screenshot(screenshot_path)
        content = f"太阳在{now_str}落下了: https://raw.githubusercontent.com/simpleapples/sunrise-and-sunset/master/data/{now_str_with_date}.jpg"

    if content:
        update_lark_status(cookie, content)

    print(content, now_str, sunrise, sunset)


if __name__ == "__main__":
    main()
