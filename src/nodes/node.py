from src.states.blogstate import BlogState,Blog
from langchain_core.messages import HumanMessage

class BlogNode:
    """
    A class to represent the blog node
    """

    def __init__(self,llm):
        self.llm=llm

    def title_creation(self,state:BlogState):
        
        """
        CREATE THE TITLE FOR THE BLOG.
        """

        if "topic" in state and state['topic']:
            prompt="""
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the {topic}. This title should be creative and SEO friendly.
                   Do not provide alternate titles or any additional detail except title.
                   """
            system_message=prompt.format(topic=state['topic'])
            response=self.llm.invoke(system_message)

            return {"blog":{"title":response.content}}
        
    def content_generation(self,state:BlogState):
        """
        CREATE THE CONTENT FOR THE BLOG.
        """
        if "topic" in state and state['topic']:
            system_prompt="""
                    You are an expert blog content writer. Use Markdown formatting. Generate
                    a detailed blog content with detailed breakdown for the {topic}. This tittle should be creative and SEO friendly.
                    """
            
            system_message=system_prompt.format(topic=state['topic'])
            response=self.llm.invoke(system_message)

            return {"blog":{"title":state['blog']['title'],"content":response.content}}
        

    def translation(self,state:BlogState):
        """
        Converts the genrated content to specified language.
        """

        translate_prompt = """
    You are a professional translator.

    Translate the following blog post into **{current_language}** and return only a valid JSON object with exactly two keys: "title" and "content".

    Strictly follow this format:
    {{
        "title": "Translated title here",
        "content": "Translated blog content here"
    }}

    - Do NOT include markdown styling (like **bold** or ## headers).
    - Avoid HTML.
    - Only return valid JSON.

    Original blog content:
    Content: {blog_content}
    """

        blog_content=state['blog']['content']
        message=[
            HumanMessage(translate_prompt.format(current_language=state['current_language'],blog_content=blog_content))
        ]
        translation_content=self.llm.with_structured_output(Blog).invoke(message)
        return {"blog": {
        "title": state['blog']['title'],
        "content": translation_content.content
        }}

    def route(self,state:BlogState):
        return {"current_language":state['current_language']}
    
    def route_decision(self,state:BlogState):
        """
        Route to the respective translation function.
        """
        if state["current_language"]=="hindi":
            return "hindi"
        elif state["current_language"]=="french":
            return "french"
        else:
            return state["currrent_language"]