import streamlit as st
from gpt import OpenAIAPI
from file_manager import FileManager

class ChatBotApp:
    def __init__(self):
        self.file_manager = FileManager()
        self.api_key = self.file_manager.load_api_key()
        self.initialize_session_state()

    def initialize_session_state(self):
        if 'messages' not in st.session_state:
            st.session_state['messages'] = []
        if 'current_conversation' not in st.session_state:
            st.session_state['current_conversation'] = ''
        if 'model' not in st.session_state:
            st.session_state['model'] = 'gpt-3.5-turbo'
        if 'api_key' not in st.session_state:
            st.session_state['api_key'] = self.api_key

    def display_main_page(self):
        messages = self.file_manager.read_messages(st.session_state['messages'])

        st.header('🤖 N-GPT', divider=True)

        for message in messages:
            chat = st.chat_message(message['role'])
            chat.markdown(message['content'])
        
        prompt = st.chat_input('Talk to the chat')
        if prompt:
            if st.session_state['api_key'] == '':
                st.error('Add an API key in the settings tab')
            else:
                new_message = {'role': 'user', 'content': prompt}
                chat = st.chat_message(new_message['role'])
                chat.markdown(new_message['content'])
                messages.append(new_message)

                openai_api = OpenAIAPI(st.session_state['api_key'])
                chat = st.chat_message('assistant')
                placeholder = chat.empty()
                placeholder.markdown("▌")
                full_response = ''
                responses = openai_api.get_response(messages,
                                                    model=st.session_state['model'],
                                                    stream=True)
                for response in responses:
                    full_response += response.choices[0].delta.get('content', '')
                    placeholder.markdown(full_response + "▌")
                placeholder.markdown(full_response)
                new_message = {'role': 'assistant', 'content': full_response}
                messages.append(new_message)

                st.session_state['messages'] = messages
                self.file_manager.save_messages(messages)

    def display_conversations_tab(self, tab):
        tab.button('➕ New Conversation', on_click=self.new_conversation, use_container_width=True)
        tab.markdown('')
        conversations = self.file_manager.list_conversations()
        for filename in conversations:
            message_name = self.file_manager.revert_message_name(filename)
            if len(message_name) == 30:
                message_name += '...'
            tab.button(message_name,
                       on_click=self.select_conversation,
                       args=(filename,),
                       disabled=filename == st.session_state['current_conversation'],
                       use_container_width=True)

    def display_settings_tab(self, tab):
        selected_model = tab.selectbox('Select the model', ['gpt-3.5-turbo', 'gpt-4'])
        st.session_state['model'] = selected_model

        api_key = tab.text_input('Add your API key', value=st.session_state['api_key'])
        if api_key != st.session_state['api_key']:
            st.session_state['api_key'] = api_key
            self.file_manager.save_api_key(api_key)
            tab.success('Key saved successfully')

    def new_conversation(self):
        self.select_conversation('')

    def select_conversation(self, filename):
        if filename == '':
            st.session_state['messages'] = []
        else:
            messages = self.file_manager.read_message_by_file_name(filename)
            st.session_state['messages'] = messages
        st.session_state['current_conversation'] = filename

    def run(self):
        self.display_main_page()
        tab1, tab2 = st.sidebar.tabs(['Conversations', 'Settings'])
        self.display_conversations_tab(tab1)
        self.display_settings_tab(tab2)

def main():
    app = ChatBotApp()
    app.run()

if __name__ == '__main__':
    main()