def retConv(str):
    str =str.replace(":)","🙂")
    str =str.replace(":(","🙁")
    return str

def main():
    str_input = input()
    con_str= retConv(str_input)
    print(con_str)

main()