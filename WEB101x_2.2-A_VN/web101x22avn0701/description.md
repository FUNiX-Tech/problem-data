CSS treats each HTML element as its own box, which is usually referred to as the CSS Box Model. Block-level items automatically start on a new line (think headings, paragraphs, and divs) while inline items sit within surrounding content (like images or spans). The default layout of elements in this way is called the normal flow of a document, but CSS offers the position property to override it.

When the position of an element is set to `relative`, it allows you to specify how CSS should move it relative to its current position in the normal flow of the page. It pairs with the CSS offset properties of `left` or `right`, and `top` or `bottom`. These say how many pixels, percentages, or ems to move the item away from where it is normally positioned. The following example moves the paragraph 10 pixels away from the bottom:

```html
p { position: relative; bottom: 10px; }
```

Changing an element's position to relative does not remove it from the normal flow - other elements around it still behave as if that item were in its default position.

**Note:** Positioning gives you a lot of flexibility and power over the visual layout of a page. It's good to remember that no matter the position of elements, the underlying HTML markup should be organized and make sense when read from top to bottom. This is how users with visual impairments (who rely on assistive devices like screen readers) access your content.

---

Change the `position` of the `h2` to `relative`, and use a CSS offset to move it 15 pixels away from the `top` of where it sits in the normal flow. Notice there is no impact on the positions of the surrounding h1 and p elements.

---

CSS coi mỗi phần tử HTML như một hộp riêng của nó, thường được gọi là CSS Box Model . Các phần tử block-level (heading, paragraph, div) sẽ tự động bắt đầu trên một dòng mới. Trong khi các phần tử inline nằm trên một dòng (như images hoặc span). Bố cục mặc định của các phần tử này được gọi là normal flow của tài liệu, nhưng CSS cung cấp một số thuộc tính position để ghi đè nó.

Khi vị trí của một phần tử được đặt thành `relative`, nó cho phép phần tử đó di chuyển so với vị trí hiện tại trong normal flow của trang. Chúng ta chỉ định vị trí mới thông qua các thuộc tính `left`, `right`, `top` hoặc `bottom`. Chúng cho biết cần di chuyển phần tử này bao nhiêu pixel, tỷ lệ phần trăm hoặc ems ra khỏi vị trí thường được đặt. Ví dụ, di chuyển paragraph lên 10 pixel so với phần dưới cùng:

```html
p { position: relative; bottom: 10px; }
```

Thay đổi position của một phần tử thành relative không loại bỏ nó khỏi normal flow - các phần tử khác xung quanh nó vẫn hoạt động như thể mục đó ở vị trí mặc định của nó.

**Lưu ý:** Việc định vị mang lại cho bạn nhiều sự linh hoạt đối với bố cục trực quan của một trang. Lưu ý rằng bất kể vị trí của các phần tử ở đâu, HTML phải được tổ chức một cách có cấu trúc và ý nghĩa khi đọc từ trên xuống dưới. Đây là cách người dùng khiếm thị (những người dựa vào các thiết bị hỗ trợ như trình đọc màn hình) truy cập nội dung của bạn.

---

Thay đổi giá trị `position` của `h2` thành `relative` sử dụng CSS offset để di chuyển nó ra xa 15 pixel so với `top`, vị trí mà nó nằm trong normal flow. Chú ý rằng không có tác động đến vị trí của các phần tử h1 và p xung quanh.

```html
<style>
  h2 {
  }
</style>
<body>
  <h1>On Being Well-Positioned</h1>
  <h2>Move me!</h2>
  <p>I still think the h2 is where it normally sits.</p>
</body>
```
