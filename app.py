from flask import Flask, render_template, request, redirect, url_for
import numpy as np

ap = Flask(__name__)


def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね",
    ]

    return np.random.choice(messages)


txt = picked_up()
print(txt)
