import re               # re meaning regular expression we use search,remove,replace
import inflect             #1.convert numbers to words,2.make words plural or singular,3.handle "a"/"an" automatically,4.
def format_name(name):
    return ' '.join([w.capitalize() for w in name.strip().split()])
def format_phone(phone):
    digits=re.sub(r'\D+', '',phone)
    return f"+{digits[:2]} {digits[2:7]} {digits[7:]}"
def format_currency(amount,symbol='$'):                    #convert num to currency format
    return f"{symbol}{amount:,.2f}"
def number_to_words(n):
    p=inflect.engine()                                    # convert numbers to text(e.g 123-->one hundred twenty three")
    return p.number_to_words(n).replace(',','')
def slugify(text):
    return re.sub(r'[^a-z0-9]+','-', text.lower()).strip('-') #slugify means converts text to URl-safe slugs e.g "My Post!"-->"my-post"
