import analysis
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit as st
import time
st.set_page_config(layout="wide")



df = pd.read_csv("fox_index.csv")

def readability(df, score):
    if score <= 6:
        return "Sixth grade"
    elif score >= 17:
        return "College graduate"
    else:
        return (df['Reading level by grade'][df['Fog Index'] == score]).values[0]

def display(result):
    st.title("Results: ")
    tab1 = st.tabs(["Text Summary:"])[0]
    tab1.write(result["summary"][0]['summary_text'])

    st.header("Sentiment Analysis:")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        col1.metric("Positive Score", str(result["positive_score_num"])+"%", help="Indicates how positive sentence the is")
        #st.markdown("<span style='font-size: 1.2rem;'>Positive Score</span>", unsafe_allow_html=True)
        #st.header("83")
    with col2:
        col2.metric("Negative Score", str(result["negative_score_num"])+"%", help="Indicates how negative sentence the is")
        #st.markdown("<span style='font-size: 1.2rem;'>Negative Score</span>", unsafe_allow_html=True)
        #st.header("65")
    with col3:
        col3.metric("Polarity Score", str(result["polarity_score"]), help="Polarity scores are numerical values that range from -1 to 1, where -1 indicates a very negative sentiment, 0 indicates a neutral sentiment, and 1 indicates a very positive sentiment.")
        # st.markdown("<span style='font-size: 1.2rem; text-align: center;'>Polarity Score</span>", unsafe_allow_html=True)
        # st.header("93")
    with col4:
        col4.metric("Subjective Score", str(result["subjective_score"]), help="Subjectivity scores are numerical values that range from 0 to 1, where 0 indicates a very objective text, and 1 indicates a very subjective text. ")
        # st.markdown("<span style='font-size: 1.2rem; text-align: center;'>Subjective Score</span>", unsafe_allow_html=True)
        # st.header("52")


    st.markdown("<br><br>", unsafe_allow_html=True)

    st.header("Readability Score: ")
    col5, col6 = st.columns(2)
    with col5:
        st.text("Your Fox Index Score is: " + str(result["fox_index"]))
        st.write("The Gunning Fog formula generates a grade level between 0 and 20. It estimates the education level required to understand the text. According to your fox index score given text is likely to be understood by:")
        read_type = readability(df, int(result['fox_index']))
        st.subheader(f":green[{read_type}]")
    with col6:
        st.dataframe(df)

    st.header("Top Statistics: ")
    col7, col8, col9, col10 = st.columns(4)
    with col7:
        col7.metric("WORD COUNT", result["number_of_words"])
        # st.markdown("<span style='font-size: 1.2rem;'>WORD COUNT</span>", unsafe_allow_html=True)
        # st.header("2683")
    with col8:
        col8.metric("CHARACTERS COUNT", result["number_of_characters"])
        # st.markdown("<span style='font-size: 1.2rem;'>CHARACTERS COUNT</span>", unsafe_allow_html=True)
        # st.header("1665")
    with col9:
        col9.metric("SENTENCE COUNT", result["no_of_sentence"])
        # st.markdown("<span style='font-size: 1.2rem;'>SENTENCE COUNT</span>", unsafe_allow_html=True)
        # st.header("13357")
    with col10:
        col10.metric("COMPLEX WORD COUNT", result["count_complex_word"])
        # st.markdown("<span style='font-size: 1.2rem;'>SPEAKING TIME</span>", unsafe_allow_html=True)
        # st.header("123")

    st.markdown("<br><br>", unsafe_allow_html=True)
    col11, col12, col13, col14 = st.columns(4)
    with col11:
        col11.metric("AVERAGE WORD LENGTH", result["avg_word_len"])
        # st.markdown("<span style='font-size: 1.2rem;'>AVERAGE WORD LENGTH</span>", unsafe_allow_html=True)
        # st.header("2683")
    with col12:
        col12.metric("AVERAGE SENTENCE LENGTH", result["average_sentence_length"])
        # st.markdown("<span style='font-size: 1.2rem;'>AVERAGE SENTENCE LENGTH</span>", unsafe_allow_html=True)
        # st.header("1665")
    with col13:
        col13.metric("SYLLABLE COUNT", result["syllable_counts"])
        # st.markdown("<span style='font-size: 1.2rem;'>SYLLABLE COUNT</span>", unsafe_allow_html=True)
        # st.header("2683")
    with col14:
        col14.metric("PERCENTAGE OF COMPLEX WORDS", str(result["per_complex_words"])+"%")
        # st.markdown("<span style='font-size: 1.2rem;'>COMPLEX WORD COUNT</span>", unsafe_allow_html=True)
        # st.header("1665")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.metric("SPEAKING TIME", result["speaking_time"])
    # st.markdown("<span style='font-size: 1.2rem;'>PERCENTAGE OF COMPLEX WORDS</span>", unsafe_allow_html=True)
    # st.header("2683")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("Personal Pronoun: ")
    st.text(result["Personal Pronouns"])

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.subheader("Emotional Analysis: ")
    col16, col17 = st.columns(2)

    with col16:
        fig, ax = plt.subplots()
        data = result['emotions']
        #data = pd.DataFrame(data, index=[0, 1, 2, 3, 4])
        ax.bar(data["label"], data["score"], color='maroon', width=0.4)
        st.pyplot(fig)

    with col17:
        result["emotions"]["score"] = result["emotions"]["score"]*100
        st.dataframe(result['emotions'])



st.sidebar.title("Blog Post Analyser")


url = st.sidebar.text_input("Enter URL")

if "load_state" not in st.session_state:
    st.session_state.load_state = False


if st.sidebar.button('Analyse') or st.session_state.load_state:
    st.session_state.load_state = True
    st.empty()
    start=time.time()
    with st.spinner('Analysing...'):
        try:
            result = analysis.calculate_details(url)
            display(result)
        except:
            st.error('Kindly check your URL. Either the text is too short or too long to process.', icon="🚨")
    end = time.time()
    seconds = str(round(end-start, 1))
    st.toast('Analysis finished in ' + seconds + 's', icon='🎉')
    time.sleep(5)
st.sidebar.text('OR')
input_text = st.sidebar.text_area("Enter the text")
if st.sidebar.button('Analyse Text'):
    st.session_state.load_state = True
    st.empty()
    start = time.time()
    with st.spinner('Analysing...'):
        try:
            result = analysis.calculate_text_details(input_text)
            display(result)
        except:
            st.error('Either the text is too short or too long to process.', icon="🚨")
    end = time.time()
    seconds = str(round(end - start, 1))
    st.toast('Analysis finished in ' + seconds + 's', icon='🎉')
    time.sleep(5)


st.info('Click on > icon at the top-left corner to enter URL or text', icon="ℹ️")
st.title("Content Analyzer")
st.divider()
st.write("Content Analyser is a web app that allows you to gain insights into any type of content. It provides you with comprehensive results based on the text data analyzed and presents the information in a standardized form. It is a versatile tool that allows you to input information either in the form of a URL or text directly. Users consistently praise Content Analyzer for its user-friendly interface and quick results, citing these features as standout strengths of the web app.\n\nImagine having a personal writing coach who can instantly assess your writing style, sentiment, and readability. Content Analyser does exactly that, offering a range of features designed to help you polish your craft and achieve maximum impact with your audience.")
st.markdown("<br>", unsafe_allow_html=True)
st.header("Features")
para = '''
📝 **Text Summarization**

Gives you a summary of the text after analyzing your data. You must make sure that you enter a minimum of 60 words in the text area to get a valid summary. Therefore, this feature allows your long-form content to squeeze into concise, coherent summaries, saving valuable time during content review and editing. It gives you 50-200 words summary of your content based on the point that is most emphasized in the text.
\n\n
😃 **Sentiment Analysis**

This allows you to know the positive score, negative score, polarity score, and subjective score of your content. Positive score is the measure of positivity in your content. Negative score gives you an idea about how negative your content sounds. Polarity helps you understand the sentiment of the text. It is expressed in numerical values that range from -1 to 1, where -1 indicates a very negative sentiment, 0 indicates a neutral sentiment, and 1 indicates a very positive sentiment.
\n\n
📖 **Readability Scores**

Readability score gives you an idea about the text complexity. Content Analyser uses Gunning Fox formula to calculate the scores. The Gunning Fog formula generates a grade level between 0 and 20. It estimates the education level required to understand the text.
\n\n
🧮 **Statistical Insights**

The web app provides statistical insights like word count, character count, sentence count, complex word count, average word length, average sentence length, syllable count, percentage of complex words, and speaking time. You receive a detailed overview of your content's structural nuances.
\n\n
🗣️ **Personal Pronouns**

Using this tool you can identify and list personal pronouns used in the content. It provids valuable insights into the author's voice, tone, and perspective.
\n\n
🥹 **Emotion Detection**

You will get a visual picture of the top five emotions depicted in your text. This report is represented in the form of bar graph.
'''
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(para)

usage = '''
    \t**Step 1:** Access the Content Analyzer web app at https://content-analyser.streamlit.app/.
\n
    \t**Step 2:** Input the content for analysis by either providing a URL or directly entering the text.
\n
    \t**Step 3:** Click the "Analyze" button to initiate the analysis process.
\n
    \t**Step 4:** Review the detailed results provided in various sections, including text summarization, sentiment analysis, readability scores, statistical insights, personal pronouns, and emotion detection.
'''
st.markdown("<br>", unsafe_allow_html=True)
st.header("How to Use?")

st.markdown(usage)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.write("Thanking you for reading this far😇. I am working on this app to add new features and make it more interesting. Feel free to reachout to suggest ideas or give a feedback.")