import streamlit as st


# with st.chat_message(name="user"): # or you can name = assistant
#     st.write("Hello ✌️")

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat message from history on app return
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("what is up?"):
    # Display user message in chat container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display Assistant response in chat container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add Assistant response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    