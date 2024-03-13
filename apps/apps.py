import streamlit as st
import pyperclip as clip

def app():
    st.title('Custom CV Template Prompt Generator')
    st.write('This app is designed to help you generate a custom CV template prompt for your next job application. Simply fill in the form below and click "Generate Prompt" to get started.')
    st.write('Once you have your prompt, you can use it to create a custom CV template using GPT-based text generation tools like OpenAI\'s ChatGPT. You can also use it to guide your CV writing process, ensuring that you include all the relevant information that the employer is looking for.')

    with open('apps/template.txt', 'r') as file:
        template = file.read()

    st.subheader('Input your previous CV here')
    st.write('Paste your previous CV into the text box below. This will help the app generate a prompt that is tailored to your specific experience and skills.')
    previous_cv = st.text_area('Paste your previous CV here', height=200)

    template = template.replace('cv_here', previous_cv)

    st.subheader('Input the job description here')
    st.write('Paste the job description into the text box below. This will help the app generate a prompt that is tailored to the specific requirements of the job you are applying for.')
    job_description = st.text_area('Paste the job description here', height=200)

    template = template.replace('desc_here', job_description)

    st.subheader('Input the company information here')
    st.write('Paste the company information into the text box below. This will help the app generate a prompt that is tailored to the specific requirements of the company you are applying to.')
    company_info = st.text_area('Paste the company information here', height=200)
    template = template.replace('ci_here', company_info)

    st.subheader('Generate Prompt')
    st.write('Click the button below to generate your custom CV template prompt.')


    template_bytes = template.encode()
    st.download_button(label='Generate and Download Prompt', data=template_bytes, file_name='prompt.txt', mime='text/plain')

    if st.button('Auto-Copy Prompt'):
        template = "Your generated prompt content here"

        # Copy the template to clipboard
        clip.copy(template)
        st.success("Prompt copied to clipboard!")


if __name__ == '__main__':
    app()