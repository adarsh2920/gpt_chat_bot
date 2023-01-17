import os
import openai
import gradio as gr

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0.6,
    presence_penalty=0.95,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text





def myChatgpt(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Welcome to GBT Chatbot</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="ask me anything ")
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(myChatgpt, inputs=[message, state], outputs=[chatbot, state])
    css="footer {visibility: hidden}"

block.launch(debug = True)
