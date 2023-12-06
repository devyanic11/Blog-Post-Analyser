# Content Analyzer

![App Screenshot](https://github.com/devyanic11/Blog-Post-Analyser/blob/main/content-analyser.jpg)

<!--- [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]((https://github.com/devyanic11/Blog-Post-Analyser/blob/7e6ca11cb9b5fe2a5268857f7263b11e93e1d9c9/LICENSE))
[![GitHub Issues](https://img.shields.io/github/issues/your-username/content-analyzer)](https://github.com/your-username/content-analyzer/issues)
[![GitHub Stars](https://img.shields.io/github/stars/your-username/content-analyzer)](https://github.com/your-username/content-analyzer/stargazers)
---> 

The Content Analyzer is a powerful and intuitive web application designed for analyzing textual content with a focus on providing comprehensive insights. 

<br>

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<br>

## About the Project

Content Analyser is a web app that allows you to gain insights into any type of content. It provides you with comprehensive results based on the text data analyzed and presents the information in a standardized form. It is a versatile tool that allows you to input information either in the form of a URL or text directly. Users consistently praise Content Analyzer for its user-friendly interface and quick results, citing these features as standout strengths of the web app.

Imagine having a personal writing coach who can instantly assess your writing style, sentiment, and readability. Content Analyser does exactly that, offering a range of features designed to help you polish your craft and achieve maximum impact with your audience.

Certainly, it is more than just a tool; it's a catalyst for writing growth. It empowers you to refine your style, optimize your content for your target audience, and ultimately, become a more skilled and confident writer. 

So, whether you're crafting a blog post, a business proposal, or any other form of written communication, Content Analyser is there to guide you every step of the way. Unleash the full potential of your words and take your writing to the next level with this powerful and insightful web app.

<br>

## Features

- **Text Summarization**
  <p>Gives you a summary of the text after analyzing your data. You must make sure that you enter a minimum of 60 words in the text area to get a valid summary. Therefore, this feature allows your long-form content to squeeze into concise, coherent summaries, saving valuable time during content review and editing. It gives you 50-200 words summary of your content based on the point that is most emphasized in the text.</p>

- **Sentiment Analysis**
  <p>This allows you to know the positive score, negative score, polarity score, and subjective score of your content. Positive score is the measure of positivity in your content. Negative score gives you an idea about how negative your content sounds. Polarity helps you understand the sentiment of the text. It is expressed in numerical values that range from -1 to 1, where -1 indicates a very negative sentiment, 0 indicates a neutral sentiment, and 1 indicates a very positive sentiment.</p>

- **Readability Scores**
  <p>Readability score gives you an idea about the text complexity. Content Analyser uses Gunning Fox formula to calculate the scores. The Gunning Fog formula generates a grade level between 0 and 20. It estimates the education level required to understand the text. </p>

- **Statistical Insights**
  <p>The web app provides statistical insights like word count, character count, sentence count, complex word count, average word length, average sentence length, syllable count, percentage of complex words, and speaking time. You receive a detailed overview of your content's structural nuances.</p>

- **Personal Pronouns**
  <p>Using this tool you can identify and list personal pronouns used in the content. It provids valuable insights into the author's voice, tone, and perspective.</p>

- **Emotion Detection**
  <p>You will get a visual picture of the top five emotions depicted in your text. This report is represented in the form of bar graph. </p>


<br>

## Getting Started

### Prerequisites

- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [streamlit](https://streamlit.io/) (latest version applicable)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
- [requests](https://docs.python-requests.org/en/latest/)
- [regex](https://pypi.org/project/regex/)
- [nltk](https://www.nltk.org/)
- [pyphen](https://pyphen.org/)
- [transformers](https://huggingface.co/transformers/)
- [scipy](https://www.scipy.org/)
- [torch](https://pytorch.org/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/content-analyzer.git
   
2. Navigate to the project directory:
   ```bash
   cd content-analyzer
   
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    
5. Run the app:
   ```bash
    streamlit run app.py
   
7. Access the app in your browser at http://localhost:8501

<br>

## Usage
1. Access the Content Analyzer web app at https://content-analyser.streamlit.app/.
2. Input the content for analysis by either providing a URL or directly entering the text.
3. Click the "Analyze" button to initiate the analysis process.
4. Review the detailed results provided in various sections, including text summarization, sentiment analysis, readability scores, statistical insights, personal pronouns, and emotion detection.

<br>

## Contributing
We welcome and appreciate contributions from the community! If you'd like to contribute to Content Analyzer, here's how you can get involved:

If you encounter a bug, have a feature request, or want to suggest an improvement, please open an issue on the [GitHub Issue Tracker](https://github.com/devyanic11/Blog-Post-Analyser/issues). When submitting an issue, please provide as much detail as possible, including steps to reproduce the problem or a clear description of the new feature.

If you'd like to contribute to the project, feel free to open an issue or submit a pull request.

<br>

## License
This project is licensed under the [MIT License](https://github.com/devyanic11/Blog-Post-Analyser/blob/7e6ca11cb9b5fe2a5268857f7263b11e93e1d9c9/LICENSE).

