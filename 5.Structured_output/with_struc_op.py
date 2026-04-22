from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
import os

load_dotenv()

llm = ChatOpenAI(
    # model="openai/gpt-4o-mini",
    model="gpt-4o-mini",
    base_url=os.getenv("OPENAI_BASE_URl"),
    api_key=os.getenv("OPENAI_API_KEY")
)

class Review(TypedDict):
    key_themes: Annotated[list[str],"write down all the keys themes discussed in the review in the list"]
    summary: Annotated[str,"write a brief summary"]
    sentiments: Annotated[Literal["pos","neg"],"give positive,negative or neutral based on summary"]
    pros: Annotated[Optional[list[str]],"Write down all the pros inside a list "]
    cons: Annotated[Optional[list[str]],"Write down all the cons inside a list "]
    name: Annotated[Optional[str],"Write the name of the review"]

str_output = llm.with_structured_output(Review)

result = str_output.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Akshat Tayal
""")

# print(result)
# print(result['summary'])
# print(result['sentiments'])
# print(result['key_themes'])
# print(result['pros'])
# print(result['cons'])
print(result['name'])