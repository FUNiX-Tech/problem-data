The opposite of `flex-shrink` is the `flex-grow` property. Recall that `flex-shrink` controls the size of the items when the container shrinks. The `flex-grow` property controls the size of items when the parent container expands.

Using a similar example from the last challenge, if one item has a `flex-grow` value of `1` and the other has a `flex-grow` value of `3`, the one with the value of `3` will grow three times as much as the other.

---

Add the CSS property `flex-grow` to both `#box-1` and `#box-2`. Give `#box-1` a value of `1` and `#box-2` a value of `2`.

---

Đối lập với `flex-shrink`là thuộc tính `flex-grow`. `flex-shrink` cho phép thu hẹp kích thước của các item khi container thu hẹp. Thuộc tính `flex-grow` mở rộng kích thước của các item khi container mở rộng.

Sử dụng một ví dụ tương tự thử thách trước, nếu một item có giá trị của `flex-grow` là `1` và item kia có giá trị của `flex-grow` là `3`, thì item có giá trị `3` sẽ mở rộng gấp ba lần so với item kia.

---

Thêm thuộc tính CSS `flex-grow` vào cả `#box-1` và `#box-2`. Cho `#box-1` một giá trị là `1` và `#box-2` một giá trị là `2`.

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
