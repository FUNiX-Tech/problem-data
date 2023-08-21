The `align-items` property is similar to `justify-content`. Recall that the `justify-content` property aligned flex items along the main axis. For rows, the main axis is a horizontal line and for columns it is a vertical line.

Flex containers also have a **cross axis** which is the opposite of the main axis. For rows, the cross axis is vertical and for columns, the cross axis is horizontal.

CSS offers the `align-items` property to align flex items along the cross axis. For a row, it tells CSS how to push the items in the entire row up or down within the container. And for a column, how to push all the items left or right within the container.

The different values available for `align-items` include:

- `flex-start:` aligns items to the start of the flex container. For rows, this aligns items to the top of the container. For columns, this aligns items to the left of the container.
- `flex-end:` aligns items to the end of the flex container. For rows, this aligns items to the bottom of the container. For columns, this aligns items to the right of the container.
- `center:` align items to the center. For rows, this vertically aligns items (equal space above and below the items). For columns, this horizontally aligns them (equal space to the left and right of the items).
- `stretch:` stretch the items to fill the flex container. For example, rows items are stretched to fill the flex container top-to-bottom. This is the default value if no `align-items` value is specified.
- `baseline:` align items to their baselines. Baseline is a text concept, think of it as the line that the letters sit on.

---

An example helps show this property in action. Add the CSS property `align-items` to the `#box-container` element, and give it a value of `center`.

**Bonus**
Try the other options for the `align-items` property in the code editor to see their differences. But note that a value of `center` is the only one that will pass this challenge.

---

Thuộc tính `align-items` tương tự như `justify-content`. `justify-content` căn chỉnh các flex item dọc theo main axis. Đối với hàng, main axis là đường nằm ngang và đối với cột là đường thẳng đứng.

Các flex container cũng có **cross axis** vuông góc với main axis. Đối với hàng, cross axis là dọc và đối với cột, cross axis là ngang.

CSS cung cấp thuộc tính `align-items` để căn chỉnh các flex item dọc theo cross axis. Đối với một hàng, nó cho CSS biết cách đẩy các item trong toàn bộ hàng lên hoặc xuống trong container. Và đối với một cột, làm thế nào để đẩy tất cả các mục sang trái hoặc phải trong container

Các giá trị khác có sẵn của `align-items`bao gồm:

- `flex-start:` căn chỉnh các item với điểm đầu của vùng chứa linh hoạt. Đối với các hàng, điều này sẽ căn chỉnh các item lên trên của container. Đối với các cột, điều này sẽ căn chỉnh các item sang bên trái của container.
- `flex-end:` căn chỉnh các item vào cuối flex container. Đối với các hàng, điều này sẽ căn chỉnh các item xuống dưới cùng của container. Đối với các cột, điều này sẽ căn chỉnh các item sang bên phải của container.
- `center:` căn chỉnh các item vào trung tâm. Đối với các hàng, điều này sẽ căn chỉnh các item theo chiều dọc (khoảng cách trên và dưới các item bằng nhau). Đối với các cột, điều này sẽ căn chỉnh chúng theo chiều ngang (không gian ở bên trái và bên phải của các item bằng nhau).
- `stretch:` kéo dài các item để lấp đầy flex container. Ví dụ: các item hàng được kéo dài để lấp đầy flex container từ trên xuống dưới. Đây là giá trị mặc định nếu không có giá trị `align-items` nào được chỉ định.
- `baseline:` sắp xếp các item theo đường cơ sở của chúng. Đường cơ sở là một khái niệm văn bản, nó là dòng mà các chữ cái nằm trên đó.

---

Ví dụ, thêm thuộc tính CSS `align-items`vào phần tử `#box-container` và đặt cho nó một giá trị là `center`

**Luyện tập thêm**
Hãy thử các tùy chọn khác cho thuộc tính `align-items` trong trình chỉnh sửa code để xem sự khác biệt của chúng. Nhưng lưu ý rằng giá trị `center` là giá trị duy nhất để hoàn thành thử thách này.

---

```html
<style>
  #box-container {
    background: gray;
    display: flex;
    height: 500px;
  }
  #box-1 {
    background-color: dodgerblue;
    width: 200px;
    font-size: 24px;
  }

  #box-2 {
    background-color: orangered;
    width: 200px;
    font-size: 18px;
  }
</style>

<div id="box-container">
  <div id="box-1"><p>Hello</p></div>
  <div id="box-2"><p>Goodbye</p></div>
</div>
```
