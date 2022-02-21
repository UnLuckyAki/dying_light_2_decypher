import re
keys_list = {'AAAAA':'a', 'AAAAB':'b',
             'AAABA':'c','AAABB':'d',
             'AABAA':'e','AABAB':'f',
             'AABBA':'g','AABBB':'h',
             'ABAAA':'(i-j)','ABAAB':'k',
             'ABABA':'l','ABABB':'m',
             'ABBAA':'n','ABBAB':'o',
             'ABBBA':'p','ABBBB':'q',
             'BAAAA':'r','BAAAB':'s',
             'BAABA':'t','BAABB':'(u-v)',
             'BABAA':'w','BABAB':'x',
             'BABBA':'y','BABBB':'z'}

text = "ABABBBAABBAAABBAAABBBABBA\nAABBABAAAAABBABBAABBABBAAAAABBBAAAB\nABBBAABBABAAABBBAABBAAAAAABABA\nBAABBABBABAAABBABBABABBAAAAAAAABBBAABBABBAAAAABAABAAAAA\nABBAABAABBABABABAABABAAAAABAAA\nAAABBBAABBAAAAAABBABAAABBABAAAABBAA\nBAAABAAABAAABBBAABAABAAABBAABABAAABAABAAABABB"
for line in text.split("\n"):
    string = []
    for letter in (re.findall('.....', line)):
        string.append(keys_list.get(letter))
    print(*string,sep='')
