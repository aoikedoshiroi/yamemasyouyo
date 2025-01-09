from flask import Flask, request, jsonify
import gradio as gr
from gradio.routes import App

# Flaskアプリの作成
app = Flask(__name__)

# Gradioインターフェースの定義
def reverse_text(text):
    return text[::-1]

gr_interface = gr.Interface(fn=reverse_text, inputs="text", outputs="text")

# GradioをFlaskアプリのルート "/gradio" に統合
gr_app = App.create_app(gr_interface)
app.wsgi_app = gr_app

# APIエンドポイントの作成
@app.route("/api/reverse", methods=["POST"])
def reverse_api():
    data = request.json.get("text", "")
    result = reverse_text(data)
    return jsonify({"reversed_text": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
