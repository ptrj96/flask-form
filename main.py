from flask import Flask, render_template, request

app = Flask(__name__, template_folder="template")

@app.route("/test/", methods=["post", "get"])
def form():
    
    message = ""

    if request.method == "POST":
        message = request.form.get("message")
        option = request.form.get("voice")

        print(message)
        print(option)

    return render_template("test.html", message=message)


if __name__ == "__main__":
    app.run()