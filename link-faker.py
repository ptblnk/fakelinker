real_url = str(input("Real link: ")).rstrip()
fake_url = str(input("Fake link: ")).rstrip()
response = str(input("Do you want to embed the fake link? (y/n): ")).rstrip()

embed = True if response == "y" else False

fake_url_cut = fake_url[1:]

template = "[h](<{}>)[{}](<{}>)                         [⠀]({})"
if embed == False:
    print(template[:20].format(real_url, fake_url_cut, real_url, fake_url))
else:
    print(template.format(real_url, fake_url_cut, real_url, fake_url))
