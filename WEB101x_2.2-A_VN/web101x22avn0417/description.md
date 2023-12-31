Instead of adjusting your overall background or the color of the text to make the foreground easily readable, you can add a `background-color` to the element holding the text you want to emphasize. This challenge uses `rgba()` instead of `hex` codes or normal `rgb()`.

```conf
rgba stands for:
r = red
g = green
b = blue
a = alpha/level of opacity
```

The RGB values can range from 0 to 255. The alpha value can range from 1, which is fully opaque or a solid color, to 0, which is fully transparent or clear. `rgba()` is great to use in this case, as it allows you to adjust the opacity. This means you don't have to completely block out the background.

You'll use `background-color: rgba(45, 45, 45, 0.1)` for this challenge. It produces a dark gray color that is nearly transparent given the low opacity value of 0.1.

---

To make the text stand out more, adjust the `background-color` of the `h4` element to the given `rgba()` value.

Also for the `h4`, remove the `height` property and add `padding` of 10px.

---

Thay vì điều chỉnh nền tổng thể hoặc màu của văn bản, bạn có thể thêm `background-color` vào phần tử chứa văn bản mà bạn muốn nhấn mạnh. Hãy sử dụng `rgba()` thay vì hex code hoặc `rgb()`.

```conf
rgba stands for:
r = red
g = green
b = blue
a = alpha/level of opacity
```

Các giá trị RGB có thể nằm trong khoảng từ 0 đến 255. Giá trị alpha có thể nằm từ 1, một màu đặc không trong suốt, đến 0, hoàn toàn trong suốt. `rgba()` nên được sử dụng trong trường hợp này, vì nó cho phép bạn điều chỉnh độ mờ, thậm chí không còn thấy background nữa.

Hãy sử dụng `background-color: rgba(45, 45, 45, 0.1)`. Nó tạo ra màu xám đậm gần như trong suốt với giá trị độ mờ là 0.1

---

Để làm cho văn bản nổi bật hơn, hãy điều chỉnh `background-color` phần tử `h4` theo `rgba()` với giá trị đã cho.

Tại `h4`, hãy xóa thuộc tính `height` và thêm `padding` 10px.

```html
<style>
  h4 {
    text-align: center;
    height: 25px;
  }
  p {
    text-align: justify;
  }
  .links {
    text-align: left;
    color: black;
  }
  .fullCard {
    width: 245px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 10px 5px;
    padding: 4px;
  }
  .cardContent {
    padding: 10px;
  }
  .cardText {
    margin-bottom: 30px;
  }
</style>
<div class="fullCard">
  <div class="cardContent">
    <div class="cardText">
      <h4>Alphabet</h4>
      <hr />
      <p>
        <em
          >Google was founded by Larry Page and Sergey Brin while they were
          <u>Ph.D. students</u> at <strong>Stanford University</strong>.</em
        >
      </p>
    </div>
    <div class="cardLinks">
      <a
        href="https://en.wikipedia.org/wiki/Larry_Page"
        target="_blank"
        class="links"
        >Larry Page</a
      ><br /><br />
      <a
        href="https://en.wikipedia.org/wiki/Sergey_Brin"
        target="_blank"
        class="links"
        >Sergey Brin</a
      >
    </div>
  </div>
</div>
```
