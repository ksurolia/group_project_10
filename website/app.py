from flask import Flask, render_template
import pathlib
import sqlite3

base_path = pathlib.Path(r'C:\Users\Khyati\OneDrive\Desktop\Project_group_10\database')
db_name = "automobile.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    lst = cursor.execute("SELECT * FROM auto_parts limit 40").fetchall()
    con.close()

    # for title
    column_headers = ['index', 'highway-mpg', 'compression-ratio', 'fuel-system', 'engine-size',
       'engine-type', 'curb-weight', 'height', 'width', 'length',
       'drive-wheels', 'body-style', 'aspiration', 'fuel-type', 'make']
    
    return render_template("data.html", column=column_headers, automobile_features=lst)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)