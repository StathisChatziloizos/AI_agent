# Overview
This AI agent is designed to autonomously perform business-related tasks using NLP capabilities powered by Google Generative AI (Gemini) and basic web scraping. It can assist in generating insights, writing personalized messages, analyzing websites and more.

# Features

* Research B2B accounts for relevant news:
Analyze company-related news to justify collaboration with other businesses.

* Write a personalized LinkedIn connect note:
Use public information (e.g. Wikipedia) to craft professional and personal connection notes.

* Explore websites for business insights:
Scrape websites to summarize the value proposition, sales motion and pricing structure.

* Research firmographic information:
Use Wikipedia or other public sources to gather details such as company size, industry, and location.

* Answer questions about companies:
Answer specific questions about a company by searching and summarizing publicly available information.

# Build and Run Instructions
### Build a conda environment
```bash
conda create -n ai_agent python=3.12.7
conda activate ai_agent
```
### Install the required packages
```bash
pip install -r requirements.txt
```
### Change the API key in the `config.py` file
This AI agent uses the GenAI API for NLP tasks. You need to get an API key from the gemini website and put it in the `config.py` file.
```python
GENAI_API_KEY = os.getenv("GENAI_API_KEY", "PUT_YOUR_API_KEY_HERE")
```

### Run the agent
```bash
python run_agent.py
```

# Documentation
Extensive comments and doc strings are provided in the code to explain the functionality and logic of the AI agent.

`ai_agent.py`:\
Implements the AI agent’s tasks, including:

* Researching news to justify collaboration between our company and a target company.
* Writing LinkedIn connect notes.
* Exploring websites for insights.
* Researching firmographics.
* Answering company-related questions.

`llm.py`:\
Handles interactions with Google Generative AI, including:
* Summarizing content.
* Generating detailed answers.
* Providing collaboration justifications.

`scraper.py`:
Implements web scraping using BeautifulSoup to extract text from websites.

`run_agent.py`:
Demonstrates the AI agent's capabilities with examples.

# Sample output
```text
- - - - - - - - Example 1: NEWS/COLLABORATION JUSTIFICATION - - - - - - - - 
Fetching B2B news from: https://www.cbsnews.com/tag/NVIDIA
Should we collaborate with NVIDIA based on the news:

The provided text highlights Nvidia's massive success in AI, driven by its advanced technology and a skyrocketing (though volatile) stock price.  However, the question of whether MadKudu would be beneficial requires a deeper analysis than simply observing Nvidia's overall performance.

**Arguments for MadKudu's Benefit to NVIDIA:**

* **Scale and Complexity:**  While Nvidia is a leader in AI,  its marketing and sales operations are likely vast and complex.  Managing numerous sales motions (Outbound, Inbound, PLS, Expansion) across a global market requires efficient data-driven decision-making.  MadKudu's ability to automate processes and provide a single pane of glass for account insights could significantly streamline operations, especially considering the high volume of data Nvidia likely generates.

* **Increased GTM Productivity:**  Optimizing GTM (Go-to-Market) productivity is crucial for maintaining growth.  MadKudu's features for lead scoring, prioritization, and automated outreach could help Nvidia's sales teams focus their efforts on the most promising leads, improving conversion rates and overall efficiency.  This is especially valuable considering the competitive landscape in the AI sector.

* **Data-Driven Insights:** Nvidia likely possesses massive amounts of data, but extracting actionable insights can be challenging. MadKudu's no-code platform promises to make this data accessible to marketing and sales teams, enabling them to make more informed decisions without relying heavily on engineering resources.

* **Account-Based Marketing (ABM):**  Given Nvidia's focus on high-value clients and enterprise solutions, ABM is likely a key part of their strategy. MadKudu's ABM capabilities could help them refine their targeting, personalize outreach, and improve engagement with strategic accounts.


**Arguments Against MadKudu's Benefit to NVIDIA:**

* **Existing Infrastructure:** Nvidia likely already has sophisticated internal systems and tools for marketing and sales. Integrating MadKudu might require significant effort and potentially disrupt existing workflows.  The cost-benefit analysis would need to justify the investment against the potential returns.

* **Internal Expertise:**  As a tech giant, Nvidia likely employs data scientists and analysts capable of performing many of the functions MadKudu offers.  The value proposition of a no-code platform might be less compelling if Nvidia already possesses the in-house expertise.

* **Focus on R&D:**  Nvidia's primary focus is likely on R&D and product development, not necessarily on optimizing marketing and sales processes to the same level of detail as a pure SaaS company.  They might view marketing as a supporting function, and the ROI of MadKudu might not be a top priority.

**Conclusion:**

Whether MadKudu is beneficial for Nvidia is not a simple yes or no answer.  A thorough assessment is required, considering:

1. **Nvidia's current marketing and sales technology stack:** What existing tools are in place?  What are their limitations?
2. **Nvidia's internal resources and expertise:** Does the company have the in-house capabilities to achieve similar results without MadKudu?
3. **The cost-benefit analysis:**  Does the potential ROI of increased GTM productivity and efficiency justify the implementation costs and integration efforts?

Only after a detailed assessment of these factors can a well-informed decision be made regarding the potential benefits of a collaboration between Nvidia and MadKudu.  The potential is there, but it's not guaranteed without a deeper dive into Nvidia's specific needs and operational structure.
-------------------------------------------------- 

- - - - - - - - Example 2: LINKEDIN PERSONALIZED CONNECT NOTE - - - - - - - - 
Fetching personal info from: https://en.wikipedia.org/wiki/Elon_Musk
Subject: Connecting on LinkedIn - Shared Interests in [Mention a shared industry/interest]

Hi Elon,

My name is [Your Name], and I'm a [Your Title] at [Your Company]. I came across your profile and was impressed by your extensive experience in [mention a specific area, e.g., entrepreneurship, space exploration, sustainable energy].  Your work with [mention a specific company, e.g., SpaceX, Tesla, X Corp] is particularly inspiring.

I'm particularly interested in [mention something specific that connects you - e.g.,  your advancements in electric vehicles, your approach to AI development, etc.].  I'd be interested in connecting to learn more about your perspectives on [mention a relevant topic].

Would you be open to connecting?

Best regards,

[Your Name]
[Your LinkedIn Profile URL (Optional)]
-------------------------------------------------- 

- - - - - - - - Example 3: WEBSITE - - - - - - - - 
Explore a website for insights:
Exploring website: https://www.libramli.ai/about/company
1. **Value Proposition:**  Affordable, customized machine learning and AI business intelligence services that deliver business disruption and growth through innovative solutions leveraging cutting-edge technology.  They aim to make AI accessible to all.

2. **Sales Motion:**  Direct sales to entrepreneurs and research/industrial organizations, primarily through consultancy services.  Their website serves as a lead generation tool.

3. **Pricing Structure:** The provided text only states that their services are "affordable," but doesn't detail a specific pricing structure (e.g., hourly rate, project-based pricing, subscription).
-------------------------------------------------- 

- - - - - - - - Example 4: FIRMOGRAPHICS - - - - - - - - 
Research firmographic information:
Fetching firmographics from: https://en.wikipedia.org/wiki/Tesla,_Inc.
Firmographic information for Tesla, Inc.:

Tesla, Inc., founded in 2003, is a multinational company producing electric vehicles (EVs), battery storage, solar panels, and related products.  Elon Musk became a major investor and CEO, leading the company through various funding rounds and production launches, starting with the Roadster and culminating in the highly successful Model 3 and Model Y.  Tesla has become one of the world's most valuable companies, dominating the EV market, but has also faced controversies regarding worker rights, safety, and Musk's public statements.  The company's journey included initial struggles, government loans, and a successful IPO, ultimately transforming it into a global leader in the clean energy and automotive sectors.
-------------------------------------------------- 

- - - - - - - - Example 5: COMPANY QUESTIONS - - - - - - - - 
Answer a question about a company:
Fetching company information from: https://en.wikipedia.org/wiki/OpenAI
Q: Where is OpenAI located?
A: OpenAI is headquartered in San Francisco, California.

Q: What is OpenAI's main product or service provided?
A: OpenAI's main products are large language models (like GPT), text-to-image models (like DALL-E), and a text-to-video model (Sora).  These power services like ChatGPT.

Q: What is OpenAI's mission statement?
A: OpenAI's mission is to develop "safe and beneficial" artificial general intelligence (AGI).

-------------------------------------------------- 
```
