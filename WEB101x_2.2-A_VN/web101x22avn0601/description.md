Now let's put our Cat Photo App away for a little while and learn more about styling HTML.

You may have already noticed this, but all HTML elements are essentially little rectangles.

Three important properties control the space that surrounds each HTML element: `padding`, `border`, and `margin`.

An element's `padding` controls the amount of space between the element's content and its `border`.

Here, we can see that the blue box and the red box are nested within the yellow box. Note that the red box has more `padding` than the blue box.

When you increase the blue box's `padding`, it will increase the distance (`padding`) between the text and the border around it.

---

Change the `padding` of your blue box to match that of your red box.

---

Hãy tạm dừng ứng dụng Cat Photo và tìm hiểu thêm về HTML styling.

Bạn có thể đã nhận thấy điều này, về cơ bản tất cả các phần tử HTML là những hình chữ nhật nhỏ.

Ba thuộc tính quan trọng kiểm soát không gian bao quanh mỗi phần tử HTML là `padding`, `border` và `margin`.

`padding` là không gian giữa nội dung của phần tử và `border`.

Chúng ta có thể thấy rằng hộp màu xanh và hộp màu đỏ được lồng trong hộp màu vàng. Lưu ý rằng hộp màu đỏ có `padding` lớn hơn hộp màu xanh.

Khi bạn tăng `padding` hộp màu xanh lam , nó sẽ tăng khoảng cách ( `padding`) giữa văn bản và đường viền xung quanh nó.

Thay đổi `padding` hộp màu xanh lam sao cho bằng với hộp màu đỏ.

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
  }

  .blue-box {
    background-color: blue;
    color: #fff;
    padding: 10px;
  }
</style>
<h5 class="injected-text">margin</h5>

<div class="box yellow-box">
  <h5 class="box red-box">padding</h5>
  <h5 class="box blue-box">padding</h5>
</div>
```
