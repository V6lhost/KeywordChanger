def change(text, fword, cword):
    changed_text = str()
    text = " " + text + " "
    splitted_text = text.split(fword)
    for word in splitted_text:
        changed_text += word + cword
    lenght = len(changed_text)
    return((changed_text[1:])[:lenght-2])