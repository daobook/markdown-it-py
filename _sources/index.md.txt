# markdown-it-py

> Markdown parser done right.

- {fa}`check,text-success mr-1` Follows the __[CommonMark spec](http://spec.commonmark.org/)__ for baseline parsing
- {fa}`check,text-success mr-1` Configurable syntax: you can add new rules and even replace existing ones.
- {fa}`check,text-success mr-1` Pluggable: Adds syntax extensions to extend the parser (see the [plugin list](md/plugins))
- {fa}`check,text-success mr-1` High speed (see our [benchmarking tests](md/performance))
- {fa}`check,text-success mr-1` [Safe by default](md/security)

<!-- For a good introduction to [markdown-it] see the __[Live demo](https://markdown-it.github.io)__.
This is a Python port of the well used [markdown-it], and some of its associated plugins.
The driving design philosophy of the port has been to change as little of the fundamental code structure (file names, function name, etc) as possible, just sprinkling in a little Python syntactical sugar ✨.
It is very simple to write complimentary extensions for both language implementations! -->
关于 [markdown-it] 的良好介绍，请看 __[实时演示](https://markdown-it.github.io)__。这是一个被广泛使用的 [markdown-it] 的 Python 移植，以及它的一些相关插件。移植的驱动设计理念是尽可能少地改变基本的代码结构（文件名、函数名等），只是在 Python 中撒上一点语法糖✨。为两种语言实现编写免费的扩展是非常简单的！

## References & Thanks

<!-- Big thanks to the authors of [markdown-it] -->
非常感谢 [markdown-it] 的作者。

- Alex Kocharin [github/rlidwka](https://github.com/rlidwka)
- Vitaly Puzrin [github/puzrin](https://github.com/puzrin)

Also [John MacFarlane](https://github.com/jgm) for his work on the CommonMark spec and reference implementations.

## Related Links

- <https://github.com/jgm/CommonMark> - reference CommonMark implementations in C & JS, also contains latest spec & online demo.
- <http://talk.commonmark.org> - CommonMark forum, good place to collaborate developers' efforts.

```{toctree}
:maxdepth: 2

using
architecture
other
plugins
contributing
api/markdown_it
```

[markdown-it]: https://github.com/markdown-it/markdown-it
