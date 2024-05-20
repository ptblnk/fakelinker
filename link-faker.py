url = str(input("Link to send: ")).rstrip()
embed = str(input("Link to embed: ")).rstrip()

embed_cut = embed[1:]

template = "[h](<{}>)[{}](<{}>)                                                                                                                                                                                                                                          [⠀]({})"
print(template.format(url, embed_cut, url, embed))
