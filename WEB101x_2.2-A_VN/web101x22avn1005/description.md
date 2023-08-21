When you used `grid-template-columns` and `grid-template-rows` to define the structure of a grid, you entered a value for each row or column you created.

Let's say you want a grid with 100 rows of the same height. It isn't very practical to insert 100 values individually. Fortunately, there's a better way - by using the `repeat` function to specify the number of times you want your column or row to be repeated, followed by a comma and the value you want to repeat.

Here's an example that would create the 100 row grid, each row at 50px tall.

```css
grid-template-rows: repeat(100, 50px);
```

You can also repeat multiple values with the repeat function and insert the function amongst other values when defining a grid structure. Here's what that looks like:

```css
grid-template-columns: repeat(2, 1fr 50px) 20px;
```

This translates to:

```css
grid-template-columns: 1fr 50px 1fr 50px 20px;
```

**Note:** The `1fr 50px` is repeated twice followed by 20px.

---

Use `repeat` to remove repetition from the `grid-template-columns` property.

---

Khi bạn sử dụng `grid-template-columns` và `grid-template-rows` để xác định cấu trúc của grid, bạn nhập một giá trị cho mỗi hàng hoặc cột bạn đã tạo.

Giả sử bạn muốn một lưới có 100 hàng có cùng chiều cao. Không thực tế lắm khi chèn 100 giá trị riêng lẻ. May mắn thay, có một cách tốt hơn - bằng cách sử dụng hàm `repeat` để chỉ định số lần bạn muốn cột hoặc hàng của mình được lặp lại, theo sau là dấu phẩy và giá trị bạn muốn lặp lại.

Đây là một ví dụ về việc tạo grid với 100 hàng, mỗi hàng cao 50px.

```css
grid-template-rows: repeat(100, 50px);
```

Bạn cũng có thể lặp lại nhiều giá trị bằng hàm repeat và chèn hàm vào giữa các giá trị khác khi xác định cấu trúc grid. Dưới đây là một ví dụ

```css
grid-template-columns: repeat(2, 1fr 50px) 20px;
```

Nó cũng được biểu diễn như sau

```css
grid-template-columns: 1fr 50px 1fr 50px 20px;
```

**Lưu ý:** `1fr 50px` được lặp lại hai lần, sau đó là 20px.

---

Sử dụng `repeat` để loại bỏ sự lặp lại khỏi thuộc tính `grid-template-columns`

```html
<style>
  .item1 {
    background: LightSkyBlue;
  }
  .item2 {
    background: LightSalmon;
  }
  .item3 {
    background: PaleTurquoise;
  }
  .item4 {
    background: LightPink;
  }
  .item5 {
    background: PaleGreen;
  }

  .container {
    font-size: 40px;
    min-height: 300px;
    width: 100%;
    background: LightGray;
    display: grid;
    /* Only change code below this line */

    grid-template-columns: 1fr 1fr 1fr;

    /* Only change code above this line */
    grid-template-rows: 1fr 1fr 1fr;
    grid-gap: 10px;
  }
</style>

<div class="container">
  <div class="item1">1</div>
  <div class="item2">2</div>
  <div class="item3">3</div>
  <div class="item4">4</div>
  <div class="item5">5</div>
</div>
```
