import os
import json
from together import Together
from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    parsed_url = urlparse(url)

    if parsed_url.netloc in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    elif parsed_url.netloc in ["youtu.be"]:
        return parsed_url.path.lstrip("/")

    return None

app = Flask(__name__)

# Initialize the Together client
client = Together(api_key="c21c0fcab807ec6565316a83f4b146bc3513a2b885f7eb94393093b5c88d3b4f")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user's message from the request
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "No message provided."}), 400

        video_id = extract_video_id(user_message)
        if not video_id:
            return jsonify({"error": "Invalid YouTube URL."}), 400

        def get_transcript(video_id):
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                return "\n".join([entry['text'] for entry in transcript])
            except Exception as e:
                return jsonify({"error": f"Failed to fetch transcript: {str(e)}"}), 500

        transcript = get_transcript(video_id)
        if isinstance(transcript, dict) and "error" in transcript:
            return transcript

        # Generate a summary from the transcript
        prompt = f"""
        Summarize the following content in 3-5 sentences. Focus on the key points and main ideas:

        Content: {transcript}
        """

        # Define the conversation messages
        messages = [
            {"role": "user", "content": prompt}
        ]

        # Generate a chat completion
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=messages,
            max_tokens=200,  # Adjust max_tokens for a concise summary
            temperature=0.7,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=["<|eot_id|>", "<|eom_id|>"],
            stream=False
        )

        # Extract the bot's reply
        bot_reply = response.choices[0].message.content if response.choices else "Sorry, I couldn't process that."

        # Return the summary as JSON
        return jsonify({"summary": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)