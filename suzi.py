from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/suzi", methods=["POST"])
def suzi_advice():
    data = request.json
    health_data = data.get("health_data", "")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful doctor."},
            {"role": "user", "content": f"A patient says: {health_data}. Please give general medical advice."}
        ]
    )
    
    advice = response.choices[0].message.content.strip()
    return jsonify({"advice": advice})

if __name__ == "__main__":
    app.run(debug=True)
