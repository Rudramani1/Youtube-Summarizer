# 🎥 YouTube Video Summarizer  

This is a **Flask-based web application** that extracts and summarizes transcripts from YouTube videos using the **YouTube Transcript API** and **Together AI**.

## 🚀 Features  
✅ Extracts transcripts from YouTube videos.  
✅ Generates a concise summary using AI.  
✅ Simple and user-friendly web interface.  
✅ Uses Flask as the backend framework.  

---

## 🛠️ Tech Stack  
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **APIs:** YouTube Transcript API, Together AI  
- **Database:** (Optional) SQLite/Firebase  

---

## 📌 Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```

### 2️⃣ Set Up Virtual Environment  
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements/requirements.txt
```

### 4️⃣ Run the Application  
```sh
python app.py
```
Now, open `http://127.0.0.1:5000/` in your browser. 🎉

---

## 📂 Project Structure  
```
📁 youtube-summarizer
│── 📁 static          # CSS & JavaScript files  
│── 📁 templates       # HTML files  
│── 📁 requirements    # Dependencies  
│── app.py            # Main Flask app  
│── .gitignore        # Ignoring unnecessary files  
│── requirements.txt  # Required Python packages  
│── README.md         # Project Documentation  
```

---

## 📜 .env File (For API Keys)  
If using Together AI or other APIs, create a `.env` file:  

```ini
TOGETHER_API_KEY=your_api_key
```

---

## 🌟 How It Works  
1. Enter a YouTube video URL in the input field.  
2. Click "Generate Summary".  
3. The app fetches the transcript and summarizes it.  
4. The summary is displayed in the output card.  

---

## 🚀 Uploading to GitHub  
Follow these steps to upload your project to GitHub:  

### 1️⃣ Initialize Git  
```sh
git init
```

### 2️⃣ Create a `.gitignore` File  
Run the following to ignore unnecessary files:  

```sh
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.sqlite3" >> .gitignore
echo ".env" >> .gitignore
```

### 3️⃣ Add and Commit Changes  
```sh
git add .
git commit -m "Initial commit"
```

### 4️⃣ Push to GitHub  
Replace `USERNAME` and `REPO_NAME` with your details:  

```sh
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## 💡 Future Enhancements  
✅ Support for multiple languages.  
✅ Option to download the summary.  
✅ Integration with OpenAI/GPT-4 for better summaries.  

---

## 📝 License  
This project is licensed under the MIT License.  

Made with ❤️ by [Your Name] 🚀  
```

---

### **How to Add This to Your Repo**
1. Create a `README.md` file in your project folder:  
   ```sh
   touch README.md
   ```
2. Open the file in a text editor and paste the above content.
3. Add and commit it to Git:
   ```sh
   git add README.md
   git commit -m "Added README"
   git push origin main
   ```
