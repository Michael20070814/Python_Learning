### 1. 字典 (`Dictionary`) 与键值对

Python

```
headers = {
    "User-Agent": "Mozilla/5.0 ..."
}
```

- **语法复习**：用花括号 `{}` 包裹，里面是 `"Key": "Value"` 的结构。
- **工程意义**：这是 HTTP 协议的一部分。我们在构造一个“身份证明”。
  - **Key (`User-Agent`)**：告诉服务器“我是谁”。
  - **Value (`Mozilla...`)**：这是 Chrome 浏览器的身份证号。如果不写这个，你的代码就是“裸奔”的 Python 脚本，容易被网站拦截。

### 2. 异常处理 (`try...except`)

Python

```
try:
    # 尝试做某些危险的事
    response = requests.get(...)
except Exception as e:
    # 如果出事了，执行这里
    print(f"发生错误: {e}")
```

- **语法复习**：`try` 块里的代码如果报错，程序不会直接崩溃（Flash back），而是跳到 `except` 块里处理。
- **工程意义**：**健壮性**。网络请求是非常不稳定的（断网、服务器崩了、网址错了）。
  - **学生思维**：代码只要能跑通就行。
  - **工程思维**：必须假设代码随时会挂，所以要兜底，保证程序能活着报错，而不是直接消失。

### 3. 对象与方法调用 (`.` 点号操作符)

Python

```
response = requests.get(url, headers=headers)
# ...
soup = BeautifulSoup(response.text, "html.parser")
# ...
quotes = soup.find_all("div", class_="quote")
```

- **语法复习**：`对象.方法()`。这里的 `.` 可以理解为“的”。
  - `requests.get(...)`：调用 `requests` 工具箱里“的” `get` 功能。
  - `response.text`：获取 `response` 这个快递包裹里“的”文本内容（网页源码）。
- **BeautifulSoup 的核心逻辑**：
  - `soup` 变成了网页的**DOM树**（一种树状结构）。
  - `soup.find_all(...)`：在树上查找**所有**符合条件的树叶，返回一个列表（List）。
  - `class_="quote"`：注意这里有个下划线 `_`，因为 `class` 是 Python 的关键字（定义类用的），所以库的作者特意加个下划线来区分，这在 Python 库中很常见。

### 4. 循环与枚举 (`enumerate`) —— **高频考点**

Python

```
for index, quote in enumerate(quotes, 1):
```

- **语法复习**：普通的循环是 `for quote in quotes`。
- **进阶语法 (`enumerate`)**：
  - 如果你同时需要**数据本身 (`quote`)** 和它的**序号 (`index`)**，不要用 `i = i + 1` 这种笨办法。
  - `enumerate(列表, 1)` 会自动帮你计数，`1` 代表从 1 开始数（默认是从 0 开始）。
- **工程意义**：让代码更简洁、更 Pythonic（地道）。

### 5. f-string 字符串格式化

Python

```
print(f"{index}. {author} 说: {text}")
```

- **语法复习**：在字符串引号前加个 `f`，然后在里面用 `{}` 包裹变量。
- **工程意义**：这是 Python 3.6 以后推出的“大杀器”。
  - 以前的写法：`print("%d. %s 说: %s" % (index, author, text))` —— 像 C 语言，容易写错。
  - 现在的写法：所见即所得，极其易读。

### 6. 主程序入口

Python

```
if __name__ == "__main__":
    scrape_quotes()
```

- **语法复习**：这是一个固定写法。
- **工程意义**：
  - 当你在终端直接运行这个文件（`python scraper.py`）时，`__name__` 等于 `"__main__"`，代码会运行。
  - 如果你在这个文件里写了很多好用的函数，别的脚本想 `import` 这个文件来使用你的函数，这行代码下面的内容就**不会**自动运行。
  - **结论**：这是为了防止代码被引用时“乱跑”，是模块化开发的基石。