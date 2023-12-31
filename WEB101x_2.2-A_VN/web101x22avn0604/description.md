Sometimes you will want to customize an element so that it has a different `margin` on each of its sides.

CSS allows you to control the `margin` of all four individual sides of an element with the `margin-top`, `margin-right`, `margin-bottom`, and `margin-left` properties.

---

Give the blue box a `margin` of `40px` on its top and left side, but only `20px` on its bottom and right side.

---

Đôi khi bạn sẽ muốn tùy chỉnh margintrên mỗi mặt của phần tử.

CSS cho phép bạn điều chỉnh `margin` cả bốn mặt riêng lẻ của một phần tử thông qua thuộc tính `margin-top`, `margin-right`,`margin-bottom`,`margin-left`.

---

Chỉ định hộp màu xanh lam có `margin` là `40px` phía trên và bên trái , `20px` ở phía dưới và bên phải.

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
    padding: 10px;
  }

  .red-box {
    background-color: crimson;
    color: #fff;
    margin-top: 40px;
    margin-right: 20px;
    margin-bottom: 20px;
    margin-left: 40px;
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
