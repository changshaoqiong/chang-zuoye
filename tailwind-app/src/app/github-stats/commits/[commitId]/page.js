// src/app/github-stats/commits/[commitId]/page.js
// 动态路由页面：展示 GitHub 仓库中特定提交（commitId）的详细信息

// 定义异步函数：通过 GitHub API 获取指定提交的详细信息
// 参数：commitId（提交的 SHA 值）
async function getCommitDetails(commitId) {
  // 构造 GitHub API 请求 URL（替换为用户自己的仓库地址）
  const res = await fetch(`https://api.github.com/repos/changshaoqiong/chang-zuoye/commits/${commitId}`);
  // 检查请求是否成功（HTTP 状态码非 2xx 时抛出错误）
  if (!res.ok) {
    throw new Error(`Failed to fetch commit details for ${commitId}`);
  }
  // 解析响应为 JSON 并返回
  return res.json();
}

// 定义页面组件（Next.js 动态路由组件）
// 参数：params（动态路由参数对象，包含 commitId）
export default async function CommitDetailPage({ params }) {
  // 从 params 中解构获取动态路由参数 commitId（即提交的 SHA 值）
  const { commitId } = params;
  // 初始化状态变量：存储提交详情数据、请求错误信息
  let commitDetails = null;
  let errorFetching = null;

  // 尝试获取提交详情（异步请求）
  try {
    commitDetails = await getCommitDetails(commitId);
  } catch (error) {
    // 捕获请求错误，记录错误信息
    console.error(error);
    errorFetching = error.message;
  }

  // 情况 1：请求失败（errorFetching 存在）
  if (errorFetching) {
    return (
      <div className="container mx-auto p-4">
        <h1 className="text-xl font-bold mb-4 text-red-500">获取提交详情失败</h1>
        <p>Commit SHA: {commitId}</p>
        <p>{errorFetching}</p>
      </div>
    );
  }

  // 情况 2：请求中（commitDetails 未加载完成）
  if (!commitDetails) {
    return (
      <div className="container mx-auto p-4">
        <h1 className="text-xl font-bold mb-4">加载中...</h1>
        <p>Commit SHA: {commitId}</p>
      </div>
    );
  }

  // 解构提交详情数据（来自 GitHub API 响应）
  const { commit, author, committer, html_url, files } = commitDetails;

  // 情况 3：数据加载成功，渲染提交详情页面
  return (
    <div className="container mx-auto p-4">
      {/* 返回提交列表的链接 */}
      <a href="/github-stats" className="text-blue-500 hover:underline mb-4 inline-block">&larr; 返回提交列表</a>
      {/* 显示提交 SHA 的前 7 位（常用缩写形式） */}
      <h1 className="text-2xl font-bold mb-2 break-all">提交详情: {commitId.substring(0, 7)}</h1>
      {/* 显示提交信息（GitHub 提交的 message 字段） */}
      <p className="text-lg mb-4 bg-gray-100 p-3 rounded">{commit.message}</p>

      {/* 作者与提交者信息分两列展示 */}
      <div className="grid md:grid-cols-2 gap-4 mb-6">
        <div className="border p-3 rounded">
          <h2 className="text-md font-semibold mb-1">作者 (Author):</h2>
          <p>{commit.author.name} &lt;{commit.author.email}&gt;</p>
          <p>日期: {new Date(commit.author.date).toLocaleString()}</p>
          {/* 作者头像（若 API 返回 author 对象） */}
          {author && <img src={author.avatar_url} alt={author.login} className="w-10 h-10 rounded-full mt-1" />}
        </div>
        <div className="border p-3 rounded">
          <h2 className="text-md font-semibold mb-1">提交者 (Committer):</h2>
          <p>{commit.committer.name} &lt;{commit.committer.email}&gt;</p>
          <p>日期: {new Date(commit.committer.date).toLocaleString()}</p>
          {/* 提交者头像（若 API 返回 committer 对象） */}
          {committer && <img src={committer.avatar_url} alt={committer.login} className="w-10 h-10 rounded-full mt-1" />}
        </div>
      </div>

      {/* 跳转到 GitHub 原生提交页面的链接 */}
      <a href={html_url} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline mb-4 inline-block">
        在 GitHub 上查看提交 &rarr;
      </a>

      {/* 显示变更的文件列表（若有文件变更） */}
      {files && files.length > 0 && (
        <div>
          <h2 className="text-xl font-semibold mb-2">变更的文件 ({files.length}):</h2>
          <ul className="list-disc pl-5 space-y-1">
            {files.map((file) => (
              <li key={file.sha || file.filename} className="text-sm">
                {/* 跳转到文件 blob 页面的链接 */}
                <a href={file.blob_url} target="_blank" rel="noopener noreferrer" className="hover:underline text-green-600">
                  {file.filename}
                </a>
                {/* 显示文件新增/删除的行数 */}
                <span className="ml-2 text-gray-500">(+{file.additions} / -{file.deletions})</span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

// 可选：为动态路由生成元数据（用于 SEO 或浏览器标签页标题）
// 参数：params（动态路由参数对象，包含 commitId）
export async function generateMetadata({ params }) {
  const { commitId } = params;
  return {
    title: `Commit ${commitId.substring(0, 7)} - GitHub Stats`, // 页面标题
    description: `Details for commit ${commitId} from changshaoqiong/chang-zuoye`, // 页面描述
  };
}