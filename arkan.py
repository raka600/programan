from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    html = """
    <style type="text/css">
    h1 {
	color: Gray;
    }
    h3{
       color: Red;
       }
    p{
      color: Red;
      }
    </style>
    <center><h1><b>CHAPTER 2 PYHTON OBJECT ORIENTED PROGRAMMING</b></h1></center> 
    <center><h3><b>Hello Guys, selamat datang di flask<br>
    Perkenalan saya rakasona, dari kelas D4 Teknik Informatika 2C</b></h3></center>
    <p align="center"><b>Terima kasih banyak !</b></p>
    """
    return html

app.run()