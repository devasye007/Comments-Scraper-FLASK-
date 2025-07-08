# 🗣️ Comment Scraper + Sentiment Analyzer

This is a Python-Flask based web application that allows users to **scrape comments from a given URL**, download them as a **CSV file**, and perform **sentiment analysis** on the collected data using the **VADER (NLTK)** sentiment model.

---

## 🚀 Features

- 🌐 Input a webpage URL and extract all visible comments
- 📄 Export the scraped comments to a downloadable CSV file
- 🧠 Upload the CSV to analyze sentiment: **Positive**, **Negative**, or **Neutral**
- 🔍 Real-time display of sentiment results
- Built using **Flask**, **VADER**, **Pandas**, and **NLTK**

---

## 📂 Project Structure

comment-scraper-sentiment/
│
├── app.py # Main Flask application
├── templates/
│ ├── index.html # Input form and sentiment display
│
├── static/ # (Optional) CSS/JS files
├── comments.csv # Scraped output file
├── README.md # Project documentation
---

## 🧠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML (Jinja2 templates), Basic CSS  
- **Libraries:** NLTK (VADER), Pandas  
- **Export Format:** CSV

---

## ⚙️ How It Works

1. **Enter URL**  
   User enters the URL of a page containing visible comments (YouTube, blog, etc.)

2. **Scraping Comments**  
   Using a scraping script (e.g., `requests + BeautifulSoup`), the app extracts all text-based comments.

3. **Download CSV**  
   The comments are exported into a CSV file, which the user can download.

4. **Upload CSV for Sentiment Analysis**  
   The user uploads the CSV file containing comments. The app then uses **VADER** to classify each comment as **positive**, **negative**, or **neutral**.

5. **Results Displayed**  
   The results are shown in the UI — either as a list or summarized view (expandable).

---

## ✅ Requirements

Install dependencies via pip:

```bash
pip install flask nltk pandas
