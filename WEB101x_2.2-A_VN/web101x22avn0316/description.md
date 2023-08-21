You can use _radio buttons_ for questions where you want the user to only give you one answer out of multiple options.

Radio buttons are a type of `input`.

Each of your radio buttons can be nested within its own `label` element. By wrapping an `input` element inside of a `label` element it will automatically associate the radio button input with the label element surrounding it.

All related radio buttons should have the same `name` attribute to create a radio button group. By creating a radio group, selecting any single radio button will automatically deselect the other buttons within the same group ensuring only one answer is provided by the user.

Here's an example of a radio button:

```html
<label> <input type="radio" name="indoor-outdoor" />Indoor </label>
```

It is considered best practice to set a `for` attribute on the `label` element, with a value that matches the value of the `id` attribute of the `input` element. This allows assistive technologies to create a linked relationship between the label and the related `input` element. For example:

```html
<input id="indoor" type="radio" name="indoor-outdoor" />
<label for="indoor">Indoor</label>
```

We can also nest the `input` element within the `label` tags:

```html
<label for="indoor">
  <input id="indoor" type="radio" name="indoor-outdoor" />Indoor
</label>
```

---

Add a pair of radio buttons to your form, each nested in its own `label` element. One should have the option of `indoor` and the other should have the option of `outdoor`. Both should share the `name` attribute of `indoor-outdoor` to create a radio group.

---

Bạn có thể sử dụng các nút radio để chỉ cho phép người dùng chọn duy nhất một lựa chọn.

Các nút Radio là một kiểu `input`.

Mỗi nút radio có thể được lồng bên trong phần tử `label` của chính nó. Bằng cách đặt phần tử `input` nằm trong một phần tử `label`, nút radio sẽ tự động được liên kết với phần tử `label` bao xung quanh nó.

Tất cả các nút radio có liên quan với nhau phải có cùng một thuộc tính `name` để có thể tạo được một nhóm nút radio. Trong một nhóm nút radio, khi nhấn vào một nút radio thì lập tức các nút radio khác sẽ được bỏ chọn. Điều này giúp đảm bảo chỉ có duy nhất một nút trong nhóm đó được chọn mà thôi.

Dưới đây là ví dụ nút radio:

```html
<label> <input type="radio" name="indoor-outdoor" />Indoor </label>
```

Người ta khuyến cáo cách tốt nhất là thiết lập một thuộc tính `for` trong phần tử `label`. Phần tử này phải có giá trị trùng khớp với giá trị thuộc tính `id` của phần tử `input` để cho phép các công nghệ trợ năng tạo một mối quan hệ liên kết giữa nhãn và phần tử `input` có liên quan. Ví dụ:

```html
<input id="indoor" type="radio" name="indoor-outdoor" />
<label for="indoor">Indoor</label>
```

Ta có thể lồng phần tử `input` vào trong các thẻ `label`:

```html
<label for="indoor">
  <input id="indoor" type="radio" name="indoor-outdoor" />Indoor
</label>
```

---

Hãy thêm một cặp nút radio vào biểu mẫu. mỗi nút phải được lồng trong phần tử `label` của riêng nó. Một nút là `indoor` (trong nhà) và nút còn lại là `outdoor` (ngoài trời). Cả 2 nút phải có cùng một thuộc tính name là `indoor-outdoor` để tạo được một nhóm radio.

---

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
    <input type="text" placeholder="cat photo URL" required />
    <button type="submit">Submit</button>
  </form>
</main>
```
