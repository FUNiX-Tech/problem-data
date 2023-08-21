Sometimes your HTML elements will receive multiple styles that conflict with one another.

For example, your `h1` element can't be both green and pink at the same time.

Let's see what happens when we create a class that makes text pink, then apply it to an element. Will our class override the `body` element's `color: green;` CSS property?

---

Create a CSS class called `pink-text` that gives an element the color pink.

Give your `h1` element the class of `pink-text`.

---

Đôi khi các phần tử HTML sẽ xuất hiện một số kiểu xung đột với nhau.

Ví dụ, phần tử `h1` không thể có cả màu xanh lá cây và màu hồng cùng một lúc.

Hãy xem điều gì sẽ xảy ra khi chúng ta tạo một class chỉ định văn bản có màu hồng, sau đó áp dụng nó cho một phần tử. Liệu class của chúng ta có ghi đè thuộc tính CSS c`olor: green;` của phần tử `body` không?

---

Tạo một class CSS có tên là `pink-text` chỉ định màu hồng cho phần tử.

Gán class `pink-text` này vào phần tử `h1`

```html
<style>
  body {
    background-color: black;
    font-family: monospace;
    color: green;
  }
</style>
<h1>Hello World!</h1>
```
