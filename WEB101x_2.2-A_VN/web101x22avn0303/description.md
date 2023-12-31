`a` (anchor) elements can also be used to create internal links to jump to different sections within a webpage.

To create an internal link, you assign a link's `href` attribute to a hash symbol`#` plus the value of the `id` attribute for the element that you want to internally link to, usually further down the page. You then need to add the same `id` attribute to the element you are linking to. An `id` is an attribute that uniquely describes an element.

Below is an example of an internal anchor link and its target element:

```html
<a href="#contacts-header">Contacts</a>
...

<h2 id="contacts-header">Contacts</h2>
```

When users click the `Contacts` link, they'll be taken to the section of the webpage with the **Contacts** heading element.

---

Change your external link to an internal link by changing the `href` attribute to `#footer` and the text from `cat photos` to `Jump to Bottom`.

Remove the `target="\_blank"` attribute from the anchor tag since this causes the linked document to open in a new window tab.

Then add an `id` attribute with a value of `footer` to the `<footer>` element at the bottom of the page.

---

Các phần tử `a` ( anchor ) cũng có thể được sử dụng để tạo các liên kết nội bộ, chuyển đến các phần khác nhau trong một trang web.

Để tạo liên kết nội bộ, bạn gán href với ký hiệu `#` theo sau là giá trị của attribute `id` mà bạn muốn liên kết nội bộ, thường ở cuối trang. Với attribute `id` đã được chỉ định vào phần tử mà bạn đang liên kết. Attribute `id` là mô tả duy nhất của một phần tử.

Dưới đây là ví dụ về liên kết nội bộ với phần tử mục tiêu:

```html
<a href="#contacts-header">Contacts</a>
...

<h2 id="contacts-header">Contacts</h2>
```

Khi người dùng nhấp vào liên kết `Contacts`, nó sẽ đưa họ đến phần tử với tiêu đề **Contacts**

---

Thay đổi liên kết bên ngoài thành liên kết nội bộ bằng cách thay đổi attribute href thành `#footer` và nội dung hiển thị từ `cat photos` thành `Jump to Bottom`.

Xóa `target="\_blank"` khỏi thẻ liên kết vì điều này khiến tài liệu được mở trong tab cửa sổ mới.

Sau đó, thêm attribute `id` có giá trị `footer` vào phần tử `<footer>` ở cuối trang.

```html
<h2>CatPhotoApp</h2>
<main>
  <a href="https://www.freecatphotoapp.com" target="_blank">cat photos</a>

  <img
    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
    alt="A cute orange cat lying on its back."
  />

  <p>
    Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching
    attack your ankles chase the red dot, hairball run catnip eat the grass
    sniff. Purr jump eat the grass rip the couch scratched sunbathe, shed
    everywhere rip the couch sleep in the sink fluffy fur catnip scratched.
    Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching
    attack your ankles chase the red dot, hairball run catnip eat the grass
    sniff.
  </p>
  <p>
    Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere
    rip the couch sleep in the sink fluffy fur catnip scratched. Kitty ipsum
    dolor sit amet, shed everywhere shed everywhere stretching attack your
    ankles chase the red dot, hairball run catnip eat the grass sniff. Purr jump
    eat the grass rip the couch scratched sunbathe, shed everywhere rip the
    couch sleep in the sink fluffy fur catnip scratched.
  </p>
  <p>
    Meowwww loved it, hated it, loved it, hated it yet spill litter box, scratch
    at owner, destroy all furniture, especially couch or lay on arms while
    you're using the keyboard. Missing until dinner time toy mouse squeak roll
    over. With tail in the air lounge in doorway. Man running from cops stops to
    pet cats, goes to jail.
  </p>
  <p>
    Intently stare at the same spot poop in the plant pot but kitten is playing
    with dead mouse. Get video posted to internet for chasing red dot leave fur
    on owners clothes meow to be let out and mesmerizing birds leave fur on
    owners clothes or favor packaging over toy so purr for no reason. Meow to be
    let out play time intently sniff hand run outside as soon as door open yet
    destroy couch.
  </p>
</main>

<footer>Copyright Cat Photo App</footer>
```
