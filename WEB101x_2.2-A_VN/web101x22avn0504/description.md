We just proved that browsers read CSS from top to bottom in order of their declaration. That means that, in the event of a conflict, the browser will use whichever CSS declaration came last. Notice that if we even had put `blue-text` before `pink-text` in our `h1` element's classes, it would still look at the declaration order and not the order of their use!

But we're not done yet. There are other ways that you can override CSS. Do you remember id attributes?

Let's override your `pink-text` and `blue-text` classes, and make your `h1` element orange, by giving the `h1` element an id and then styling that id.

---

Give your `h1` element the `id` attribute of `orange-text`. Remember, id styles look like this:

```html
<h1 id="orange-text"></h1>
```

Leave the `blue-text` and `pink-text` classes on your `h1` element.

Create a CSS declaration for your `orange-text` id in your `style` element. Here's an example of what this looks like:

```css
#brown-text {
  color: brown;
}
```

**Note:** It doesn't matter whether you declare this CSS above or below `pink-text` class, since the `id` attribute will always take precedence.

---

Chúng ta biết rằng các trình duyệt đọc CSS từ trên xuống dưới theo thứ tự khai báo của chúng. Điều đó có nghĩa là, trong trường hợp xảy ra xung đột, trình duyệt sẽ sử dụng khai báo CSS đến sau. Lưu ý rằng nếu chúng ta đã đặt `blue-text` trước `pink-text` trong `h1`, nó vẫn sẽ xem xét thứ tự khai báo.

Tuy nhiên, vẫn còn nhiều cách khác mà bạn có thể ghi đè CSS. Bạn có nhớ attribute `id` không?

Hãy ghi đè class `pink-text` và `blue-text` , làm cho phần tử của bạn có màu cam, bằng cách đặt cho phần tử `h1` đó một id và sau đó tạo kiểu cho id đó.

Gán cho phần tử `h1` attribute `id` là `orange-text`.

```html
<h1 id="orange-text"></h1>
```

Đặt các class `blue-text` và `pink-text` trên phần tử `h1`

Tạo một khai báo CSS cho id `orange-text` trong phần tử `style`. Dưới đây là một ví dụ

```css
#brown-text {
  color: brown;
}
```

**Lưu ý:** Không quan trọng bạn khai báo CSS này ở trên hay dưới class `pink-text`, attribute `id` sẽ luôn được ưu tiên.

---

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
  .blue-text {
    color: blue;
  }
</style>
<h1 class="pink-text blue-text">Hello World!</h1>
```
