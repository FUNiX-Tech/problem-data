Yay! We just proved that inline styles will override all the CSS declarations in your `style` element.

But wait. There's one last way to override CSS. This is the most powerful method of all. But before we do it, let's talk about why you would ever want to override CSS.

In many situations, you will use CSS libraries. These may accidentally override your own CSS. So when you absolutely need to be sure that an element has specific CSS, you can use `!important`.

Let's go all the way back to our `pink-text` class declaration. Remember that our `pink-text` class was overridden by subsequent class declarations, id declarations, and inline styles.

---

Let's add the keyword `!important` to your `pink-text` element's color declaration to make 100% sure that your `h1` element will be pink.

An example of how to do this is:

```css
color: red !important;
```

---

Chúng ta biết rằng các inline style sẽ ghi đè tất cả các khai báo CSS trong phần tử `style`

Có một cách cuối cùng để ghi đè CSS. Đây là phương pháp mạnh mẽ nhất trong tất cả các phương pháp mà chúng ta đã tìm hiểu qua. Nhưng trước khi làm điều đó, hãy nói về lý do tại sao bạn muốn ghi đè CSS.

Trong nhiều tình huống, bạn sẽ sử dụng thư viện CSS. Những điều này có thể vô tình ghi đè CSS của riêng bạn. Vì vậy, khi bạn cần chắc chắn rằng một phần tử có CSS ​​cụ thể mà bạn muốn chỉ định, bạn có thể sử dụng `!important`.

Quay trở lại khai báo class `pink-text`. Hãy nhớ rằng class `pink-text` đã bị ghi đè bởi các khai báo class, khai báo id và inline style

---

Hãy thêm từ khóa `!important` vào khai báo màu của phần tử văn bản để đảm bảo 100% rằng phần tử `h1` của bạn sẽ có màu hồng.

Ví dụ:

```css
color: red !important;
```

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
<h1 id="orange-text" class="pink-text blue-text" style="color: white">
  Hello World!
</h1>
```
