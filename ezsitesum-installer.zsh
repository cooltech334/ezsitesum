#!/bin/zsh
brew install zenity
brew install node
npm install axios cheerio @xenova/transformers
mkdir ezsitesum
brew install wget
wget https://raw.githubusercontent.com/cooltech334/ezsitesum/main/ezsitesum.js
mv ezsitesum.js ezsitesum/
zenity --info --text="Setup Finished! To run, head into the 'ezsitesum' directory and run 'node ezsitesum.js' in your terminal." --title="eztech - ezsitesum"
