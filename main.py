from flask import Flask, render_template, redirect, url_for, request
import requests
import json


app = Flask(__name__)

@app.route("/stats",methods=["POST","GET"]) #flask to make a page of /stats
def stats():
    if request.method == "POST":    #allow the page to post input from an input box to backend
        user_name= request.form["nm"]
        
        url = "https://api.scrims.network/v1/user?username="+ user_name
        response = requests.get(url)
        jData = json.loads(response.content)  #puts all the response to jData

        if jData["user_data"]:
            return render_template("stats.html",User_name=user_name,User_info=jData) #build a dynamic page
        else:
            return render_template("stats.html", User_name="Cannot find this user",User_info="")
    else:
        return render_template("stats.html",  User_name="Please input user name in box above, this site is still in development. Please report any bugs to @beavermon on Discord. 2v2 Casual stats will be added soon. I know the links look ugly, deal with it.",User_info="")
    

if __name__== "__main__":
    app.run()


