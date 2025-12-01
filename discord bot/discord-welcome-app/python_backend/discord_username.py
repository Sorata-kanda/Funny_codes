import sys
import pytesseract
import pyautogui
import re
import pyperclip
import os
import time
import threading
import keyboard  # keyboard must be re-imported
# from pynput import keyboard
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter
# from pynput import keyboard

# Force stdout to flush immediately so Electron can see logs
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

# ---- CONFIG -----
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

screenshot_folder = Path(r"D:\TimePass\discord bot\user_screenshots")
screenshot_folder.mkdir(parents=True, exist_ok=True)

MAX_SCREENSHOTS = 10
usernames = set()

should_exit = False

print("Bot Running...\n")
print("ALT + C -> Capture screen + extract usernames")
print("ALT + X -> Paste all usernames")
print("CTRL + SHIFT + Q -> Quit program\n")

def maintain_screenshot_limit():
    files = sorted(screenshot_folder.glob("*.png"), key=os.path.getmtime)

    if len(files) > MAX_SCREENSHOTS:
        remove_count = len(files) - MAX_SCREENSHOTS
        for i in range(remove_count):
            try:
                os.remove(files[i])
                print(f"[Screenshot Deleted] {files[i].name}")
            except:
                pass


# 💡 NEW improved username filtering
def is_valid_username(name: str):
    bad_keywords = [
        "supporter", "paimon", "app",
        "everyone", "design", "community",
        "pls", "welcome"
    ]

    low = name.lower()

    for bad in bad_keywords:
        if bad in low:
            return False

    if len(re.findall(r"[A-Za-z]", name)) < 2:
        return False

    if name.count(" ") > 2:
        return False

    if re.search(r"[^A-Za-z0-9_\- ]", name):
        return False

    if len(name.strip()) < 3:
        return False

    return True


def extract_usernames_from_text(text: str):
    found = set()

    mention_matches = re.findall(r'@([A-Za-z0-9_\- ]{2,25})\b', text)
    raw_is_here = re.findall(r'([A-Za-z0-9_\- ]{2,25}) is here\.', text)
    raw_everyone = re.findall(r'Everyone welcome ([A-Za-z0-9_\- ]{2,25})\!', text)
    raw_glad = re.findall(r"Glad you're here, ([A-Za-z0-9_\- ]{2,25})", text)

    candidates = set(mention_matches + raw_is_here + raw_everyone + raw_glad)

    for name in candidates:
        clean = name.strip()

        if is_valid_username(clean):
            found.add(clean)

    return found


def screenshot_and_extract():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    screenshot_path = screenshot_folder / f"screenshot_{timestamp}.png"

    raw = pyautogui.screenshot()
    raw.save(screenshot_path)
    maintain_screenshot_limit()

    print(f"[Saved] {screenshot_path}")

    W, H = raw.size

    crop_left = int(W * 0.20)
    crop_top = 120
    crop_right = W - 50
    crop_bottom = H - 180

    img = raw.crop((crop_left, crop_top, crop_right, crop_bottom))
    img = img.convert("L")

    zoom_factor = 1.4
    img = img.resize((int(img.width * zoom_factor), int(img.height * zoom_factor)), Image.LANCZOS)
    img = ImageEnhance.Contrast(img).enhance(1.7)
    img = ImageEnhance.Sharpness(img).enhance(1.3)

    text = pytesseract.image_to_string(img, config=r"-l eng --oem 3 --psm 6")

    new_users = extract_usernames_from_text(text)

    if not new_users:
        print("No usernames found.")
        return

    added = 0
    for u in new_users:
        if u not in usernames:
            usernames.add(u)
            added += 1
            print(f"[+] Added: {u}")

    print(f"Total stored: {len(usernames)}")


def paste_usernames():
    if not usernames:
        print("No usernames stored.")
        return

    sorted_names = sorted(usernames, key=lambda x: x.lower())
    out = " ".join(f"@{u}" for u in sorted_names)

    pyperclip.copy(out)
    time.sleep(0.1)  # Small delay before pasting
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.1)  # Small delay after pasting to let keyboard state reset

    print("[Pasted]")


# 🔥 GLOBAL HOTKEY LISTENER
# ------------------------------------------------------
# HOTKEYS (threaded + non-blocking)
# ------------------------------------------------------

should_exit = False

def quit_program():
    global should_exit
    print("Exiting...")
    should_exit = True

def threaded(func):
    """Runs function in background so hotkeys never freeze."""
    threading.Thread(target=func, daemon=True).start()

# These hotkeys will now ALWAYS work — even inside Discord
keyboard.add_hotkey("alt+c", lambda: threaded(screenshot_and_extract))
keyboard.add_hotkey("alt+x", lambda: threaded(paste_usernames))
keyboard.add_hotkey("ctrl+shift+q", quit_program)

print("Ready. (Press CTRL+SHIFT+Q to exit)\n")
while not should_exit:
    time.sleep(0.05)   # keeps script alive without blocking hotkeys
