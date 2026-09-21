from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

images = [
    "images/螢幕擷取畫面 2026-09-09 165601.png",
    "images/螢幕擷取畫面 2026-09-10 073117.png",
    "images/螢幕擷取畫面 2026-09-10 073855.png"
]

current_index = 0


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="數學公式圖庫",
        image=images[current_index],
        idx=current_index,
        total=len(images)
    )


@app.route("/next")
def next_img():
    global current_index

    # 到最後一張後，回到第一張
    current_index = (current_index + 1) % len(images)

    return redirect(url_for("index"))


@app.route("/prev")
def prev_img():
    global current_index

    # 在第一張按上一張時，跳到最後一張
    current_index = (current_index - 1) % len(images)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)