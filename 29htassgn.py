from flask import Flask, render_template,request
import pandas as pd

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    df = pd.read_csv('F:\TATTVALABS\iris.csv')

    s1=request.form.get('val1',type=float)
    s2=request.form.get('val2',type=float)
    s3=request.form.get('val3',type=float)
    s4=request.form.get('val4',type=float)

    if s1 < 4.3 or s1 > 7.9:
        return("the value for sepal length is invalid")
    if s2 < 2.0 or s2 > 4.4:
        return("the value for sepal width is invalid")
    if s3 < 1.0 or s3 > 6.9:
        return("the value for petal length is invalid")
    if s4 < 0.1 or s4 > 2.5:
        return("the value for petal width is invalid")
    if (s1 >= 4.3 and s1 <= 5.8) and (s2 >= 2.3 and s2 <= 4.4) and (s3 >= 1.0 and s3 <= 1.9) and (
            s4 >= 0.1 and s4 <= 0.6):
        return("the species is setosa")
    elif (s1 >= 4.9 and s1 <= 7.0) and (s2 >= 2.0 and s2 <= 3.4) and (s3 >= 3.0 and s3 <= 5.1) and (
            s4 >= 1.0 and s4 <= 1.8):
        return("the species is versicolor")
    elif (s1 >= 4.9 and s1 <= 7.9) and (s2 >= 2.2 and s2 <= 3.8) and (s3 >= 4.5 and s3 <= 6.9) and (
            s4 >= 1.4 and s4 <= 2.5):
        return("the species is verginica")
    else:
        return("does not belong to any species")








if __name__=="__main__":
    app.run()




<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">`

    <title>Iris</title>

</head>

<body>

<image src="http://2.bp.blogspot.com/_fP1y4T5-DFE/TU7qH9V6YrI/AAAAAAAAFVc/JrboGJ7uras/s1600/iris-flower-658-6.jpg"></image>

<form name="myform"   method="post" >

            <div style="position:absolute;top:5%;left:10%; color:yellow;">

SEPAL-LENGTH:<p><input type="text" name="val1" id="val1" style="font-size:18pt;height=35px;width=200px;"></p>

SEPAL-WIDTH:<p><input type="text" name="val2" id="val2" style="font-size:18pt;height=35px;width=200px;"></p>

PETAL-LENGTH:<p><input type="text"name="val3" id="val3" style="font-size:18pt;height=35px;width=200px;"></p>

PETAL-WIDTH:<p><input type="text"name="val4" id="val4" style="font-size:18pt;height=35px;width=200px;"></p>

            </div>

          <div style="position:absolute; bottom:40%;left:15%; font-size:80pt;">

        <input type="submit" formaction="/submit" name="submit" id="submit" value="SUBMIT">

            </div>





</body>

</html>

