# Count Down Timer Project Using Streamlit

import streamlit as st
import time

# Countdown timer function
def countdown_timer(seconds, restart_event):
    while seconds > 0 and not restart_event:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        st.text(time_format)
        time.sleep(1)
        seconds -= 1

        if restart_event:
            st.header("Timer Restarted!")
            return
    if not restart_event:
        st.text("00:00 \nTime's finished!👍")
    
    st.text("Created this app with ❤️️ by Saba Ali Zain")

# streamlit
st.title("Countdown Timer App ⌚")

# user input for timer
total_seconds = st.number_input("Enter time in seconds for countdown:", min_value=1, step=1)

if "restart_event" not in st.session_state:
    st.session_state.restart_event = False

if st.button("Start ⌛ Timer"):
    st.session_state.restart_event = False
    st.header("Timer Started!")
    countdown_timer(total_seconds, st.session_state.restart_event)

if st.button("Start Timer Again!🌞"):
    st.session_state.restart_event = True