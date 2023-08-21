The `flex-basis` property specifies the initial size of the item before CSS makes adjustments with `flex-shrink` or `flex-grow`.

The units used by the `flex-basis` property are the same as other size properties (`px`, `em`, `%`, etc.). The value auto sizes items based on the content.

---

Set the initial size of the boxes using `flex-basis`. Add the CSS property `flex-basis` to both `#box-1` and `#box-2`. Give `#box-1` a value of `10em` and `#box-2` a value of `20em`.

---

Thuộc tính `flex-basis` chỉ định kích thước ban đầu của item trước khi CSS thực hiện điều chỉnh với `flex-shrink` hoặc `flex-grow`.

Các đơn vị được thuộc tính `flex-basis` sử dụng giống với các thuộc tính kích thước khác ( `px`, `em`, `%`,v.v. ). Giá trị auto sẽ điều chỉnh kích thước căn cứ theo nội dung.

---

Đặt kích thước ban đầu cho các hộp bằng cách sử dụng `flex-basis`. Thêm thuộc tính CSS `flex-basis` vào cả `#box-1` và `#box-2`. Cho `#box-1` một giá trị là `10em` và `#box-2` một giá trị là `20em`.

```html
<style>
  #box-container {
    display: flex;
    height: 500px;
  }

  #box-1 {
    background-color: dodgerblue;
    height: 200px;
  }

  #box-2 {
    background-color: orangered;
    height: 200px;
  }
</style>

<div id="box-container">
  <div id="box-1"></div>
  <div id="box-2"></div>
</div>
```
