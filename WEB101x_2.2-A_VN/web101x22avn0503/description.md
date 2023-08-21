Our `pink-text` class overrode our `body` element's CSS declaration!

We just proved that our classes will override the `body` element's CSS. So the next logical question is, what can we do to override our `pink-text` class?

---

Create an additional CSS class called `blue-text` that gives an element the color blue. Make sure it's below your `pink-text` class declaration.

Apply the `blue-text` class to your `h1` element in addition to your `pink-text` class, and let's see which one wins.

Applying multiple class attributes to a HTML element is done with a space between them like this:

```conf
class="class1 class2"
```

**Note:** It doesn't matter which order the classes are listed in the HTML element.

However, the order of the `class` declarations in the `<style>` section is what is important. The second declaration will always take precedence over the first. Because `.blue-text` is declared second, it overrides the attributes of `.pink-text`.

---

Class `pink-text` ghi đè lên khai báo CSS của phần tử `body`!

Chúng ta biết rằng các class sẽ ghi đè CSS của phần tử `body`. Vậy, câu hỏi tiếp theo là chúng ta có thể làm gì để ghi đè class `pink-text`

---

Tạo một class CSS bổ sung được gọi là lớp `blue-text` chỉ định phần tử có màu xanh lam. Đảm bảo rằng nó nằm dưới khai báo của class `pink-text`

Áp dụng class `blue-text` cho phần tử h1 cùng với class `pink-text` và hãy xem cái nào được áp dụng.

Việc áp dụng nhiều thuộc tính class cho một phần tử HTML được triển khai với một khoảng trắng như sau

```conf
class="class1 class2"
```

**Lưu ý:** Không quan trọng thứ tự các class được liệt kê trong phần tử HTML.

Tuy nhiên, thứ tự khai báo `class` trong `<style>` mới là điều quan trọng. Khai báo thứ hai sẽ luôn được ưu tiên hơn khai báo đầu tiên. Bởi vì `.blue-text` được khai báo thứ hai, nó ghi đè các thuộc tính của `.pink-text`.

```html
<style>
  body {
    background-color: black;
    font-family: monospace;
    color: green;
  }
  .pink-text {
    color: pink;
  }
</style>
<h1 class="pink-text">Hello World!</h1>
```
