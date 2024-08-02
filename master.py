import os
from huggingface_hub import HfApi, HfFolder, Repository

# Define your Hugging Face credentials
HF_TOKEN = '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'  # Replace with your Hugging Face token
HfFolder.save_token(HF_TOKEN)

# Define the repository you want to upload to
REPO_NAME = 'pranavajay/ImageGrondV0.1'  # Replace with your repository name
REPO_URL = f"https://huggingface.co/{REPO_NAME}"

# Define the local path to the folder you want to upload
LOCAL_FOLDER_PATH = 'ImageGrondV0.1/'  # Replace with the path to your local folder

# Initialize the repository
api = HfApi()
repo = Repository(
    local_dir=LOCAL_FOLDER_PATH,
    clone_from=REPO_URL,
    use_auth_token=HF_TOKEN,
    git_user='pranavajay',  # Replace with your GitHub username
    git_email='pranavajay74@gmail.com'  # Replace with your email
)

# Push the folder to the repository
repo.push_to_hub(commit_message="Initial commit")

print(f"Folder '{LOCAL_FOLDER_PATH}' has been uploaded to '{REPO_URL}'")
