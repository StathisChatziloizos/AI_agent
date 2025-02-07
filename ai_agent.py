from llm import generate_answer, summarize_text, justify_collaboration
from scraper import scrape_webpage

class AI_Agent:
    """
    An autonomous agent capable of performing the following tasks:
    1. Researching B2B accounts for relevant news.
    2. Writing personal LinkedIn connect notes.
    3. Exploring a website for key business insights.
    4. Researching firmographic information.
    5. Answering company-related questions.
    """
    def __init__(self):
        self.memory = []  # Store intermediate results

    def perform_task(self, task_type: str, **kwargs) -> str:
        """
        Perform a specific task based on the task type.
        """
        if task_type == "research_b2b_news":
            company_name = kwargs.get("company_name", "")
            return self._research_b2b_news(company_name)

        elif task_type == "linkedin_connect_note":
            person_name = kwargs.get("person_name", "")
            return self._generate_linkedin_connect_note(person_name)

        elif task_type == "explore_website":
            website_url = kwargs.get("website_url", "")
            return self._explore_website(website_url)

        elif task_type == "research_firmographics":
            company_name = kwargs.get("company_name", "")
            return self._research_firmographics(company_name)

        elif task_type == "answer_company_questions":
            question_list = kwargs.get("question_list", "")
            company_name = kwargs.get("company_name", "")
            return self._answer_company_questions(company_name, question_list)

        else:
            return "Task type not supported."

    # --- TASK-SPECIFIC METHODS ---

    def _research_b2b_news(self, company_name: str) -> str:
        """
        Research relevant B2B news for a company using CBS News.
        """
        if not company_name:
            return "Company name is required for B2B news research."
        url = f"https://www.cbsnews.com/tag/{company_name.replace(' ', '_')}"
        print(f"Fetching B2B news from: {url}")
        news_content = scrape_webpage(url)
        if news_content:
            justification = justify_collaboration(news_content, company_name=company_name)
            return f"Should we collaborate with {company_name} based on the news:\n\n{justification}"
        return f"No relevant news found for {company_name}."

    def _generate_linkedin_connect_note(self, person_name: str) -> str:
        """
        Generate a personalized LinkedIn connect note for a given person.
        """
        if not person_name:
            return "Person name is required for generating a LinkedIn note."
        first_name, last_name = person_name.split()
        url = f"https://en.wikipedia.org/wiki/{first_name}_{last_name}"
        print(f"Fetching personal info from: {url}")
        personal_info = scrape_webpage(url)
        if personal_info:
            # Here we could enrich the prompt to create a fully automated LinkedIn note by giving it some more context
            # about us. For example, we could provide a brief description of our name, role, company and company's mission.
            linkedin_note_prompt = (
                f"Based on the following information about {person_name}:\n{personal_info}\n\n"
                "Write a friendly and professional LinkedIn connect note."
            )
            linkedin_note = generate_answer(linkedin_note_prompt)
            return linkedin_note
        return f"No relevant information found for {person_name}."

    def _explore_website(self, website_url: str) -> str:
        """
        Explore a website to extract key business insights.
        """
        # This method requires a valid URL to scrape the website content. An alternative approach could be to use
        # a search engone API to find the appropriate website URL(s) to crawl.
        if not website_url:
            return "Website URL is required to explore business insights."
        print(f"Exploring website: {website_url}")
        website_content = scrape_webpage(website_url)
        if website_content:
            exploration_prompt = (
                f"The following is content from the company's website:\n\n{website_content}\n\n"
                "Answer the following questions based on the content:\n"
                "1. What is the company's value proposition?\n"
                "2. What is the company's sales motion?\n"
                "3. What is the company's pricing structure?\n\n"
                "Provide concise and clear answers."
            )
            insights = generate_answer(exploration_prompt)
            return insights
        return "No relevant information found on the website."

    def _research_firmographics(self, company_name: str) -> str:
        """
        Research firmographic information for a company using Wikipedia.
        """
        # We use Wikipedia as a source for firmographic information. This, similar to the _explore_website method, could be
        # extended to use a search engine API to find relevant firmographic data from multiple sources.
        if not company_name:
            return "Company name is required for firmographic research."
        url = f"https://en.wikipedia.org/wiki/{company_name.replace(' ', '_')}"
        print(f"Fetching firmographics from: {url}")
        firmographic_content = scrape_webpage(url)
        if firmographic_content:
            summary = summarize_text(firmographic_content)
            return f"Firmographic information for {company_name}:\n\n{summary}"
        return f"No firmographic information found for {company_name}."

    def _answer_company_questions(self, company_name: str, questions: list) -> str:
        """
        Answer a list of questions about a company using Wikipedia or web scraping.
        """
        if not company_name or not questions:
            return "Both company name and a list of questions are required for this task."
        url = f"https://en.wikipedia.org/wiki/{company_name.replace(' ', '_')}"
        print(f"Fetching company information from: {url}")
        company_content = scrape_webpage(url)
        if company_content:
            answers = []
            for question in questions:
                question_prompt = (
                    f"Based on the following company information:\n{company_content}\n\n"
                    f"Answer this question: {question}\n"
                    "Provide a concise and accurate answer."
                )
                answer = generate_answer(question_prompt)
                answers.append(f"Q: {question}\nA: {answer}\n")
            return "\n".join(answers)
        return f"No relevant information found for {company_name}."