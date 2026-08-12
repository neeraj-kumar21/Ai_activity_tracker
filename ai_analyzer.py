from database import get_all_activity

# =============================================
#  Productvutiy categories 
# =============================================

PRODUCTIVE_APPS = [
    "visual studio code",
    "vs code",
    "github",
    "pycharm",
    "terminal",
    "powershell",
    "command prompt",
    "stackoverflow",
    "chatgpt"
]

DISTRACTING_APPS =[
    "youtube",
    "instagram",
    "facebook",
    "twitter",
    "netflix",
    "prime video",
    "reddit"
]


# ============= Classify Activity 


def classify_activity(window_title):
    title =  window_title.lower()
    for app in PRODUCTIVE_APPS:

        if app in title:
            return "productive"
    for app in DISTRACTING_APPS:

        if app in title:
            return "distracting"

    return "neutral"

# ========== Convert Duration to Second 

def duration_to_seconds(duration):

    try:

        parts = str(duration).split(":")

        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = float(parts[2])

        return(
            hours * 3600
            + minutes * 60
            + seconds
        )

    except Exception:

        return 0

    
# ==============  Analyze Activity 

def analyze_activity():

    activities = get_all_activity()

    productive_seconds = 0 
    distracting_seconds = 0
    neutral_seconds = 0

    app_usage = {}

    for activity in activities:

        window_title = activity[4]
        duration = activity[3]

        seconds = duration_to_seconds(duration)

        category = classify_activity(window_title)


        # Category totals

        if category == "productive":

            productive_seconds += seconds

        elif category == "distracting":

            distracting_seconds += seconds

        else:

            neutral_seconds += seconds


        # Application usage

        if window_title not in app_usage:

            app_usage[window_title] = 0

        app_usage[window_title] += seconds


    total_seconds = (
        productive_seconds
        + distracting_seconds
        + neutral_seconds
    )


    # Productivity score

    if total_seconds > 0:

        productivity_score = (
            productive_seconds / total_seconds
        ) * 100

    else:

        productivity_score = 0


    # Most used application

    if app_usage:

        top_app = max(
            app_usage,
            key=app_usage.get
        )

    else:

        top_app = "None"


    return {

        "total_seconds": total_seconds,

        "productive_seconds": productive_seconds,

        "distracting_seconds": distracting_seconds,

        "neutral_seconds": neutral_seconds,

        "productivity_score": round(
            productivity_score,
            1
        ),

        "top_app": top_app,

        "app_usage": app_usage
    }


# ==============================
# Format Seconds
# ==============================

def format_duration(seconds):

    seconds = int(seconds)

    hours = seconds // 3600

    minutes = (seconds % 3600) // 60

    remaining_seconds = seconds % 60


    if hours > 0:

        return f"{hours}h {minutes}m"

    elif minutes > 0:

        return f"{minutes}m {remaining_seconds}s"

    else:

        return f"{remaining_seconds}s"


# ==============================
# Generate AI Insight
# ==============================

def generate_insight():

    data = analyze_activity()

    score = data["productivity_score"]

    productive = format_duration(
        data["productive_seconds"]
    )

    distracting = format_duration(
        data["distracting_seconds"]
    )

    top_app = data["top_app"]


    if score >= 80:

        message = (
            f"Excellent productivity! "
            f"You spent {productive} on productive activities."
        )

    elif score >= 60:

        message = (
            f"Good productivity. "
            f"You spent {productive} productively, "
            f"but {distracting} was spent on distracting activities."
        )

    else:

        message = (
            f"Your productivity can be improved. "
            f"You spent {distracting} on distracting activities."
        )


    return {

        "score": score,

        "productive_time": productive,

        "distracting_time": distracting,

        "top_app": top_app,

        "message": message
    }

   
