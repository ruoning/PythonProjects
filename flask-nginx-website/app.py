from flask import Flask, request
from flask import render_template
import os


HTML_DIR = os.environ.get("HTML_DIR")
BASE_URL = os.environ.get("BASE_URL", "http://keyin.xiaoyanzhang.com")
HTML_DIR_INDEX = os.environ.get("HTML_DIR_INDEX", "story_html5.html")
WEBSITE_TITLE = os.environ.get("WEBSITE_TITLE", "学习官网")

app = Flask(__name__)


def get_sub_dir(dir=HTML_DIR):
    """get sub dir"""
    sub_dirs = os.listdir(dir)
    return sub_dirs


@app.route('/f/index', methods=["GET"])
def index():
    dirs = get_sub_dir()
    websites = {}
    pp = request.args.get("pp")
    for dir in dirs:
        websites[dir] = "%s/%s/%s" % (BASE_URL, dir, HTML_DIR_INDEX)
    return render_template('index.html', websites=websites, website_title=WEBSITE_TITLE)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)