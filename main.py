import gradio as gr
from dotenv import load_dotenv
from manager_agent import manager_agent
from agents import Runner, trace, gen_trace_id

load_dotenv(override=True)


async def run_chat(input: str, chat_history:list):
    chat_history.append({"role":"user","content":input})

    chat_history.append({"role":"assistant","content":"Thinking..."})
    yield chat_history, ""
    
    messages = [{"role": message["role"], "content": message["content"]} for message in chat_history[:-1]]
    
    result= await Runner.run(
        manager_agent,
        messages
    )

    chat_history[-1] = {"role": "assistant", "content": result.final_output}
    yield chat_history, ""


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    chat= gr.Chatbot(type="messages", label="Research AI Tool")
    chat_history=gr.State([])

    txt=gr.Textbox(placeholder="Please ask your query...", show_label=False)
    btn=gr.Button("Ask")

    btn.click(
        fn=run_chat,
        inputs=[txt, chat_history],
        outputs=[chat, txt],
    )
    txt.submit(
        fn=run_chat,
        inputs=[txt, chat_history],
        outputs=[chat, txt],
    )

ui.launch(inbrowser=True)