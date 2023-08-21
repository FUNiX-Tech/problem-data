So far, all the properties in the challenges apply to the flex container (the parent of the flex items). However, there are several useful properties for the flex items.

The first is the `flex-shrink` property. When it's used, it allows an item to shrink if the flex container is too small. Items shrink when the width of the parent container is smaller than the combined widths of all the flex items within it.

The `flex-shrink` property takes numbers as values. The higher the number, the more it will shrink compared to the other items in the container. For example, if one item has a `flex-shrink` value of `1` and the other has a `flex-shrink` value of `3`, the one with the value of `3` will shrink three times as much as the other.

---

Add the CSS property `flex-shrink` to both `#box-1` and `#box-2`. Give `#box-1` a value of `1` and `#box-2` a value of `2`.

---

Cho đến nay, tất cả các thuộc tính trong các thử thách đều áp dụng cho flex container (phần tử mẹ của các flex item). Tuy nhiên, có một số thuộc tính áp dụng cho các flex item.

Đầu tiên là thuộc tính `flex-shrink`. Khi nó được sử dụng, nó cho phép item thu nhỏ lại nếu flex container quá nhỏ. Các item thu nhỏ khi chiều rộng của vùng chứa mẹ nhỏ hơn chiều rộng của tất cả các flex item bên trong nó cộng lại.

Thuộc tính `flex-shrink` nhận các số làm giá trị. Con số này càng cao thì nó sẽ càng bị thu hẹp lại so với các item khác trong container. Ví dụ, nếu một item có giá trị của `flex-shrink` là `1` và item kia có giá trị của `flex-shrink` là `3`, thì item có giá trị `3` sẽ co lại gấp ba lần so với item kia.

---

Thêm thuộc tính CSS `flex-shrink` vào cả `#box-1` và `#box-2`. Cho `#box-1` giá trị là `1` và `#box-2` giá trị là `2`.

```html
<style>
  #box-container {
    display: flex;
    height: 500px;
  }
  #box-1 {
    background-color: dodgerblue;
    width: 100%;
    height: 200px;
  }

  #box-2 {
    background-color: orangered;
    width: 100%;
    height: 200px;
  }
</style>

<div id="box-container">
  <div id="box-1"></div>
  <div id="box-2"></div>
</div>
```
