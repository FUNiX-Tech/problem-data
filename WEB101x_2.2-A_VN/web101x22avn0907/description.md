Sometimes the flex items within a flex container do not fill all the space in the container. It is common to want to tell CSS how to align and space out the flex items a certain way. Fortunately, the `justify-content` property has several options to do this. But first, there is some important terminology to understand before reviewing those options.

[For more info about flex-box properties read here](https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/)

Recall that setting a flex container as a row places the flex items side-by-side from left-to-right. A flex container set as a column places the flex items in a vertical stack from top-to-bottom. For each, the direction the flex items are arranged is called the **main axis**. For a row, this is a horizontal line that cuts through each item. And for a column, the main axis is a vertical line through the items.

There are several options for how to space the flex items along the line that is the main axis. One of the most commonly used is `justify-content`: center;, which aligns all the flex items to the center inside the flex container. Other options include:

- `flex-start:` aligns items to the start of the flex container. For a row, this pushes the items to the left of the container. For a column, this pushes the items to the top of the container. This is the default alignment if no `justify-content` is specified.
- `flex-end:` aligns items to the end of the flex container. For a row, this pushes the items to the right of the container. For a column, this pushes the items to the bottom of the container.
- `space-between:` aligns items to the center of the main axis, with extra space placed between the items. The first and last items are pushed to the very edge of the flex container. For example, in a row the first item is against the left side of the container, the last item is against the right side of the container, then the remaining space is distributed evenly among the other items.
- `space-around:` similar to `space-between` but the first and last items are not locked to the edges of the container, the space is distributed around all the items with a half space on either end of the flex container.
- `space-evenly:` Distributes space evenly between the flex items with a full space at either end of the flex container.

An example helps show this property in action. Add the CSS property `justify-content` to the `#box-container` element, and give it a value of `center`.

---

**Bonus**
Try the other options for the `justify-content` property in the code editor to see their differences. But note that a value of `center` is the only one that will pass this challenge.

---

Đôi khi các flex item trong flex container không lấp đầy tất cả không gian trong container. Thông thường chúng ta phải chỉ định một cách thủ công để căn chỉnh và tạo khoảng trống cho các flex item. May mắn thay, `justify-content` có một số tùy chọn để làm điều này. Nhưng trước tiên, có một số thuật ngữ quan trọng cần hiểu trước khi xem xét các tùy chọn đó.

[Thông tin tham khảo về thuộc tính flex-box](https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/)

Chúng ta đã biết việc đặt một flex container dưới dạng một hàng sẽ đặt các flex iteam cạnh nhau từ trái sang phải. Một bộ flex item được đặt làm cột sẽ đặt các flex item trong một ngăn xếp thẳng đứng từ trên xuống dưới. Hướng sắp xếp các flex item được gọi là **main axis** . Đối với một hàng, nó là một đường ngang cắt qua từng item. đối với một cột, main axis là một đường thẳng đứng qua các item.

Có một số tùy chọn về cách sắp xếp các flex item dọc theo main axis. Một trong những cách phổ biến nhất được sử dụng là `justify-content`: center; căn chỉnh tất cả các flex item vào chính giữa flex container. Các tùy chọn khác bao gồm:

- `flex-start:` căn chỉnh các item về điểm đầu của flex container. Đối với một hàng, thao tác này sẽ đẩy các mục sang bên trái của container. Đối với một cột, điều này sẽ đẩy các mục lên đầu của container. Đây là căn chỉnh mặc định nếu không có `justify-content`chỉ định
- `flex-end:` căn chỉnh các item vào điểm cuối của container. Đối với một hàng, thao tác này sẽ đẩy các mục sang bên phải của container. Đối với một cột, điều này sẽ đẩy các mục xuống dưới cùng của container.
- `space-between:` căn chỉnh các item vào tâm của main axis, với khoảng trống được đặt giữa các item. Các item đầu tiên và cuối cùng được đẩy đến cạnh của flex container. Ví dụ: trong một hàng, item đầu tiên nằm ở phía bên trái của container, item cuối cùng nằm phía bên phải của container, sau đó không gian còn lại được phân bổ đồng đều cho các item khác.
- `space-around:` tương tự như `space-between` nhưng item đầu tiên và cuối cùng không bị khóa vào các cạnh của container, không gian được phân bổ xung quanh tất cả các item với một nửa không gian ở hai đầu của flex container
- `space-evenly:` Phân bổ không gian đồng đều giữa các flex item với khoảng trống đầy đủ ở hai đầu của flex container

---

Một ví dụ giúp hiển thị thuộc tính này. Thêm thuộc tính CSS `justify-content`vào phần tử `#box-container` và đặt cho nó một giá trị là `center`.

**Luyện tập thêm**
Hãy thử các tùy chọn khác cho thuộc tính `justify-content` trong trình chỉnh sửa code để xem sự khác biệt của chúng. Nhưng lưu ý rằng giá trị `center` là giá trị duy nhất để hoàn thành thử thách này.

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
    width: 25%;
    height: 100%;
  }

  #box-2 {
    background-color: orangered;
    width: 25%;
    height: 100%;
  }
</style>

<div id="box-container">
  <div id="box-1"></div>
  <div id="box-2"></div>
</div>
```
