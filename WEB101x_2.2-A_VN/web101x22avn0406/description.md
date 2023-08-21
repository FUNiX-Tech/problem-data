The `text-transform` property in CSS is used to change the appearance of text. It's a convenient way to make sure text on a webpage appears consistently, without having to change the text content of the actual HTML elements.

The following table shows how the different `text-transform` values change the example text "Transform me".

| Value        | Result                                                 |
| ------------ | ------------------------------------------------------ |
| `lowercase`  | "transform me"                                         |
| `uppercase`  | "TRANSFORM ME"                                         |
| `capitalize` | "Transform Me"                                         |
| `initial`    | Use the default value                                  |
| `inherit`    | Use the `text-transform` value from the parent element |
| `none`       | **Default:** Use the original text                     |

---

Transform the text of the `h4` to be uppercase using the `text-transform` property.

---

Thuộc tính `text-transform` trong CSS được sử dụng để thay đổi giao diện của văn bản. Điều này giúp bạn thay đổi giao diện văn bản trên trang web mà không cần phải thay đổi nội dung văn bản của các phần tử HTML .

Bảng sau đây cung cấp các giá trị `text-transform` khác nhau, giúp bạn quan sát được sự thay đổi của văn bản mẫu "Transform me" như thế nào.

| Value        | Result                                           |
| ------------ | ------------------------------------------------ |
| `lowercase`  | "transform me"                                   |
| `uppercase`  | "TRANSFORM ME"                                   |
| `capitalize` | "Transform Me"                                   |
| `initial`    | Sử dụng giá trị mặc định                         |
| `inherit`    | Sử dụng giá trị của text-transform từ phần tử mẹ |
| `none`       | **Mặc định:** Sử dụng văn bản gốc                |

---

Chuyển đổi văn bản của phần tử `h4` thành chữ hoa bằng cách sử dụng thuộc tính `text-transform`.

---

```html
<style>
  h4 {
    text-align: center;
    background-color: rgba(45, 45, 45, 0.1);
    padding: 10px;
    font-size: 27px;
  }
  p {
    text-align: justify;
  }
  .links {
    text-align: left;
    color: black;
    opacity: 0.7;
  }
  #thumbnail {
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
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
<div class="fullCard" id="thumbnail">
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
