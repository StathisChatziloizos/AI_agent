
import ai_agent as ai

if __name__ == "__main__":
    agent = ai.AI_Agent()

    # Example 1: Research B2B accounts for news
    print("- - - - - - - - Example 1: NEWS/COLLABORATION JUSTIFICATION - - - - - - - - ")
    print(agent.perform_task("research_b2b_news", company_name="NVIDIA"))
    print("-" * 50, "\n")

    # Example 2: Write a LinkedIn connect note
    print("- - - - - - - - Example 2: LINKEDIN PERSONALIZED CONNECT NOTE - - - - - - - - ")
    print(agent.perform_task("linkedin_connect_note", person_name="Elon Musk"))
    print("-" * 50, "\n")

    # Example 3: Explore a website for insights
    print("- - - - - - - - Example 3: WEBSITE - - - - - - - - ")
    print("Explore a website for insights:")
    print(agent.perform_task("explore_website", website_url="https://www.libramli.ai/about/company"))
    print("-" * 50, "\n")

    # Example 4: Research firmographic information
    print("- - - - - - - - Example 4: FIRMOGRAPHICS - - - - - - - - ")
    print("Research firmographic information:")
    print(agent.perform_task("research_firmographics", company_name="Tesla, Inc."))
    print("-" * 50, "\n")

    # Example 5: Answer a question about a company
    print("- - - - - - - - Example 5: COMPANY QUESTIONS - - - - - - - - ")
    print("Answer a question about a company:")
    company_name = "OpenAI"
    print(agent.perform_task(
        "answer_company_questions",
        company_name=company_name,
        question_list=[f"Where is {company_name} located?",\
                        f"What is {company_name}'s main product or service provided?",\
                        f"What is {company_name}'s mission statement?"]
    ))
    print("-" * 50, "\n")
