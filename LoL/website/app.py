from flask import Flask, render_template
# library imp

app = Flask(__name__)
# app instance

@app.route('/')
def home():
    return render_template("temple.html")



if __name__ == '__main__':
    app.run(debug=True)
