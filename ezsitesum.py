print(' If you want to expand on this, please give me credit. -cooltech334 ')
print("""                    ____            __   __________ __ __
  _________  ____  / / /____  _____/ /_ |__  /__  // // /
 / ___/ __ \/ __ \/ / __/ _ \/ ___/ __ \ /_ < /_ </ // /_
/ /__/ /_/ / /_/ / / /_/  __/ /__/ / / /__/ /__/ /__  __/
\___/\____/\____/_/\__/\___/\___/_/ /_/____/____/  /_/   
                                                          """)
print('First load may take a while...')
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Function to scrape the webpage and extract text (using bs4, what are we, savages?)
def scrape_website(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the text from paragraphs or any other tag
        paragraphs = soup.find_all('p')  # You can adjust this to extract other relevant content
        text = ' '.join([para.get_text() for para in paragraphs])
        
        return text
    else:
        return "Failed to retrieve the webpage."

# Function to summarize the text
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    
    return summary[0]['summary_text']

# Main function to scrape and summarize
def main():
    url = input("Enter the URL of the website you want to summarize: ")
    
    # Scrape the website
    text = scrape_website(url)
    
    if text != "Failed to retrieve the webpage.":
        # Summarize the extracted text
        summary = summarize_text(text)
        print("\nSummary of the webpage:")
        print(summary)
    else:
        print("Error: Could not retrieve the website content.")

# Run the script
if __name__ == "__main__":
    main()
