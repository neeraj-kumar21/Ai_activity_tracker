import json
import os


CONFIG_FILE = "settings.json"


DEFAULT_SETTINGS = {
    "appearance": "dark",
    "accent_color": "blue",
    "report_interval_hours": 8,
    "auto_refresh": True,
    "report_folder": "reports",
    "tracker_enabled": True
}


def load_settings():

    if not os.path.exists(CONFIG_FILE):
        save_settings(DEFAULT_SETTINGS.copy())
        return DEFAULT_SETTINGS.copy()

    try:

        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            settings = json.load(file)

        # Missing settings ko default se fill karo
        for key, value in DEFAULT_SETTINGS.items():

            if key not in settings:
                settings[key] = value

        return settings

    except Exception as error:

        print("Could not load settings:", error)

        return DEFAULT_SETTINGS.copy()


def save_settings(settings):

    with open(
        CONFIG_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            settings,
            file,
            indent=4
        )


def get_setting(key):

    settings = load_settings()

    return settings.get(
        key,
        DEFAULT_SETTINGS.get(key)
    )


def update_setting(key, value):

    settings = load_settings()

    settings[key] = value

    save_settings(settings)