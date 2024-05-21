real_url = str(input("Real link: ")).rstrip()
fake_url = str(input("Fake link: ")).rstrip()
response = str(input("Do you want to embed the fake link? (y/n): ")).rstrip()

embed = True if response == "y" else False

template = "[h](<{}>)[{}](<{}>)                         [⠀]({})"
if embed == False:
    print(template[:20].format(real_url, fake_url[1:], real_url))
else:
    print(template.format(real_url, fake_url[1:], real_url, fake_url))
