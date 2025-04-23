from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    if request.method == "POST":
        width = request.form.get("width")
        height = request.form.get("height")
        if width and height:
            image_url = f"https://picsum.photos/{width}/{height}"
    return render_template("index.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
