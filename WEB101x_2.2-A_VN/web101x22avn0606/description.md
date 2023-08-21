Let's try this again, but with `margin` this time.

Instead of specifying an element's `margin-top`, `margin-right`, `margin-bottom`, and `margin-left` properties individually, you can specify them all in one line, like this:

```s
margin: 10px 20px 10px 20px;
```

These four values work like a clock: top, right, bottom, left, and will produce the exact same result as using the side-specific margin instructions.

---

Use Clockwise Notation to give the element with the `blue-box` class a margin of `40px` on its top and left side, but only `20px` on its bottom and right side.

---

Hãy thử lại lần nữa, nhưng với `margin` lần này.

Thay vì chỉ định riêng lẻ các thuộc tính `margin-top`, `margin-right`,`margin-bottom`,`margin-left` bạn có thể chỉ định tất cả chúng trong một dòng như sau:

```s
margin: 10px 20px 10px 20px;
```

Bốn giá trị top, right, bottom, left được đặt theo vị trí của chiều kim đồng hồ và sẽ tạo ra kết quả chính xác giống như khi sử dụng các thuộc tính riêng lẻ cho bốn mặt.

---

Sử dụng Ký hiệu chiều kim đồng hồ chỉ định cho phần tử có class `blue-box` một margin `40px` ở phía trên và bên trái, `20px` ở phía dưới và bên phải.

```html
<style>
  .injected-text {
    margin-bottom: -25px;
    text-align: center;
  }

  .box {
    border-style: solid;
    border-color: black;
    border-width: 5px;
    text-align: center;
  }

  .yellow-box {
    background-color: yellow;
    padding: 20px 40px 20px 40px;
  }

  .red-box {
    background-color: crimson;
    color: #fff;
    margin: 20px 40px 20px 40px;
  }

  .blue-box {
    background-color: blue;
    color: #fff;
  }
</style>
<h5 class="injected-text">margin</h5>

<div class="box yellow-box">
  <h5 class="box red-box">padding</h5>
  <h5 class="box blue-box">padding</h5>
</div>
```
