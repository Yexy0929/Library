def view_book():
    with open('book.txt', 'r', encoding='UTF-8') as f:
        book = f.read()
        print(book)

def add_book():
    name = input("请输入书名：")
    author = input("请输入作者：")
    price = input("请输入价格：")
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write('\n《' + name + '》,'+ '作者：' + author + ',' + price + ',' + '状态：未借出')

def borrow_book():
    pass

def return_book():
    pass

def command_list():
    # 用户选择功能
    user_command = input("""
        欢迎使用图书馆管理系统,请输入序号选择功能:
        1. 查看图书
        2. 登记图书
        3. 借出图书
        4. 归还图书
        5. 退出系统
        """
                         )
    while True:
        if user_command == "1":
            view_book()
            break
        elif user_command == "2":
            add_book()
            break
        elif user_command == "3":
            print("请输入您要借的书名：")
            break
        elif user_command == "4":
            print("请输入您要归还的图书名：")
            break
        elif user_command == "5":
            print("退出成功，感谢您的使用！")
            break
        else:
            print("序号不存在，请输入正确的序号选择功能。")
            break


if __name__ == "__main__":
    command_list()
