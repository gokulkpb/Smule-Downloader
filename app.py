from flask import Flask
from flask.templating import render_template
from flask import request
from justgood import imjustgood

app = Flask(__name__, template_folder='templates')
@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('index.html')

@app.route('/smule', methods=['POST', 'GET'])
def smule():
    print("----Gokul Balachandran")
    if request.method == 'POST':
        url = request.form['URL']
        media = imjustgood("imjustgood")
        data = media.smuledl(url)
        
        result = "Gokul's Smule Downloader"
        result += "\n\nTitle : {}".format(data["result"]["title"])
        result += "\nType : {}".format(data["result"]["type"])
        if data["result"]["type"] == "video":
            result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
            result += "\n\nVideo URL : {}".format(data["result"]["mp4Url"])
        our_url = data["result"]["mp3Url"]
        result += "\n\nAudio URL : {}".format(data["result"]["mp3Url"])
        return render_template('smule.html', result=result, our_url=our_url)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
