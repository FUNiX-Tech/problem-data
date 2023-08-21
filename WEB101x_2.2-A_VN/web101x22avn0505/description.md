So we've proven that id declarations override class declarations, regardless of where they are declared in your `style` element CSS.

There are other ways that you can override CSS. Do you remember inline styles?

---

Use an inline style to try to make our `h1` element white. Remember, inline styles look like this:

```html
<h1 style="color: green;"></h1>
```

Leave the `blue-text` and `pink-text` classes on your `h1` element.

---

Chúng ta biết rằng các khai báo id sẽ ghi đè các khai báo class, bất kể chúng được khai báo ở đâu trong phần tử `style`

Có những cách khác mà bạn có thể ghi đè CSS. Bạn có nhớ inline styles không?

---

Sử dụng inline style để tạo kiểu cho phần tử `h1` có màu trắng.

```html
<h1 style="color: green;"></h1>
```

Đặt các class `blue-text` và `pink-text` trên phần tử `h1`

```html
<style>
  body {
    background-color: black;
    font-family: monospace;
    color: green;
  }
  #orange-text {
    color: orange;
  }
  .pink-text {
    color: pink;
  }
  .blue-text {
    color: blue;
  }
</style>
<h1 id="orange-text" class="pink-text blue-text">Hello World!</h1>
```
