import openai
import gradio

openai.api_key = "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  "

messages = [{"role": "system", "content": "You are a Super Smart ChatBot named K "}]

def CustomChatGPT(input):
    messages.append({"role": "user", "content": input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Smart-K")

demo.launch(share=True)