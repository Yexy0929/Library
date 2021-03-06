class Book:

    def __init__(self, name, author, price, status):
        self.name = name
        self.author = author
        self.price = price
        self.status = status


books_list = []


# 登记新书
def add_book():
    print('======登记新书======')
    name = input('请输入书名：')
    if len(name) <= 16:
        author = input('请输入作者：')
        try:
            price = int(input('请输入价格：'))
            if 0 < price < 5000:
                price = str(price)
                books = Book(name, author, price, '未借出')
                book = (books.name, books.author, books.price, books.status)
                books_list.append(book)
                save_data()
                print('新书登记成功：\n书名：《%s》 作者：%s 价格：%s' % (name, author, price))
            else:
                print('图书价格范围0-5000，请重新登记图书信息')
                add_book()
        except ValueError:
            print('价格只能输入数字，请重新输入')
            add_book()

    else:
        print('书名不能超过16个字，请重新输入')
        add_book()


# 查询所有图书
def query_book():
    print('当前图书馆有以下图书：')
    for x in range(0, len(books_list)):
        books = books_list[x]
        name = books[0]
        author = books[1]
        price = books[2]
        status = books[3]
        print('序号：%s 书名：《%s》 作者：%s 价格：%s 状态：%s' % (x, name, author, price, status))


# 借书
def borrow_book():
    print('======借书======')
    index = find_book()
    if books_list[index][3] == '未借出':
        print('序号：%s 书名：《%s》 作者：%s 价格：%s 状态：%s' % (
            index, books_list[index][0], books_list[index][1], books_list[index][2],
            books_list[index][3]))
        print('y：确认借书，n：重新输入，b：退出借书')
        choice = input('输入你的选项：')
        if choice == 'y':
            books_list[index][3] = '已借出'
            print('借书成功')
            save_data()
        elif choice == 'n':
            print('请重新输入书名借书')
            borrow_book()
        elif choice == 'b':
            manage_book()
        else:
            print('没有该选项')
    elif books_list[index][3] == '已借出':
        print('该图书已借出')


# 还书
def return_book():
    print('======还书======')
    index = find_book()
    if books_list[index][3] == '已借出':
        print('序号：%s 书名：《%s》 作者：%s 价格：%s 状态：%s' % (
            index, books_list[index][0], books_list[index][1], books_list[index][2],
            books_list[index][3]))
        print('y：确认还书，n：重新输入，b：退出还书')
        choice = input("输入你的选项：")
        if choice == 'y':
            books_list[index][3] = '未借出'
            print('还书成功')
            save_data()
        elif choice == 'n':
            print('请重新输入书名还书')
            return_book()
        elif choice == 'b':
            manage_book()
        else:
            print('没有该选项')
    elif books_list[index][3] == '未借出':
        print('该图书未借出')


# 根据书名查找图书
def find_book():
    name = input('请输入书名：')
    while True:
        rs = False
        for book in books_list:
            if book[0] == name:
                index = books_list.index(book, 0, len(books_list))
                return index
        if rs == False:
            name = input('未找到图书，请重输：')


# 保存数据到txt文件
def save_data():
    with open('book.txt', 'w', encoding='utf-8') as f:
        for book in books_list:
            s = ' '.join(book)
            f.write(s)
            f.write('\n')


# 读取txt文件里面的数据
def read_data():
    with open('book.txt', 'r', encoding='utf-8') as f:
        contents = f.readlines()
        for s in contents:
            s = s.strip('\n')
            books = s.split(' ')
            books_list.append(books)


# 选择操作
def manage_book():
    while True:
        print('============================')
        print('欢迎使用图书管理系统，请选择功能')
        print('1.查看图书')
        print('2.登记图书')
        print('3.借出图书')
        print('4.归还图书')
        print('5.退出系统')
        try:
            choose = int(input('请选择你的操作：'))
            if choose == 1:
                query_book()
            elif choose == 2:
                add_book()
            elif choose == 3:
                borrow_book()
            elif choose == 4:
                return_book()
            elif choose == 5:
                print('再见，欢迎下次使用')
                exit()
            else:
                print('您的选项不存在，请重新选择')
        except ValueError:
            print('只能输入数字')


if __name__ == '__main__':
    read_data()
    manage_book()
