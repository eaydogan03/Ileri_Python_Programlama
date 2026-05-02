import re
#1
# text = "İletişim: 0505-123-45-67 veya 0505 123 45 67 veya destek@btk.gov.tr"

# phone_pattern=r"\d{4}[-\s]\d{3}[-\s]\d{2}[-\s]\d{2}"
# email_pattern=r"\w+@\w+.\w+.\w+"


# p_match=re.findall(phone_pattern,text)
# e_match=re.findall(email_pattern,text)

# print(p_match)
# print(e_match)

#2
data="Fiyat: $1,200.00 | İndirim:%10"
pattern=r"[^0-9.,]"

clean_data=re.sub(pattern,"",data)

print(clean_data)