import re
text=" Hellow team, our new product launch is planned for 24-03-2024 at 10:30 AM please contact marketingteam@gmail.com or support@startupAI using #productLaunch #Batmanram"
Hashtags=re.findall(r"#\+",text)
mentions=re.findall(r"@\w+",text)
emails=re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b",text)
urls=re.findall(r"https?:/^S+", text)
dates=re.findall(r"\b\d{1,2}^d{1,2}^d{4}\b",text)
tokens=re.findall(r"\b\w+\b",text)
print("Hashtags:", Hashtags)
print("Mentions:",mentions)
print("Emails:", emails)
print("URLs:",urls)
print("Dates:",dates)
print("Tokens:", tokens)
