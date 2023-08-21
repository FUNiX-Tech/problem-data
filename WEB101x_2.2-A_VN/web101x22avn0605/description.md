Instead of specifying an element's `padding-top`, `padding-right`, `padding-bottom`, and `padding-left` properties individually, you can specify them all in one line, like this:

```s
padding: 10px 20px 10px 20px;
```

These four values work like a clock: top, right, bottom, left, and will produce the exact same result as using the side-specific padding instructions.

---

Use Clockwise Notation to give the `.blue-box` class a `padding` of `40px` on its top and left side, but only `20px` on its bottom and right side.

---

Thay vì chỉ định riêng lẻ các thuộc tính `padding-top`, `padding-right`,`padding-bottom`,`padding-left`, bạn có thể chỉ định tất cả chúng trong một dòng như sau:

```s
padding: 10px 20px 10px 20px;
```

Bốn giá trị này đi theo chiều đồng hồ: trên cùng, phải, dưới cùng, trái và sẽ tạo ra kết quả chính xác giống như khi chỉ định riêng lẻ padding cho cả bốn mặt.

---

Sử dụng Ký hiệu chiều kim đồng hồ để chỉ định `padding` cho class `.blue-box` `40px` phía trên và bên trái, `20px` ở phía dưới và bên phải.

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
    padding: 20px 40px 20px 40px;
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
