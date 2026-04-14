article = "ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation. ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the Apple Pie Master, this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time. At a press conference held at ACME Inc. headquarters in Springfield, the company CEO Jane Doe introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward. The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. This isn't just about saving time, it's about enhancing the baking experience and ensuring consistent results. The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one. Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection. ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. We want to cater to all taste preferences, from the traditional to the adventurous. The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc. partners. ACME Inc. is also proud of the Apple Pie Master environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. Sustainability is at the core of all our product designs. Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss. The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. It is like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich flavorful fillings. ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience. Looking ahead, ACME Inc. plans to expand its range of automated baking machines. The Apple Pie Master is just the beginning. We are exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking. The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices."


# ---- FUNCTION 1: Count a specific word ----
def count_specific_word(text, search_word):
    if text == "":
        return 0
    word_count = 0
    words = text.split()
    i = 0
    while i < len(words):
        clean_word = ""
        for char in words[i]:
            if char.isalpha():
                clean_word += char
        if clean_word.lower() == search_word.lower():
            word_count += 1
        i += 1
    return word_count


# ---- FUNCTION 2: Identify most common word ----
def identify_most_common_word(text):
    if text == "":
        return None
    word_list = []
    for word in text.split():
        clean_word = ""
        for char in word:
            if char.isalpha():
                clean_word += char
        if clean_word != "":
            word_list.append(clean_word.lower())
    most_common = ""
    highest_count = 0
    i = 0
    while i < len(word_list):
        count = 0
        for word in word_list:
            if word == word_list[i]:
                count += 1
        if count > highest_count:
            highest_count = count
            most_common = word_list[i]
        i += 1
    return most_common


# ---- FUNCTION 3: Calculate average word length ----
def calculate_average_word_length(text):
    if text == "":
        return 0
    words = text.split()
    total_length = 0
    i = 0
    while i < len(words):
        clean_word = ""
        for char in words[i]:
            if char.isalpha():
                clean_word += char
        total_length += len(clean_word)
        i += 1
    return round(total_length / len(words), 2)


# ---- FUNCTION 4: Count paragraphs ----
def count_paragraphs(text):
    if text == "":
        return 1
    paragraphs = text.split("\n\n")
    count = 0
    i = 0
    while i < len(paragraphs):
        if paragraphs[i].strip() != "":
            count += 1
        i += 1
    if count == 0:
        return 1
    return count


# ---- FUNCTION 5: Count sentences ----
def count_sentences(text):
    if text == "":
        return 1
    count = 0
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            count += 1
        i += 1
    if count == 0:
        return 1
    return count


# ---- TESTING ALL FUNCTIONS ----

print("===== count_specific_word =====")
print(count_specific_word("This is a test. This is only a test.", "test"))
print(count_specific_word("apple apple banana banana banana", "banana"))
print(count_specific_word("", "test"))

print("\n===== identify_most_common_word =====")
print(identify_most_common_word("This is a test. This is only a test."))
print(identify_most_common_word("apple apple banana banana banana"))
print(identify_most_common_word(""))

print("\n===== calculate_average_word_length =====")
print(calculate_average_word_length("This is a test."))
print(calculate_average_word_length("apple apple banana banana banana"))
print(calculate_average_word_length(""))

print("\n===== count_paragraphs =====")
print(count_paragraphs("This is a test.\n\nThis is only a test."))
print(count_paragraphs("apple apple banana\n\nbanana banana\n\nbanana"))
print(count_paragraphs(""))

print("\n===== count_sentences =====")
print(count_sentences("This is a test. This is only a test."))
print(count_sentences("Hello world. How are you? I'm fine, thanks."))
print(count_sentences(""))

print("\n===== ACME Article Analysis =====")
print("Word count for Apple:", count_specific_word(article, "Apple"))
print("Most common word:", identify_most_common_word(article))
print("Average word length:", calculate_average_word_length(article))
print("Number of paragraphs:", count_paragraphs(article))
print("Number of sentences:", count_sentences(article))