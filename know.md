## 父知识点：Next.js 配置文件 `next.config.mjs`
### 子知识点 1：文件类型
#### 孙知识点 1：使用 `.mjs` 扩展名
表明这是一个 ES 模块文件，可使用 `import` 和 `export` 语法。
### 子知识点 2：类型注解
#### 孙知识点 1：`/** @type {import('next').NextConfig} */`
使用 JSDoc 类型注解，帮助编辑器理解 `nextConfig` 对象的类型，提供代码提示。
### 子知识点 3：配置对象
#### 孙知识点 1：`const nextConfig = {}`
定义一个空的 Next.js 配置对象，可在其中添加各种配置选项。
### 子知识点 4：导出配置
#### 孙知识点 1：`export default nextConfig`
将配置对象作为默认导出，供 Next.js 应用使用。