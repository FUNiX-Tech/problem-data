When a form gets submitted, the data is sent to the server and includes entries for the options selected. Inputs of type `radio` and `checkbox` report their values from the `value` attribute.

For example:

```html
<label for="indoor">
  <input id="indoor" value="indoor" type="radio" name="indoor-outdoor" />Indoor
</label>
<label for="outdoor">
  <input
    id="outdoor"
    value="outdoor"
    type="radio"
    name="indoor-outdoor"
  />Outdoor
</label>
```

Here, you have two `radio` inputs. When the user submits the form with the `indoor` option selected, the form data will include the line: `indoor-outdoor=indoor`. This is from the `name` and `value` attributes of the "indoor" input.

If you omit the `value` attribute, the submitted form data uses the default value, which is `on`. In this scenario, if the user clicked the "indoor" option and submitted the form, the resulting form data would be `indoor-outdoor=on`, which is not useful. So the `value` attribute needs to be set to something to identify the option.

---

Give each of the existing `radio` and `checkbox` inputs the `value` attribute. Do not create any new radio or checkbox elements. Use the input label text, in lowercase, as the value for the attribute.

---

Khi gửi biểu mẫu, dữ liệu sẽ được gửi đến một server, bao gồm cả các lựa chọn đã được chọn. Các input có kiểu `radio` và `checkbox` sẽ báo cáo giá trị của chúng thông qua thuộc tính value.

Ví dụ:

```html
<label for="indoor">
  <input id="indoor" value="indoor" type="radio" name="indoor-outdoor" />Indoor
</label>
<label for="outdoor">
  <input
    id="outdoor"
    value="outdoor"
    type="radio"
    name="indoor-outdoor"
  />Outdoor
</label>
```

Ở đây, bạn có 2 input `radio`. Khi ngươi dùng gửi biểu mẫu với lựa chọn `indoor`, dữ liệu biểu mẫu sẽ bao gồm dòng: `indoor-outdoor=indoor`. Dữ liệu này có được từ các thuộc tính `name` và `value` của input "indoor".

Nếu bỏ đi thuộc tính `value` thì dữ liệu biểu mẫu đã được gửi đi sẽ sử dụng giá trị mặc định là on. Trong trường hợp này, nếu người dùng nhấn vào lựa chọn "indoor" và gửi đi biểu mẫu thì dữ liệu biểu mẫu sẽ là `indoor-outdoor=on`, mà như vậy thì không hữu ích lắm. Do vậy, thuộc tính `value` cần phải được thiết lập cụ thể để xác định lựa chọn.

---

Thêm thuộc tính `value` cho các input `radio` và `checkbox` trong bài. Không tạo phần tử radio và checkbox mới. Sử dụng nhãn input viết thường làm giá trị thuộc tính.

```html
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"
    ><img
      src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
      alt="A cute orange cat lying on its back."
  /></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <form action="https://www.freecatphotoapp.com/submit-cat-photo">
    <label for="indoor"
      ><input id="indoor" type="radio" name="indoor-outdoor" /> Indoor</label
    >
    <label for="outdoor"
      ><input id="outdoor" type="radio" name="indoor-outdoor" /> Outdoor</label
    ><br />
    <label for="loving"
      ><input id="loving" type="checkbox" name="personality" /> Loving</label
    >
    <label for="lazy"
      ><input id="lazy" type="checkbox" name="personality" /> Lazy</label
    >
    <label for="energetic"
      ><input id="energetic" type="checkbox" name="personality" />
      Energetic</label
    ><br />
    <input type="text" placeholder="cat photo URL" required />
    <button type="submit">Submit</button>
  </form>
</main>
```
