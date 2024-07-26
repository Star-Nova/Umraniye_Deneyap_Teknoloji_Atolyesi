from openai import OpenAI

client = OpenAI(api_key ="You API KEY")

messages = [{"role":"user",
             "content":""}]

while True:
    prompt = input("Kullanıcı: prompt giriniz / bitirmek için (q) iletiniz): ")
    if prompt == "q" or prompt == "Q" :
        break
    else:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[ {"role": "user",
                        "content": prompt} ] )

        print(completion.choices[0].message)
        messages.append({"role": "assistant",
                         "content": completion.choices[0].message})