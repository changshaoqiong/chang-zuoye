// src/app/github-stats/loading.js
// GitHub 统计数据加载状态组件：用于在数据请求过程中显示加载动画和提示信息

// 定义默认导出的加载状态组件（无状态函数组件）
export default function LoadingGitHubStats() {
    return (
        // 外层容器：使用 Tailwind 类实现居中布局、内边距和文本居中
        <div className="container mx-auto p-4 text-center">
            {/* 加载动画：使用圆形旋转图标 */}
            <div
                className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto my-4"
            // animate-spin：Tailwind 内置的旋转动画类
            // rounded-full：圆形边框（border-radius: 9999px）
            // h-12/w-12：尺寸（高度/宽度 3rem，约 48px）
            // border-b-2：仅显示底部边框（宽度 2px）
            // border-blue-500：边框颜色（蓝色系）
            // mx-auto：水平居中；my-4：上下外边距（1rem）
            ></div>
            {/* 主提示文本：较大的加粗字体 */}
            <p className="text-lg font-semibold">正在加载 GitHub 统计数据...</p>
            {/* 次要提示文本：较小的灰色字体，补充说明加载状态 */}
            <p className="text-sm text-gray-600">请稍候，我们正在从 GitHub 获取最新的提交信息。</p>
        </div>
    );
}