import requests
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    temp=''
    weather=''
    min_temp=''
    max_temp=''
    icon=''
    city=''
    if request.method=='POST':
        city=request.form['city']
        url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=662e233665c5ca5286dd808dbfb2b455'
        resp=requests.get(url.format(city)).json()
        temp = resp['main']['temp']
        weather = resp['weather'][0]['description']
        min_temp = resp['main']['temp_min']
        max_temp = resp['main']['temp_max']
        icon = resp['weather'][0]['icon']
    return render_template('index.html',temp=temp,weather=weather,min_temp=min_temp,max_temp=max_temp,icon=icon,city=city)
    


if __name__=='__main__':
    app.run(debug=False)