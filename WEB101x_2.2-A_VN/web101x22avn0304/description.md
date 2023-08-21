You can nest links within other text elements.

```html
<p>
  Here's a
  <a target="_blank" href="https://www.freecodecamp.org">
    link to www.freecodecamp.org</a
  >
  for you to follow.
</p>
```

Let's break down the example. Normal text is wrapped in the `p` element:

```html
<p>Here's a ... for you to follow.</p>
```

Next is the anchor element `<a>` (which requires a closing tag `</a>`):

```html
<a> ... </a>
```

`target` is an anchor tag attribute that specifies where to open the link. The value `\_blank` specifies to open the link in a new tab. The `href` is an anchor tag attribute that contains the URL address of the link:

```html
<a href="https://www.freecodecamp.org" target="_blank"> ... </a>
```

The text, `link to www.freecodecamp.org`, within the `a` element is called anchor text, and will display the link to click:

```html
<a href=" ... " target="...">link to freecodecamp.org</a>
```

The final output of the example will look like this:

Here's a [link to www.freecodecamp.org](https://www.freecodecamp.org) for you to follow.

Nest the existing `a` element within a new `p` element. Do not create a new anchor tag. The new paragraph should have text that says `View more cat photos`, where `cat photos` is a link, and the rest is plain text.

---

Bạn có thể lồng các liên kết trong các phần tử paragraph

```html
<p>
  Here's a
  <a target="_blank" href="https://www.freecodecamp.org">
    link to www.freecodecamp.org</a
  >
  for you to follow.
</p>
```

Văn bản được bao bọc trong phần tử `p`:

```html
<p>Here's a ... for you to follow.</p>
```

Tiếp theo là lồng vào một phần tử liên kết `<a>` và thẻ đóng `</a>`:

```html
<a> ... </a>
```

`target` là một attribute của thẻ liên kết, chỉ định nơi để mở liên kết. Giá trị `\_blank` chỉ định mở liên kết trong tab mới. `href` là attribute chứa địa chỉ URL của liên kết:

```html
<a href="https://www.freecodecamp.org" target="_blank"> ... </a>
```

Nội dung `link to www.freecodecamp.org` trong phần tử `a` được gọi là văn bản liên kết và sẽ hiển thị liên kết để nhấp vào:

```html
<a href=" ... " target="...">link to freecodecamp.org</a>
```

Kết quả của ví dụ sẽ như sau:

[Here's a link to www.freecodecamp.org for you to follow.](https://www.freecodecamp.org)

Lồng phần tử `a` vào phần tử `p` .Không tạo một thẻ liên kết mới. Nội dung của đoạn văn là `View more cat photos`, trong đó `cat photos` là liên kết và phần còn lại là văn bản thuần túy.

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
    sniff.
  </p>
  <p>
    Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere
    rip the couch sleep in the sink fluffy fur catnip scratched.
  </p>
</main>
```
