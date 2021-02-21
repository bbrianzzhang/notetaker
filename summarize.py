from summarizer import Summarizer

def get_notes(body):
    model = Summarizer()
    result = model(body, ratio=0.2)
    full = ''.join(result)
    return full

print(get_notes("tree play a significant role in reducing a rosian and moderating the climate they remove carbon dioxide from the atmosphere and store large quantity of carbon in your tissues trees and forests provide a habitat for many species of animals and plants tropical rainforests are among the most biodiverse trees provide shade and shelter timberpro construction fuel for cooking and heating and food for food as well as having many other uses the world worth of shrinking of trees are clear to increase amount of land available for agriculture because of the longest tivity long one and youthfulness please have always been revered and sacred gold in various cultures and they play a role in many of the world mythology"))
