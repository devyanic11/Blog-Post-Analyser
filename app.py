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
    start=time.time()
    with st.spinner('Analysing...'):
        result = analysis.calculate_details(url)
        if (time.time() - start) == 3:
            st.write("Kindly wait!! That was a lot to process")
        display(result)
    end = time.time()
    seconds = str(round(end-start, 1))
    st.toast('Analysis finished in ' + seconds + 's', icon='🎉')
    time.sleep(5)
st.sidebar.text('OR')
input_text = st.sidebar.text_area("Enter the text")
if st.sidebar.button('Analyse Text'):
    with st.spinner('Analysing...'):
        result = analysis.calculate_text_details(input_text)
        display(result)

