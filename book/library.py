books_list = []


def add_book():
    print('*********添加图书**********')
    name = input('请输入书名：')
    if len(name) <= 16:
        author = input('请输入作者：')
        price = input('请输入价格：')
        status = input('请输入状态：')
        if status == '未借出' or '已借出':
            book = (name, author, price, status)
            books_list.append(book)
            save_data()
        else:
            print("状态只能是'已借出'或者'未借出'")
            add_book()
    else:
        print('书名不能超过16个字，请重新输入')
        add_book()


def query_book():
    print('当前图书馆有以下图书：')
    for x in range(0, len(books_list)):
        books = books_list[x]
        name = books[0]
        author = books[1]
        price = books[2]
        status = books[3]
        print('序号：%s 书名：%s 作者：%s 价格：%s 状态：%s' % (x, name, author, price, status))


def borrow_book():
    name = input('请输入书名：')
    for books in books_list:
        if books[0] == name and books[3] == '未借出':
            index = books_list.index(books, 0, len(books_list))
            print('序号：%s 书名：%s 作者：%s 价格：%s 状态：%s' % (
                index, books_list[index][0], books_list[index][1], books_list[index][2],
                books_list[index][3]))
            choice = input('请确认图书信息是否正确')
            if choice == 'y':
                books[3] = '已借出'
                print('借书成功')
                save_data()


def return_book():
    name = input('请输入书名：')
    for books in books_list:
        if books[0] == name and books[3] == '已借出':
            index = books_list.index(books, 0, len(books_list))
            print('序号：%s 书名：%s 作者：%s 价格：%s 状态：%s' % (
                index, books_list[index][0], books_list[index][1], books_list[index][2],
                books_list[index][3]))
            choice = input("请确认图书信息是否正确，输入'y'确认借书：")
            if choice == 'y':
                books[3] = '未借出'
                print('还书成功')
                save_data()


# 存储至本地文件
def save_data():
    file_handle = open('book.txt', 'w', encoding='utf-8')
    for book in books_list:
        # 把列表中的数据用空格分开拼接为一个字符串
        s = ' '.join(book)
        file_handle.write(s)
        file_handle.write('\n')
    file_handle.close()


def read_data():
    file_handle = open('book.txt', mode='r', encoding='utf-8')
    contents = file_handle.readlines()
    for msg in contents:
        msg = msg.strip('\n')
        books = msg.split(' ')
        books_list.append(books)
    file_handle.close()


if __name__ == '__main__':
    read_data()
    while True:
        print('****************图书管理系统*****************')
        print('*****************1.查看图书*****************')
        print('*****************2.登记图书*****************')
        print('*****************3.借出图书*****************')
        print('*****************4.归还图书*****************')
        print('*****************5.退出系统*****************')
        choose = int(input('请选择你的操作：'))
        if choose == 1:
            query_book()
        elif choose == 2:
            add_book()
        elif choose == 3:
            borrow_book()
        elif choose == 4:
            return_book()
            save_data()
        elif choose == 5:
            print('再见，欢迎下次使用')
            break
        else:
            print('您的选项不存在，请重新选择')
