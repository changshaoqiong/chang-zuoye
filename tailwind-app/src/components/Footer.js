'use client';

import React, { useState, useEffect } from 'react';

const Footer = () => {
    // 问答功能状态
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');
    const [isLoadingQA, setIsLoadingQA] = useState(false);
    const [errorQA, setErrorQA] = useState('');
    // WakaTime状态
    const [wakatimeText, setWakatimeText] = useState('');
    const [isLoadingWaka, setIsLoadingWaka] = useState(true);
    const [errorWaka, setErrorWaka] = useState(null);
    // 环境变量
    const apiKey = process.env.NEXT_PUBLIC_QANYTHING_API_KEY;
    const agentUuid = process.env.NEXT_PUBLIC_QANYTHING_AGENT_UUID;

    // WakaTime数据获取
    useEffect(() => {
        const fetchWakatimeStats = async () => {
            setIsLoadingWaka(true);
            setErrorWaka(null);
            try {
                // 替换为项目总时长 API 端点
                const apiUrl = `https://csc-wakatime.wemedia.press/`;
                const response = await fetch(apiUrl);
                if (!response.ok) {
                    const errorData = await response.json().catch(() => ({ message: "解析错误响应失败" }));
                    throw new Error(errorData.message || `请求失败：${response.status}`);
                }
                const result = await response.json();
                // 解析总时长（单位：秒，转换为小时）
                const totalSeconds = result.data.total_seconds;
                const totalHours = (totalSeconds / 3600).toFixed(2); // 保留2位小数
                setWakatimeText(`：${totalHours} 小时`);
            } catch (err) {
                console.error("WakaTime数据获取失败", err);
                setErrorWaka(err.message);
                setWakatimeText("无法加载统计数据");
            } finally {
                setIsLoadingWaka(false);
            }
        };
        fetchWakatimeStats();
    }, []);

    // 问答功能处理
    const handleAsk = async () => {
        if (!question.trim() || !apiKey || !agentUuid) {
            setError('请输入问题并确保已配置API Key和Agent UUID'); // 此提示将消失当变量正确配置
            return;
        }
        setIsLoadingQA(true);
        setErrorQA('');
        try {
            const response = await fetch('https://openapi.youdao.com/q_anything/api/bot/chat_stream', {
                method: 'POST',
                headers: {
                    'Authorization': apiKey,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ uuid: agentUuid, question, history: [], sourceNeeded: true })
            });
            if (!response.ok) throw new Error(`API请求失败：${response.status}`);
            const reader = response.body.getReader();
            const decoder = new TextDecoder();
            let fullResponse = '';
            while (true) {
                const { done, value } = await reader.read();
                if (done) break;
                const chunk = decoder.decode(value);
                const data = chunk.split('data: ').filter(Boolean).map(JSON.parse);
                data.forEach(item => {
                    if (item.result?.response) fullResponse += item.result.response;
                });
            }
            setAnswer(fullResponse);
        } catch (err) {
            setErrorQA(`错误：${err.message}`);
        } finally {
            setIsLoadingQA(false);
        }
    };

    return (
        <footer className="bg-slate-800 text-slate-300 py-8 mt-12">
            <div className="container mx-auto px-4 text-center">
                {/* 版权信息 */}
                <p className="text-sm">&copy; {new Date().getFullYear()} 《Web前端开发》课程练习平台. 保留所有权利.</p>
                <p className="text-xs mt-2">使用 Next.js 和 Tailwind CSS 构建</p>

                {/* WakaTime统计 */}
                <p className="text-xs mt-2">Wakatime : {isLoadingWaka ? "加载中..." : errorWaka ? `错误：${errorWaka}` : wakatimeText}</p>




                {/* 问答功能 */}
                <div className="bg-gray-100 p-4 mt-4 rounded">
                    <h3 className="text-lg font-semibold mb-2">新闻传播问答</h3>
                    <div className="flex gap-2 mb-2">
                        <input
                            type="text"
                            value={question}
                            onChange={(e) => setQuestion(e.target.value)}
                            placeholder="输入您的问题..."
                            className="flex-1 p-2 border rounded"
                        />
                        <button
                            onClick={handleAsk}
                            disabled={isLoadingQA}
                            className="bg-blue-500 text-white px-4 py-2 rounded disabled:opacity-50"
                        >
                            {isLoadingQA ? '正在获取答案...' : '提问'}
                        </button>
                    </div>
                    {errorQA && <p className="text-red-500 text-sm mb-2">{errorQA}</p>}
                    {answer && <div className="bg-white p-2 rounded"><p className="text-gray-800">{answer}</p></div>}
                </div>
            </div>
        </footer>
    );
};

export default Footer;