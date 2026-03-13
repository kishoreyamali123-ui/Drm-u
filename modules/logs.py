import logging
import sys
import traceback

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("BOT")


def log(msg):
    logger.info(msg)


def log_error(e):
    logger.error(f"ERROR: {e}")
    traceback.print_exc()


def log_txt_upload(user_id, file_name):
    logger.info(f"TXT UPLOADED | user={user_id} | file={file_name}")


def log_links_parsed(total):
    logger.info(f"LINKS PARSED | total_links={total}")


def log_platform(url):
    platform = "UNKNOWN"

    if "youtu" in url:
        platform = "YOUTUBE"
    elif "classplus" in url:
        platform = "CLASSPLUS"
    elif "m3u8" in url:
        platform = "M3U8 STREAM"
    elif "mpd" in url:
        platform = "DRM MPD"
    elif url.endswith(".pdf"):
        platform = "PDF"
    elif url.endswith(".zip"):
        platform = "ZIP"
    elif url.endswith((".jpg",".png",".jpeg")):
        platform = "IMAGE"

    logger.info(f"PLATFORM DETECTED | {platform} | {url}")


def log_download_start(index,total,url):
    logger.info(f"DOWNLOAD START | {index}/{total} | {url}")


def log_download_done(file):
    logger.info(f"DOWNLOAD COMPLETE | {file}")


def log_upload_start(file):
    logger.info(f"UPLOAD START | {file}")


def log_upload_done(file):
    logger.info(f"UPLOAD COMPLETE | {file}")


def log_api(url):
    logger.info(f"API CALL | {url}")


def log_token(name,token):
    if token:
        masked = token[:4] + "***" + token[-4:]
    else:
        masked = "None"

    logger.info(f"TOKEN USED | {name}={masked}")
