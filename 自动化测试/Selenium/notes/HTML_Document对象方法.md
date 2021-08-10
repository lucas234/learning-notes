## Document 查找对象方法

| 方法                                                         | 描述                                 |
| ------------------------------------------------------------ | ------------------------------------ |
| document.getElementById(*id*)                                | 返回对拥有指定 id 的第一个对象的引用 |
| document.getElementsByTagName(*name*)                        | 返回带有指定 tag 名称的对象集合      |
| document.getElementsByClassName(*name*)                      | 返回带有指定 class 标签名的对象集合  |
| document.getElementsByName(*name*)                           | 返回带有指定 name 标签名的对象集合   |
| document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue | 通过xpath获取对象                    |
| document.querySelector(*CSS selectors*)                      | 通过css获取对象，如果多个选择第一个  |
| document.querySelectorAll(*CSS selectors*)                   | 通过css获取对象集合                  |



## Changing HTML Elements

| Property                                   | Description                                   |
| :----------------------------------------- | :-------------------------------------------- |
| *element*.innerHTML = *new html content*   | Change the inner HTML of an element           |
| *element*.*attribute = new value*          | Change the attribute value of an HTML element |
| *element*.style.*property = new style*     | Change the style of an HTML element           |
| Method                                     | Description                                   |
| *element*.setAttribute*(attribute, value)* | Change the attribute value of an HTML element |



## Element 对象的属性和方法

| 属性 / 方法                                                  | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [element.accessKey](https://www.w3school.com.cn/jsref/prop_html_accesskey.asp) | 设置或返回元素的快捷键。                                     |
| [element.appendChild()](https://www.w3school.com.cn/jsref/met_node_appendchild.asp) | 向元素添加新的子节点，作为最后一个子节点。                   |
| [element.attributes](https://www.w3school.com.cn/jsref/prop_node_attributes.asp) | 返回元素属性的 NamedNodeMap。                                |
| [element.childNodes](https://www.w3school.com.cn/jsref/prop_node_childnodes.asp) | 返回元素子节点的 NodeList。                                  |
| [element.className](https://www.w3school.com.cn/jsref/prop_html_classname.asp) | 设置或返回元素的 class 属性。                                |
| element.clientHeight                                         | 返回元素的可见高度。                                         |
| element.clientWidth                                          | 返回元素的可见宽度。                                         |
| [element.cloneNode()](https://www.w3school.com.cn/jsref/met_node_clonenode.asp) | 克隆元素。                                                   |
| [element.compareDocumentPosition()](https://www.w3school.com.cn/jsref/met_node_comparedocumentposition.asp) | 比较两个元素的文档位置。                                     |
| [element.contentEditable](https://www.w3school.com.cn/jsref/prop_html_contenteditable.asp) | 设置或返回元素的文本方向。                                   |
| [element.dir](https://www.w3school.com.cn/jsref/prop_html_dir.asp) | 设置或返回元素的内容是否可编辑。                             |
| [element.firstChild](https://www.w3school.com.cn/jsref/prop_node_firstchild.asp) | 返回元素的首个子。                                           |
| [element.getAttribute()](https://www.w3school.com.cn/jsref/met_element_getattribute.asp) | 返回元素节点的指定属性值。                                   |
| [element.getAttributeNode()](https://www.w3school.com.cn/jsref/met_element_getattributenode.asp) | 返回指定的属性节点。                                         |
| [element.getElementsByTagName()](https://www.w3school.com.cn/jsref/met_element_getelementsbytagname.asp) | 返回拥有指定标签名的所有子元素的集合。                       |
| element.getFeature()                                         | 返回实现了指定特性的 API 的某个对象。                        |
| element.getUserData()                                        | 返回关联元素上键的对象。                                     |
| [element.hasAttribute()](https://www.w3school.com.cn/jsref/met_element_hasattribute.asp) | 如果元素拥有指定属性，则返回true，否则返回 false。           |
| [element.hasAttributes()](https://www.w3school.com.cn/jsref/met_node_hasattributes.asp) | 如果元素拥有属性，则返回 true，否则返回 false。              |
| [element.hasChildNodes()](https://www.w3school.com.cn/jsref/met_node_haschildnodes.asp) | 如果元素拥有子节点，则返回 true，否则 false。                |
| [element.id](https://www.w3school.com.cn/jsref/prop_html_id.asp) | 设置或返回元素的 id。                                        |
| [element.innerHTML](https://www.w3school.com.cn/jsref/prop_html_innerhtml.asp) | 设置或返回元素的内容。                                       |
| [element.insertBefore()](https://www.w3school.com.cn/jsref/met_node_insertbefore.asp) | 在指定的已有的子节点之前插入新节点。                         |
| [element.isContentEditable](https://www.w3school.com.cn/jsref/prop_html_iscontenteditable.asp) | 设置或返回元素的内容。                                       |
| [element.isDefaultNamespace()](https://www.w3school.com.cn/jsref/met_node_isdefaultnamespace.asp) | 如果指定的 namespaceURI 是默认的，则返回 true，否则返回 false。 |
| [element.isEqualNode()](https://www.w3school.com.cn/jsref/met_node_isequalnode.asp) | 检查两个元素是否相等。                                       |
| [element.isSameNode()](https://www.w3school.com.cn/jsref/met_node_issamenode.asp) | 检查两个元素是否是相同的节点。                               |
| [element.isSupported()](https://www.w3school.com.cn/jsref/met_node_issupported.asp) | 如果元素支持指定特性，则返回 true。                          |
| [element.lang](https://www.w3school.com.cn/jsref/prop_html_lang.asp) | 设置或返回元素的语言代码。                                   |
| [element.lastChild](https://www.w3school.com.cn/jsref/prop_node_lastchild.asp) | 返回元素的最后一个子元素。                                   |
| [element.namespaceURI](https://www.w3school.com.cn/jsref/prop_node_namespaceuri.asp) | 返回元素的 namespace URI。                                   |
| [element.nextSibling](https://www.w3school.com.cn/jsref/prop_node_nextsibling.asp) | 返回位于相同节点树层级的下一个节点。                         |
| [element.nodeName](https://www.w3school.com.cn/jsref/prop_node_nodename.asp) | 返回元素的名称。                                             |
| [element.nodeType](https://www.w3school.com.cn/jsref/prop_node_nodetype.asp) | 返回元素的节点类型。                                         |
| [element.nodeValue](https://www.w3school.com.cn/jsref/prop_node_nodevalue.asp) | 设置或返回元素值。                                           |
| [element.normalize()](https://www.w3school.com.cn/jsref/met_node_normalize.asp) | 合并元素中相邻的文本节点，并移除空的文本节点。               |
| element.offsetHeight                                         | 返回元素的高度。                                             |
| element.offsetWidth                                          | 返回元素的宽度。                                             |
| element.offsetLeft                                           | 返回元素的水平偏移位置。                                     |
| element.offsetParent                                         | 返回元素的偏移容器。                                         |
| element.offsetTop                                            | 返回元素的垂直偏移位置。                                     |
| [element.ownerDocument](https://www.w3school.com.cn/jsref/prop_node_ownerdocument.asp) | 返回元素的根元素（文档对象）。                               |
| [element.parentNode](https://www.w3school.com.cn/jsref/prop_node_parentnode.asp) | 返回元素的父节点。                                           |
| [element.previousSibling](https://www.w3school.com.cn/jsref/prop_node_previoussibling.asp) | 返回位于相同节点树层级的前一个元素。                         |
| [element.removeAttribute()](https://www.w3school.com.cn/jsref/met_element_removeattribute.asp) | 从元素中移除指定属性。                                       |
| [element.removeAttributeNode()](https://www.w3school.com.cn/jsref/met_element_removeattributenode.asp) | 移除指定的属性节点，并返回被移除的节点。                     |
| [element.removeChild()](https://www.w3school.com.cn/jsref/met_node_removechild.asp) | 从元素中移除子节点。                                         |
| [element.replaceChild()](https://www.w3school.com.cn/jsref/met_node_replacechild.asp) | 替换元素中的子节点。                                         |
| element.scrollHeight                                         | 返回元素的整体高度。                                         |
| element.scrollLeft                                           | 返回元素左边缘与视图之间的距离。                             |
| element.scrollTop                                            | 返回元素上边缘与视图之间的距离。                             |
| element.scrollWidth                                          | 返回元素的整体宽度。                                         |
| [element.setAttribute()](https://www.w3school.com.cn/jsref/met_element_setattribute.asp) | 把指定属性设置或更改为指定值。                               |
| [element.setAttributeNode()](https://www.w3school.com.cn/jsref/met_element_setattributenode.asp) | 设置或更改指定属性节点。                                     |
| element.setIdAttribute()                                     |                                                              |
| element.setIdAttributeNode()                                 |                                                              |
| element.setUserData()                                        | 把对象关联到元素上的键。                                     |
| element.style                                                | 设置或返回元素的 style 属性。                                |
| [element.tabIndex](https://www.w3school.com.cn/jsref/prop_html_tabindex.asp) | 设置或返回元素的 tab 键控制次序。                            |
| [element.tagName](https://www.w3school.com.cn/jsref/prop_element_tagname.asp) | 返回元素的标签名。                                           |
| [element.textContent](https://www.w3school.com.cn/jsref/prop_node_textcontent.asp) | 设置或返回节点及其后代的文本内容。                           |
| [element.title](https://www.w3school.com.cn/jsref/prop_html_title.asp) | 设置或返回元素的 title 属性。                                |
| element.toString()                                           | 把元素转换为字符串。                                         |
| [nodelist.item()](https://www.w3school.com.cn/jsref/met_nodelist_item.asp) | 返回 NodeList 中位于指定下标的节点。                         |
| [nodelist.length](https://www.w3school.com.cn/jsref/prop_nodelist_length.asp) | 返回 NodeList 中的节点数。                                   |



## CSS Selectors

In CSS, selectors are patterns used to select the element(s) you want to style.

Use our [CSS Selector Tester](https://www.w3schools.com/cssref/trysel.asp) to demonstrate the different selectors.

| Selector                                                     | Example               | Example description                                          |
| :----------------------------------------------------------- | :-------------------- | :----------------------------------------------------------- |
| [.*class*](https://www.w3schools.com/cssref/sel_class.asp)   | .intro                | Selects all elements with class="intro"                      |
| *.class1.class2*                                             | .name1.name2          | Selects all elements with both *name1* and *name2* set within its class attribute |
| *.class1 .class2*                                            | .name1 .name2         | Selects all elements with *name2* that is a descendant of an element with *name1* |
| [#*id*](https://www.w3schools.com/cssref/sel_id.asp)         | #firstname            | Selects the element with id="firstname"                      |
| [*](https://www.w3schools.com/cssref/sel_all.asp)            | *                     | Selects all elements                                         |
| *[element](https://www.w3schools.com/cssref/sel_element.asp)* | p                     | Selects all <p> elements                                     |
| *[element.class](https://www.w3schools.com/cssref/sel_element_class.asp)* | p.intro               | Selects all <p> elements with class="intro"                  |
| *[element,element](https://www.w3schools.com/cssref/sel_element_comma.asp)* | div, p                | Selects all <div> elements and all <p> elements              |
| [*element* *element*](https://www.w3schools.com/cssref/sel_element_element.asp) | div p                 | Selects all <p> elements inside <div> elements               |
| [*element*>*element*](https://www.w3schools.com/cssref/sel_element_gt.asp) | div > p               | Selects all <p> elements where the parent is a <div> element |
| [*element*+*element*](https://www.w3schools.com/cssref/sel_element_pluss.asp) | div + p               | Selects all <p> elements that are placed immediately after <div> elements |
| [*element1*~*element2*](https://www.w3schools.com/cssref/sel_gen_sibling.asp) | p ~ ul                | Selects every <ul> element that are preceded by a <p> element |
| [[*attribute*\]](https://www.w3schools.com/cssref/sel_attribute.asp) | [target]              | Selects all elements with a target attribute                 |
| [[*attribute*=*value*\]](https://www.w3schools.com/cssref/sel_attribute_value.asp) | [target=_blank]       | Selects all elements with target="_blank"                    |
| [[*attribute*~=*value*\]](https://www.w3schools.com/cssref/sel_attribute_value_contains.asp) | [title~=flower]       | Selects all elements with a title attribute containing the word "flower" |
| [[*attribute*\|=*value*\]](https://www.w3schools.com/cssref/sel_attribute_value_lang.asp) | [lang\|=en]           | Selects all elements with a lang attribute value starting with "en" |
| [[*attribute*^=*value*\]](https://www.w3schools.com/cssref/sel_attr_begin.asp) | a[href^="https"]      | Selects every <a> element whose href attribute value begins with "https" |
| [[*attribute*$=*value*\]](https://www.w3schools.com/cssref/sel_attr_end.asp) | a[href$=".pdf"]       | Selects every <a> element whose href attribute value ends with ".pdf" |
| [[*attribute**=*value*\]](https://www.w3schools.com/cssref/sel_attr_contain.asp) | a[href*="w3schools"]  | Selects every <a> element whose href attribute value contains the substring "w3schools" |
| [:active](https://www.w3schools.com/cssref/sel_active.asp)   | a:active              | Selects the active link                                      |
| [::after](https://www.w3schools.com/cssref/sel_after.asp)    | p::after              | Insert something after the content of each <p> element       |
| [::before](https://www.w3schools.com/cssref/sel_before.asp)  | p::before             | Insert something before the content of each <p> element      |
| [:checked](https://www.w3schools.com/cssref/sel_checked.asp) | input:checked         | Selects every checked <input> element                        |
| [:default](https://www.w3schools.com/cssref/sel_default.asp) | input:default         | Selects the default <input> element                          |
| [:disabled](https://www.w3schools.com/cssref/sel_disabled.asp) | input:disabled        | Selects every disabled <input> element                       |
| [:empty](https://www.w3schools.com/cssref/sel_empty.asp)     | p:empty               | Selects every <p> element that has no children (including text nodes) |
| [:enabled](https://www.w3schools.com/cssref/sel_enabled.asp) | input:enabled         | Selects every enabled <input> element                        |
| [:first-child](https://www.w3schools.com/cssref/sel_firstchild.asp) | p:first-child         | Selects every <p> element that is the first child of its parent |
| [::first-letter](https://www.w3schools.com/cssref/sel_firstletter.asp) | p::first-letter       | Selects the first letter of every <p> element                |
| [::first-line](https://www.w3schools.com/cssref/sel_firstline.asp) | p::first-line         | Selects the first line of every <p> element                  |
| [:first-of-type](https://www.w3schools.com/cssref/sel_first-of-type.asp) | p:first-of-type       | Selects every <p> element that is the first <p> element of its parent |
| [:focus](https://www.w3schools.com/cssref/sel_focus.asp)     | input:focus           | Selects the input element which has focus                    |
| [:hover](https://www.w3schools.com/cssref/sel_hover.asp)     | a:hover               | Selects links on mouse over                                  |
| [:in-range](https://www.w3schools.com/cssref/sel_in-range.asp) | input:in-range        | Selects input elements with a value within a specified range |
| [:indeterminate](https://www.w3schools.com/cssref/sel_indeterminate.asp) | input:indeterminate   | Selects input elements that are in an indeterminate state    |
| [:invalid](https://www.w3schools.com/cssref/sel_invalid.asp) | input:invalid         | Selects all input elements with an invalid value             |
| [:lang(*language*)](https://www.w3schools.com/cssref/sel_lang.asp) | p:lang(it)            | Selects every <p> element with a lang attribute equal to "it" (Italian) |
| [:last-child](https://www.w3schools.com/cssref/sel_last-child.asp) | p:last-child          | Selects every <p> element that is the last child of its parent |
| [:last-of-type](https://www.w3schools.com/cssref/sel_last-of-type.asp) | p:last-of-type        | Selects every <p> element that is the last <p> element of its parent |
| [:link](https://www.w3schools.com/cssref/sel_link.asp)       | a:link                | Selects all unvisited links                                  |
| [:not(*selector*)](https://www.w3schools.com/cssref/sel_not.asp) | :not(p)               | Selects every element that is not a <p> element              |
| [:nth-child(*n*)](https://www.w3schools.com/cssref/sel_nth-child.asp) | p:nth-child(2)        | Selects every <p> element that is the second child of its parent |
| [:nth-last-child(*n*)](https://www.w3schools.com/cssref/sel_nth-last-child.asp) | p:nth-last-child(2)   | Selects every <p> element that is the second child of its parent, counting from the last child |
| [:nth-last-of-type(*n*)](https://www.w3schools.com/cssref/sel_nth-last-of-type.asp) | p:nth-last-of-type(2) | Selects every <p> element that is the second <p> element of its parent, counting from the last child |
| [:nth-of-type(*n*)](https://www.w3schools.com/cssref/sel_nth-of-type.asp) | p:nth-of-type(2)      | Selects every <p> element that is the second <p> element of its parent |
| [:only-of-type](https://www.w3schools.com/cssref/sel_only-of-type.asp) | p:only-of-type        | Selects every <p> element that is the only <p> element of its parent |
| [:only-child](https://www.w3schools.com/cssref/sel_only-child.asp) | p:only-child          | Selects every <p> element that is the only child of its parent |
| [:optional](https://www.w3schools.com/cssref/sel_optional.asp) | input:optional        | Selects input elements with no "required" attribute          |
| [:out-of-range](https://www.w3schools.com/cssref/sel_out-of-range.asp) | input:out-of-range    | Selects input elements with a value outside a specified range |
| [::placeholder](https://www.w3schools.com/cssref/sel_placeholder.asp) | input::placeholder    | Selects input elements with the "placeholder" attribute specified |
| [:read-only](https://www.w3schools.com/cssref/sel_read-only.asp) | input:read-only       | Selects input elements with the "readonly" attribute specified |
| [:read-write](https://www.w3schools.com/cssref/sel_read-write.asp) | input:read-write      | Selects input elements with the "readonly" attribute NOT specified |
| [:required](https://www.w3schools.com/cssref/sel_required.asp) | input:required        | Selects input elements with the "required" attribute specified |
| [:root](https://www.w3schools.com/cssref/sel_root.asp)       | :root                 | Selects the document's root element                          |
| [::selection](https://www.w3schools.com/cssref/sel_selection.asp) | ::selection           | Selects the portion of an element that is selected by a user |
| [:target](https://www.w3schools.com/cssref/sel_target.asp)   | #news:target          | Selects the current active #news element (clicked on a URL containing that anchor name) |
| [:valid](https://www.w3schools.com/cssref/sel_valid.asp)     | input:valid           | Selects all input elements with a valid value                |
| [:visited](https://www.w3schools.com/cssref/sel_visited.asp) | a:visited             | Selects all visited links                                    |



## 参考

[https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelectorAll](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelectorAll)

[https://www.w3schools.com/jsref/met_element_scrollintoview.asp](https://www.w3schools.com/jsref/met_element_scrollintoview.asp)