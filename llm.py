import google.generativeai as genai
from config import GENAI_API_KEY

# Configure the API key
genai.configure(api_key=GENAI_API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")
default_generation_config = genai.GenerationConfig(max_output_tokens=8192)

def generate_answer(prompt: str, max_output_tokens: int = 300) -> str:
    """
    General-purpose function to generate an answer for a given user prompt.
    """
    try:
        generation_config = genai.GenerationConfig(max_output_tokens=max_output_tokens)
        response = model.generate_content(prompt, generation_config=generation_config)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating answer: {e}")
        return ""

def summarize_text(text: str, max_output_tokens: int = 1000, concise: bool = True) -> str:
    """
    Summarize a given text using the LLM.
    """
    if concise:
        concise = "\n\nConcise summary:"
    if not text:
        return "No content available to summarize."
    prompt = f"Summarize the following text:\n\n{text}{concise}"
    try:
        generation_config = genai.GenerationConfig(max_output_tokens=max_output_tokens)
        response = model.generate_content(prompt, generation_config=generation_config)
        return response.text.strip()
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return ""

def justify_collaboration(text: str, max_output_tokens: int = 1000, company_name: str = "") -> str:
    """
    Justify collaborating with a target company based on our company's mission.
    """
    if not text:
        return "No content available to summarize."
    # This is a sample prompt that can be customized based on MadKudu's product, mission, objectives etc.
    prompt = f"You are an advisor for a company that does this \"We're a team of innovators solving a real problem in b2B SaaS Marketing. \
        Successful B2B marketing teams utilize data science to unlock rapid growth and beat out the competition. But doing that is hard \
        work due to high volumes of inaccessible data, constant changes in the market, and reliance on engineers. We’re on a mission to \
        help go-to-market teams operationalize data science to make informed decisions and drive meaningful revenue growth. \
        No coding required.\". The use cases are these \"MadKudu can be used to increase pipeline generation and GTM productivity across most \
        of your motions. Below is a list of common use cases.\
        Outbound & ABM:\
        Run ABM/Outbound outbound plays\
        Prioritize target accounts with scoring\
        Automate ABM/Outbound sales outreach\
        Automate account research (single pane of glass)\
        Capture buying signals (from 1st/2nd/3rd-party buying signals like LI activity, job postings, …)\
        Inbound:\
        Qualify and Prioritize inbound leads with scoring (MQLs/MQAs)\
        Automate Inbound sales outreach\
        Run inbound / warm outbound Sales plays\
        Product-led Sales (PLS):\
        Run PLS Sales plays\
        Qualify and prioritize Product users and accounts with scoring\
        Automate PLS outreach\
        Get 360 insights on product users and accounts\
        Expansion:\
        Run Expansion Sales plays\
        Identify Expansion opportunities with scoring \
        Automate Expansion post-sales outreach\
        Get 360 insights on customer accounts \" \
        Now this is the target company ({company_name}) that you want to justify whether it would be beneficial or not to collaborate:\n\n{text}"
    try:
        generation_config = genai.GenerationConfig(max_output_tokens=max_output_tokens)
        response = model.generate_content(prompt, generation_config=generation_config)
        return response.text.strip()
    except Exception as e:
        print(f"Error justifying collaboration: {e}")
        return ""