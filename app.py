# src/app.py
from flask import Flask, request, render_template_string
from analyzer import analyze_sentiment, analyze_summary, analyze_ner

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
  <title>NLP Analyzer</title>
</head>
<body>
  <h1>NLP Analyzer</h1>
  <form method="post">
    <textarea name="text" rows="10" cols="50" placeholder="Enter your text here..."></textarea><br><br>
    <label for="analysis_type">Choose Analysis:</label>
    <select name="analysis_type">
      <option value="sentiment">Sentiment Analysis</option>
      <option value="summary">Text Summarization</option>
      <option value="ner">Named Entity Recognition</option>
    </select><br><br>
    <input type="submit" value="Analyze">
  </form>
  {% if result %}
    <h2>Result:</h2>
    <pre>{{ result }}</pre>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form.get("text", "")
        analysis_type = request.form.get("analysis_type", "sentiment")
        if text:
            if analysis_type == "sentiment":
                result = analyze_sentiment(text)
            elif analysis_type == "summary":
                result = analyze_summary(text)
            elif analysis_type == "ner":
                result = analyze_ner(text)
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
