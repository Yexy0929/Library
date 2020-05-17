class Library:

    def add_book(self):
        """登记新书"""
        pass

    def view_book(self):
        """查看图书馆所有书籍"""
        with open("book.txt", "r", encoding="utf-8") as f:
            book_list = f.read()
            print("当前图书馆有以下图书：")
            print(book_list)

    def borrow_book(self):
        """借书"""
        pass

    def return_book(self):
        """还书"""
        pass

    def logout(self):
        """退出系统"""
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
    if user_command == "1":
        Library().view_book()
    elif user_command == "2":
        print("请输入新图书名：")
    elif user_command == "3":
        print("请输入您要借的书名：")
    elif user_command == "4":
        print("请输入您要归还的图书名：")
    elif user_command == "5":
        print("退出成功，感谢您的使用！")
    else:
        print("序号不存在，请输入正确的序号选择功能。")


if __name__ == "__main__":
    command_list()
