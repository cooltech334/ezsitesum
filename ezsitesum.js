// Import required modules
const axios = require("axios");
const cheerio = require("cheerio");
const { pipeline } = require("@xenova/transformers");

// Function to scrape the webpage and extract text
async function scrapeWebsite(url) {
    try {
        const response = await axios.get(url);

        if (response.status === 200) {
            const $ = cheerio.load(response.data);

            // Extract the text from <p> tags
            const paragraphs = $("p").map((i, el) => $(el).text()).get();
            const text = paragraphs.join(" ");

            return text;
        } else {
            throw new Error("Failed to retrieve the webpage.");
        }
    } catch (error) {
        console.error("Error fetching the webpage:", error.message);
        return null;
    }
}

// Function to summarize the text
async function summarizeText(text) {
    try {
        console.log("Loading summarization model...");
        const summarizer = await pipeline("summarization");

        console.log("Summarizing text...");
        const summary = await summarizer(text, { max_length: 150, min_length: 50 });

        return summary[0].summary_text;
    } catch (error) {
        console.error("Error during summarization:", error.message);
        return null;
    }
}

// Main function
async function main() {
    const readline = require("readline");
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    rl.question("Enter the URL of the website you want to summarize: ", async (url) => {
        console.log("Scraping website...");

        const text = await scrapeWebsite(url);
        if (text) {
            const summary = await summarizeText(text);
            if (summary) {
                console.log("\nSummary of the webpage:");
                console.log(summary);
            } else {
                console.error("Summarization failed.");
            }
        } else {
            console.error("Failed to scrape the website.");
        }

        rl.close();
    });
}

// Run the script
main();
