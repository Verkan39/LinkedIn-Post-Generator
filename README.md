# Gen-AI powered LinkedIn Post Generator

The core idea behind this project is to help any LinkedIn Influencer by producing posts it can use. We use their previous posts, analyze them with AI tools, further using these researched posts to generate new posts based on the topic and the interest author wants to write today.



#### Tech Stack 

```
Langchain, Groq, Python, Streamlit, Pandas
```



#### User Interface 

![Interface](/home/vedanshu/Documents/LinkedIn Post Generator/assets/Ui.png)



### Set-Up

1. Create an API key on https://groq.com/ and save it in .env file with label GROQ_API_KEY. 

2. Install dependencies using

   ```bash
   pip install -r requirement.txt
   ```

3. Run the system using

   ```bash
   streamlit run main.py
   ```



If you are using a Linux system, you might face difficulty downloading dependencies, you can turn on a virtual environment using the following commands, then configure your python interpretor to the virtual environment and run the streamline command

```bash
python3 -m venv .venv
source .venv/bin/activate
```

