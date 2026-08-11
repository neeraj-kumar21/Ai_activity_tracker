from flask import Flask, request, jsonify
from database import save_browser_activity

app = Flask(__name__)


@app.route("/browser-activity", methods=["POST"])
def browser_activity():

    data = request.get_json()

    title = data.get("title")
    url = data.get("url")

    print("\n===== Browser Activity =====")
    print("Title:", data.get("title"))
    print("URL:", data.get("url"))
    print("============================\n")


    save_browser_activity(title ,url)

    return jsonify({
        "status": "success"
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1", 
        port=5000, 
        debug=False
    )
