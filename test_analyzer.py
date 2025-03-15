# tests/test_analyzer.py
import unittest
from src.analyzer import analyze_sentiment, analyze_summary, analyze_ner

class TestNLPFunctions(unittest.TestCase):
    def test_sentiment(self):
        text = "I love this product!"
        result = analyze_sentiment(text)
        # Check that result is a list with at least one dictionary that has 'label' and 'score'
        self.assertIsInstance(result, list)
        self.assertIn('label', result[0])
        self.assertIn('score', result[0])
        
    def test_summary(self):
        text = (
            "Natural Language Processing (NLP) is a sub-field of artificial intelligence "
            "that focuses on the interaction between computers and humans through language. "
            "It has many practical applications such as text summarization, sentiment analysis, "
            "and machine translation."
        )
        summary = analyze_summary(text)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)
        
    def test_ner(self):
        text = "Apple was founded by Steve Jobs in Cupertino."
        entities = analyze_ner(text)
        self.assertIsInstance(entities, list)
        # Optionally, check if one of the recognized entities is "Apple"
        self.assertTrue(any("Apple" in entity.get("word", "") for entity in entities))

if __name__ == '__main__':
    unittest.main()
