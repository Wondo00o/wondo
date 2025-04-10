#5-25
s1 = "Kang Young Min"
s2 = "kang Young-Min"
s3 = "Kimdowon"
s4 = "kim Do-Won"

def process_string(s):
    cleaned = s.replace(" ", "").replace("-", "").upper()
    return cleaned

s1_clean = process_string(s1)
s2_clean = process_string(s2)
s3_clean = process_string(s3)
s4_clean = process_string(s4)

print("s1:", s1_clean, "| N의 개수:", s1_clean.count("N"))
print("s2:", s2_clean, "| N의 개수:", s2_clean.count("N"))
print("s3:", s3_clean, "| N의 개수:", s3_clean.count("N"))
print("s4:", s4_clean, "| N의 개수:", s4_clean.count("N"))
