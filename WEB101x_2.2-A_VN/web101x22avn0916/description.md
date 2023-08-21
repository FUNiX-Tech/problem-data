There is a shortcut available to set several flex properties at once. The `flex-grow`, `flex-shrink`, and `flex-basis` properties can all be set together by using the flex property.

For example, `flex: 1 0 10px;` will set the item to `flex-grow: 1;`, `flex-shrink: 0;`, and `flex-basis: 10px;`.

The default property settings are `flex: 0 1 auto;`.

---

Add the CSS property flex to both `#box-1` and `#box-2`. Give `#box-1` the values so its flex-grow is` 2`, its `flex-shrink` is `2`, and its `flex-basis` is `150px`. Give `#box-2` the values so its `flex-grow` is `1`, its `flex-shrink` is `1`, and its `flex-basis` is `150px`.

These values will cause `#box-1` to grow to fill the extra space at twice the rate of `#box-2` when the container is greater than 300px and shrink at twice the rate of `#box-2` when the container is less than 300px. 300px is the combined size of the `flex-basis` values of the two boxes.

---

Có một cách để thiết lập một số thuộc tính flex cùng một lúc. Tất cả các thuộc tính `flex-grow`, `flex-shrink` và f`lex-basis` đều có thể được đặt cùng nhau bằng cách sử dụng thuộc tính flex.

Ví dụ: `flex: 1 0 10px;` sẽ đặt mục thành `flex-grow: 1;`, `flex-shrink: 0;`và `flex-basis: 10px;`

Các cài đặt thuộc tính mặc định là `flex: 0 1 auto;`.

---

Thêm thuộc tính CSS flexvào cả `#box-1`và `#box-2`. Chỉ định cho `#box-1`với giá trị `flex-grow` là `2`, giá trị `flex-shrink` là `2` và giá trị `flex-basis` là `150px`. Chỉ định `#box-2` với giá trị `flex-grow` là `1`, giá trị `flex-shrink` là `1` và giá trị `flex-basis` là `150px`.

Các giá trị này sẽ tăng `#box-1` lên để lấp đầy không gian thừa với tỉ lệ gấp đôi `#box-2` khi container lớn hơn 300px và thu nhỏ với tỉ lệ gấp đôi `#box-2` khi container nhỏ hơn 300px. 300px là kích thước kết hợp của các giá trị `flex-basis` của hai hộp.

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
