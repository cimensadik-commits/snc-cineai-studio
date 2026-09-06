from flask import Flask, render_template_string, jsonify, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SNÇ CineAI Studio</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin: 0; padding: 20px; font-family: sans-serif; background: #070b14; color: #fff; padding-bottom: 120px; display: flex; flex-direction: column; align-items: center; position: relative; min-height: 100vh; }
        #ambientLight {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            pointer-events: none; z-index: 1; transition: background 0.6s ease;
            background: radial-gradient(circle at 50% 35%, rgba(52, 211, 153, 0.25) 0%, transparent 75%);
        }
        .main-wrapper { width: 100%; max-width: 800px; position: relative; z-index: 2; }
        .card { background: #111827; padding: 25px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #1f2937; width: 100%; box-sizing: border-box; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        h3 { color: #34d399; margin-top: 0; font-size: 22px; text-align: center; letter-spacing: 1px; }
        button { background: #34d399; border: none; color: #070b14; padding: 14px 20px; font-weight: bold; border-radius: 6px; cursor: pointer; width: 100%; font-size: 16px; transition: all 0.2s; }
        button:hover { background: #10b981; transform: translateY(-1px); }
        input, select, textarea { width: 100%; padding: 12px; margin-top: 6px; margin-bottom: 18px; background: #0b0f19; border: 1px solid #374151; color: #fff; border-radius: 6px; box-sizing: border-box; font-size: 14px; }
        input:focus, select:focus, textarea:focus { border-color: #34d399; outline: none; box-shadow: 0 0 10px rgba(52, 211, 153, 0.3); }

        .daisy-section {
            background: linear-gradient(135deg, rgba(17,24,39,0.9), rgba(11,15,25,0.95));
            border: 2px solid #34d399;
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            margin-bottom: 25px;
            box-shadow: 0 20px 40px rgba(52, 211, 153, 0.2);
            width: 100%;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .daisy-container {
            position: relative;
            width: 260px;
            height: 260px;
            margin: 20px auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .petal {
            position: absolute;
            width: 46px;
            height: 95px;
            background: linear-gradient(to top, #ffffff, #a7f3d0);
            border-radius: 23px;
            top: calc(50% - 47.5px);
            left: calc(50% - 23px);
            box-shadow: 0 0 15px rgba(52, 211, 153, 0.4);
            opacity: 0.95;
            transition: transform 0.3s ease;
        }
        .petal:hover { transform: scale(1.05); }

        .p1 { transform: rotate(0deg) translateY(-65px); }
        .p2 { transform: rotate(45deg) translateY(-65px); }
        .p3 { transform: rotate(90deg) translateY(-65px); }
        .p4 { transform: rotate(135deg) translateY(-65px); }
        .p5 { transform: rotate(180deg) translateY(-65px); }
        .p6 { transform: rotate(225deg) translateY(-65px); }
        .p7 { transform: rotate(270deg) translateY(-65px); }
        .p8 { transform: rotate(315deg) translateY(-65px); }

        .daisy-core {
            position: absolute;
            width: 110px;
            height: 110px;
            background: radial-gradient(circle, #34d399 0%, #054f38 100%);
            border-radius: 50%;
            border: 4px solid #065f46;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            box-shadow: 0 0 30px rgba(52, 211, 153, 0.7);
        }
        .core-text {
            color: #070b14;
            font-weight: 900;
            font-size: 24px;
            letter-spacing: 2px;
            text-shadow: 0 1px 2px rgba(255,255,255,0.4);
        }
    </style>
</head>
<body>
    <div id="ambientLight"></div>
    <div class="main-wrapper">
        <div class="daisy-section">
            <h3>SNÇ CineAI Studio</h3>
            <div class="daisy-container">
                <div class="petal p1"></div>
                <div class="petal p2"></div>
                <div class="petal p3"></div>
                <div class="petal p4"></div>
                <div class="petal p5"></div>
                <div class="petal p6"></div>
                <div class="petal p7"></div>
                <div class="petal p8"></div>
                <div class="daisy-core">
                    <span class="core-text">SNÇ</span>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h3>Stüdyo Kontrol Paneli</h3>
            <p style="color: #9ca3af; text-align: center; margin-bottom: 20px;">Bulut altyapısı ve mobil APK paketlemesi için sistem hazır.</p>
            <button onclick="alert('SNÇ CineAI Studio bulut bağlantısı aktif!')">Sistemi Test Et</button>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)
