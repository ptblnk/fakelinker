# linkfaker
Generates markdown links with fake titles and embeds based on two user inputs. Designed for Discord.

# How does the fake embed work?
Discord does not filter out the unicode character U+2800, allowing you to make an invisible embed by using the following markdown: \[⠀](https://.../)

## Why did you make this?
Purely to make the process of making these links faster.

## Uses
For example, you can link to a Discord voice channel invite, and then embed a twitter post. When users click on that link, they will join the VC (assuming they are already in the server). 

## Example markdown
`[h](<https://twitter.com/>)[ttps://reddit.com/](<https://twitter.com/>)                         [⠀](https://reddit.com/)`

## Aren't you scared of malicious uses?
No. This is five lines of code. Anybody could make this. 
