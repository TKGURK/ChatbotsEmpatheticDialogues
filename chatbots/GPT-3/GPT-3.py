import openai

def askGPT(text):
    openai.api_key = "XXXXXX"
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        temperature=0.0,
        max_tokens=1000
    )
    return print(response.choices[0].text)


def main():
    while True:
        print('GPT: Ask me a question\n')
        myQn = input()
        askGPT(myQn)
        print('\n')

main()


