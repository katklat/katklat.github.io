import openai
import os
# pip install GitPython
from git import Repo
from pathlib import Path


PATH_TO_BLOG_REPO = Path("C:\\Users\\Giga\\OpenAI_Python_API_Bootcamp\\github_pages\\.git")

PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent

PATH_TO_CONTENT = PATH_TO_BLOG/"content"

PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)

def update_blog(commit_message='Update blog'):
    repo = Repo(PATH_TO_BLOG_REPO)
    repo.git.add(all=True)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

with open(PATH_TO_BLOG/"index.html", 'w') as f:
    f.write('automation test')

update_blog()