An element's `margin` controls the amount of space between an element's `border` and surrounding elements.

Here, we can see that the blue box and the red box are nested within the yellow box. Note that the red box has a bigger `margin` than the blue box, making it appear smaller.

When you increase the blue box's `margin`, it will increase the distance between its border and surrounding elements.

---

Change the `margin` of the blue box to match that of the red box.

---

Lề của `margin` kiểm soát lượng không gian giữa `border` của phần tử và các phần tử xung quanh.

Ở đây, chúng ta có thể thấy rằng hộp màu xanh dương và hộp màu đỏ được lồng trong hộp màu vàng. Lưu ý rằng hộp màu đỏ có `margin` lớn hơn hộp màu xanh, điều này khiến cho nó trông có vẻ nhỏ hơn.

Khi bạn tăng `margin` của hộp màu xanh dương, khoảng cách giữa viền của nó và các phần tử xung quanh cũng tăng lên.

---

Hãy thay đổi `margin` của hộp màu xanh dương để khớp với hộp màu đỏ.

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
    padding: 20px;
    margin: 20px;
  }

  .blue-box {
    background-color: blue;
    color: #fff;
    padding: 20px;
    margin: 10px;
  }
</style>
<h5 class="injected-text">margin</h5>

<div class="box yellow-box">
  <h5 class="box red-box">padding</h5>
  <h5 class="box blue-box">padding</h5>
</div>
```
