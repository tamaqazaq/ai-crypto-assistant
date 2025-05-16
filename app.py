import streamlit as st
from services.news import get_news
from services.price import get_price
from services.market import get_market_data
from utils.summarizer import summarize

st.title("AI Crypto Assistant")

query = st.text_input("Enter your crypto question (e.g., 'Tell me about Ethereum')")

if query:
    with st.spinner("Fetching data..."):
        token = query.split()[-1].capitalize()

        print("Step 1: Calling get_news()")
        news = get_news(token)
        print("Step 1 complete")

        print("Step 2: Calling get_price()")
        price = get_price(token)
        print("Step 2 complete")

        print("Step 3: Calling get_market_data()")
        market = get_market_data(token)
        print("Step 3 complete")

        print("Step 4: Calling summarize()")
        context = f"{news}\n\nPrice: {price}\n\nMarket Info: {market}"
        answer = summarize(context, query)
        print("Step 4 complete")

    st.success("Done!")
    st.subheader("Answer:")
    st.write(answer)
