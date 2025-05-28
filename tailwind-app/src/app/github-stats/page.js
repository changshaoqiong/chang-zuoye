// src/app/github-stats/page.js
// GitHub 提交记录列表页面组件：用于展示指定 GitHub 仓库的最近提交记录

// 导入 Next.js 的 Link 组件（用于页面间跳转）
import Link from 'next/link';

/**
 * 异步函数：通过 GitHub API 获取仓库的提交记录
 * @returns {Promise<Array>} 包含提交记录的数组（每个元素是提交对象）
 */
async function getCommits() {
    // 注意：未认证的 GitHub API 请求有速率限制（每小时 60 次）
    // 实际生产环境建议使用认证请求（添加 Token）或后端代理提升限制
    // 构造 GitHub API 请求 URL（替换为用户自己的仓库地址：changshaoqiong/chang-zuoye）
    // per_page=10：限制返回最近 10 条提交记录
    const res = await fetch('https://api.github.com/repos/changshaoqiong/chang-zuoye/commits?per_page=10', {
        // next: { revalidate: 3600 } // 可选配置：每小时重新验证数据（用于增量更新）
    });

    // 检查请求是否成功（HTTP 状态码非 2xx 时抛出错误）
    if (!res.ok) {
        // 抛出错误信息，会被 Next.js 的 error.js 错误边界捕获处理
        throw new Error('Failed to fetch commits from GitHub');
    }

    // 解析响应数据为 JSON 格式并返回（返回提交记录数组）
    return res.json();
}

/**
 * 页面组件：渲染 GitHub 提交记录列表
 * @returns {JSX.Element} 页面 UI 元素
 */
export default async function GitHubStatsPage() {
    // 初始化状态变量：存储提交记录数组（默认空数组）、请求错误信息（默认 null）
    let commits = [];
    let errorFetching = null;

    // 尝试获取提交记录（异步请求）
    try {
        // 调用 getCommits 函数获取提交数据
        commits = await getCommits();
    } catch (error) {
        // 捕获请求过程中的错误（如网络问题、API 错误）
        console.error('获取提交数据失败:', error); // 错误信息输出到控制台
        errorFetching = error.message; // 存储错误信息用于页面展示
    }

    // 情况 1：请求失败（errorFetching 存在）
    if (errorFetching) {
        return (
            // 渲染错误提示页面
            <div className="container mx-auto p-4">
                <h1 className="text-2xl font-bold mb-4 text-red-500">获取 GitHub 提交数据失败</h1>
                <p>{errorFetching}</p> {/* 显示具体错误信息（如 API 返回的错误描述） */}
                <p>请检查网络连接或稍后再试。详细错误已记录在控制台。</p>
            </div>
        );
    }

    // 情况 2：请求成功，渲染提交列表页面
    return (
        <div className="container mx-auto p-4">
            {/* 页面主标题：显示当前仓库名称（与 API 请求的仓库一致） */}
            <h1 className="text-2xl font-bold mb-4">GitHub: changshaoqiong/chang-zuoye 提交记录</h1>
            <p className="mb-4">最近 {commits.length} 条提交：</p> {/* 显示实际获取到的提交数量 */}

            {/* 条件渲染：根据提交数量决定显示列表或提示 */}
            {commits.length > 0 ? (
                // 提交数量 > 0 时，渲染提交列表
                <ul className="space-y-4">
                    {/* 遍历提交数组生成列表项（每个提交对应一个列表项） */}
                    {commits.map((commit) => (
                        <li 
                            key={commit.sha} // 唯一标识（提交的 SHA 值，确保 React 列表渲染性能）
                            className="p-4 border rounded-lg shadow hover:shadow-md transition-shadow" // 列表项样式（边框、阴影、悬停效果）
                        >
                            <div className="font-semibold text-lg text-blue-600">
                                {/* 提交信息链接：跳转到提交详情页（动态路由 /github-stats/commits/[commitId]） */}
                                <Link 
                                    href={`/github-stats/commits/${commit.sha}`} // 动态路由路径（commit.sha 为提交的唯一标识）
                                    className="hover:underline" // 悬停下划线交互效果
                                >
                                    {commit.commit.message.split('\n')[0]} {/* 截取提交信息的第一行（避免过长） */}
                                </Link>
                            </div>

                            {/* 作者信息：显示提交作者的名称和邮箱 */}
                            <p className="text-sm text-gray-600">
                                作者: {commit.commit.author.name} ({commit.commit.author.email})
                            </p>

                            {/* 提交时间：将 ISO 格式时间转换为本地可读格式 */}
                            <p className="text-sm text-gray-500">
                                日期: {new Date(commit.commit.author.date).toLocaleString()}
                            </p>

                            {/* 查看详情链接：跳转到当前提交的详情页 */}
                            <Link 
                                href={`/github-stats/commits/${commit.sha}`} 
                                className="text-blue-500 hover:underline text-sm mt-2 inline-block"
                            >
                                查看详情 &rarr;
                            </Link>
                        </li>
                    ))}
                </ul>
            ) : (
                // 提交数量为 0 时，显示提示信息（可能仓库无提交或 API 未返回数据）
                <p>未能获取到提交记录，或仓库中没有提交。</p>
            )}
        </div>
        
    );
}
