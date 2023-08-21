The `order` property is used to tell CSS the order of how flex items appear in the flex container. By default, items will appear in the same order they come in the source HTML. The property takes numbers as values, and negative numbers can be used.

---

Add the CSS property `order` to both `#box-1` and `#box-2`. Give `#box-1` a value of `2` and give `#box-2` a value of `1`.

---

Thuộc tính `order` được sử dụng để CSS biết thứ tự xuất hiện của các flex item trong flex container. Theo mặc định, các item sẽ xuất hiện theo cùng thứ tự mà chúng có trong HTML . Thuộc tính order nhận số làm giá trị và có thể sử dụng số âm.

---

Thêm thuộc tính CSS ordervào cả `#box-1` và `#box-2`. Cho `#box-1` một giá trị là `2` và cho `#box-2`một giá trị là `1`.

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
