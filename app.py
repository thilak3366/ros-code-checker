from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        request.files["file"].save("uploaded.zip")
        subprocess.run(["python3","checker.py"])
        return open("report.txt").read()
    return """
    <h2>ROS Code Checker</h2>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit">
    </form>
    <br>
    <a href="/sim">Run Simulation</a>
    """

@app.route("/sim")
def sim():
    subprocess.run(["python3","sim.py"])
    return "Simulation completed. Check screenshots folder."

app.run()
