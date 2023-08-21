The final property for flex items is `align-self`. This property allows you to adjust each item's alignment individually, instead of setting them all at once. This is useful since other common adjustment techniques using the CSS properties `float`, `clear`, and `vertical-align` do not work on flex items.

`align-self` accepts the same values as `align-items` and will override any value set by the `align-items` property.

---

Add the CSS property `align-self` to both `#box-1` and `#box-2`. Give `#box-1` a value of `center` and give `#box-2` a value of `flex-end`.

---

Thuộc tính cuối cùng cho các flex item là `align-self`. Thuộc tính này cho phép bạn căn chỉnh từng item riêng lẻ, thay vì áp dụng cho tất cả item cùng một lúc. Điều này rất hữu ích vì các kỹ thuật như `float`,`clear`.`vertical-align` không hoạt động trên các flex item.

`align-self`chấp nhận các giá trị giống như `align-items`và sẽ ghi đè bất kỳ giá trị nào do thuộc tính `align-items` đặt.

---

Thêm thuộc tính CSS `align-self` vào cả `#box-1` và `#box-2`. Cho `#box-1`một giá trị của `center` và cho `#box-2` một giá trị `flex-end`.

```html
<style>
  #box-container {
    display: flex;
    height: 500px;
  }
  #box-1 {
    background-color: dodgerblue;

    height: 200px;
    width: 200px;
  }

  #box-2 {
    background-color: orangered;

    height: 200px;
    width: 200px;
  }
</style>

<div id="box-container">
  <div id="box-1"></div>
  <div id="box-2"></div>
</div>
```
