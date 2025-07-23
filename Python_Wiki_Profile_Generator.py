"""
Wikipedia Profile Generator
----------------------------
Fetches summary content from Wikipedia using the wikipedia API.
Given a name/topic, returns a brief profile.

Skills:
- API-based data access
- Text summarization
- Exception handling
"""

import wikipedia

# Set language (optional)
wikipedia.set_lang("en")

# Ask user or define a topic
topic = "Barack Obama"  # You can change this to any name, e.g. "Turkey", "Machine Learning"

try:
    # Get summary (first 2 paragraphs)
    summary = wikipedia.summary(topic, sentences=5)

    print(f"📘 Wikipedia Profile for: {topic}\n")
    print(summary)

except wikipedia.exceptions.DisambiguationError as e:
    print(f"⚠️ The term '{topic}' is ambiguous. Options include:\n")
    print(e.options[:5])
except wikipedia.exceptions.PageError:
    print(f"❌ No Wikipedia page found for: {topic}")
except Exception as e:
    print("An unexpected error occurred:", e)
