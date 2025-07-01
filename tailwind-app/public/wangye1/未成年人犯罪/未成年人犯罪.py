<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>守护青春 远离犯罪</title>
    <style>
        /* 设置 logo 的样式 */
        .logo {
            position: fixed;
            top: 30px;
            right: 30px;
            width: 100px;
            height: auto;
            z-index: 999;
            background: rgba(255, 255, 255, 0.9);
            padding: 8px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>

<body>
    <!-- 添加 logo 图片 -->
    <img class="logo"
        src="https://mmbiz.qpic.cn/mmbiz_png/KM3FU3XPKYibHicdC1UpqdYAOpF6W0Sg8SJaicrJuOYp7GBdibCcvvYhmhkeLzB2tlC0eKWUQmp95K2FDJKFBjuw1Q/0?wxfrom=12&tp=wxpic&usePicPrefetch=1&wx_fmt=png&from=appmsg&watermark=1"
        alt="Logo">
    <title>未成年犯罪数据可视化</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.8/dist/chart.umd.min.js"></script>

    <!-- Tailwind配置 -->
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#000000',
                        secondary: '#333333',
                        accent: '#ff3d00',
                        neutral: '#f5f5f5',
                        'neutral-dark': '#4a4a4a',
                    },
                    fontFamily: {
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                    },
                },
            }
        }
    </script>

    <style type="text/tailwindcss">
        @layer utilities {
        .content-auto {
          content-visibility: auto;
        }
        .scrollbar-hide {
          -ms-overflow-style: none;
          scrollbar-width: none;
        }
        .scrollbar-hide::-webkit-scrollbar {
          display: none;
        }
        .text-shadow {
          text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .card-hover {
          transition: all 0.3s ease;
        }
        .card-hover:hover {
          transform: translateY(-5px);
          box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
      }
    </style>
    </head>

    <body class="bg-neutral text-primary overflow-x-hidden">
        <!-- 左侧导航栏 -->
        <aside id="sidebar"
            class="fixed top-0 left-0 h-full w-16 md:w-64 bg-primary text-white shadow-lg z-50 transition-all duration-300">
            <div class="flex flex-col h-full">
                <div class="p-4 flex items-center justify-center md:justify-start">
                    <div class="w-10 h-10 rounded-full bg-accent flex items-center justify-center">
                        <i class="fa fa-balance-scale text-white"></i>
                    </div>
                    <h1 class="ml-3 text-xl font-bold hidden md:block text-center">法护青苗<br>成长防线</h1>
                </div>

                <nav class="flex-1 py-6 overflow-y-auto scrollbar-hide">
                    <ul class="space-y-1">
                        <li>
                            <a href="#home"
                                class="flex items-center p-3 text-white hover:bg-accent/80 rounded-lg mx-2 transition-all">
                                <i class="fa fa-home text-xl w-6 text-center"></i>
                                <span class="ml-3 hidden md:block">首页</span>
                            </a>
                        </li>
                        <li>
                            <a href="#overview"
                                class="flex items-center p-3 text-white hover:bg-accent/80 rounded-lg mx-2 transition-all">
                                <i class="fa fa-bar-chart text-xl w-6 text-center"></i>
                                <span class="ml-3 hidden md:block">现状概览</span>
                            </a>
                        </li>
                        <li>
                            <a href="#causes"
                                class="flex items-center p-3 text-white hover:bg-accent/80 rounded-lg mx-2 transition-all">
                                <i class="fa fa-lightbulb-o text-xl w-6 text-center"></i>
                                <span class="ml-3 hidden md:block">原因分析</span>
                            </a>
                        </li>
                        <li>
                            <a href="#cases"
                                class="flex items-center p-3 text-white hover:bg-accent/80 rounded-lg mx-2 transition-all">
                                <i class="fa fa-folder-open text-xl w-6 text-center"></i>
                                <span class="ml-3 hidden md:block">典型案例</span>
                            </a>
                        </li>
                        <li>
                            <a href="#prevention"
                                class="flex items-center p-3 text-white hover:bg-accent/80 rounded-lg mx-2 transition-all">
                                <i class="fa fa-shield text-xl w-6 text-center"></i>
                                <span class="ml-3 hidden md:block">预防措施</span>
                            </a>
                        </li>
                        <li>
                            <a href="#resources"
                                class="flex items-center p-3 text-white hover:bg-accent/80 rounded-lg mx-2 transition-all">
                                <i class="fa fa-book text-xl w-6 text-center"></i>
                                <span class="ml-3 hidden md:block">相关资源</span>
                            </a>
                        </li>
                    </ul>
                </nav>

                <div class="p-4 border-t border-gray-700">
                    <a href="#contact"
                        class="flex items-center p-3 text-white hover:bg-accent/80 rounded-lg transition-all">
                        <i class="fa fa-phone text-xl w-6 text-center"></i>
                        <span class="ml-3 hidden md:block">联系我们</span>
                    </a>
                </div>
            </div>
        </aside>

        <!-- 主内容区 -->
        <main class="ml-16 md:ml-64 min-h-screen">
            <!-- 首页 -->
            <section id="home"
                class="relative min-h-screen flex items-center justify-center bg-gradient-to-br from-primary to-secondary text-white overflow-hidden">
                <div class="absolute inset-0 opacity-10">
                    <div
                        class="absolute inset-0 bg-[url('https://ts1.tc.mm.bing.net/th/id/R-C.16a983e8883a62ce5184c0478a3dc829?rik=pZffTX5iOQ%2boCw&riu=http%3a%2f%2f5b0988e595225.cdn.sohucs.com%2fimages%2f20190623%2fad3966e9c73c465d84a38eb62b560340.jpeg&ehk=OHGZlYMHyqSdFeio%2fGvIkGrQAHVB0310x81qFWjgt48%3d&risl=&pid=ImgRaw&r=0')] bg-cover bg-center">
                    </div>
                </div>

                <div class="container mx-auto px-6 py-20 relative z-10">
                    <div class="max-w-3xl mx-auto text-center">
                        <h1 class="text-[clamp(2.5rem,5vw,4rem)] font-bold mb-6 leading-tight text-shadow">
                            守护青春 <span class="text-accent">远离犯罪</span>
                        </h1>
                        <p class="text-[clamp(1rem,2vw,1.25rem)] mb-10 text-gray-200 leading-relaxed">
                            <span
                                style="font-family: 楷体;">每一个孩子都是家庭的希望、社会的未来，他们的成长轨迹牵动着无数父母的目光与社会的期待。我们深入挖掘未成年犯罪的真实数据与背后的成长困境，不仅是为了剖析问题，更是为了以理解与关怀为起点——让每一个迷茫的少年都能被看见，每一段偏离的人生都有机会被修正。让我们携手筑起防护网，用法律的温度、教育的力量与社会的关爱，为未成年人的成长守护一片纯净的天空。</span>
                        </p>
                        <div class="flex flex-col sm:flex-row justify-center gap-4">
                            <a href="#overview"
                                class="px-8 py-3 bg-accent hover:bg-accent/90 text-white rounded-lg transition-all shadow-lg hover:shadow-xl">
                                查看现状数据
                            </a>
                            <a href="#prevention"
                                class="px-8 py-3 bg-white/10 hover:bg-white/20 text-white rounded-lg transition-all backdrop-blur-sm border border-white/30">
                                了解预防措施
                            </a>
                        </div>
                    </div>
                </div>

                <div class="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-neutral to-transparent"></div>
            </section>

            <!-- 现状概览 -->
            <section id="overview" class="py-20 bg-neutral">
                <div class="container mx-auto px-6">
                    <div class="text-center mb-16">
                        <h2 class="text-[clamp(1.75rem,3vw,2.5rem)] font-bold mb-4">未成年犯罪现状概览</h2>
                        <p class="text-gray-600 max-w-3xl mx-auto">
                            近年来，未成年人犯罪问题呈现低龄化、暴力化趋势，2023年最高检数据显示，14-16岁犯罪占比较五年前上升5.2%。以下基于2020-2024年权威数据的现状分析，数据来源标注在各图表下方，通过多维度可视化呈现问题的严峻性与变化趋势。
                        </p>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
                        <!-- 图表1：未成年犯罪人数趋势 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <h3 class="text-xl font-bold mb-4 flex items-center">
                                <i class="fa fa-line-chart text-accent mr-2"></i>
                                近五年未成年犯罪人数趋势
                            </h3>
                            <div class="h-80">
                                <canvas id="crimeTrendChart"></canvas>
                            </div>
                            <p class="text-sm text-gray-500 mt-2">数据来源：最高人民检察院工作报告（2020-2024）</p>
                        </div>

                        <!-- 图表2：犯罪类型分布 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <h3 class="text-xl font-bold mb-4 flex items-center">
                                <i class="fa fa-pie-chart text-accent mr-2"></i>
                                未成年犯罪类型分布
                            </h3>
                            <div class="h-80">
                                <canvas id="crimeTypeChart"></canvas>
                            </div>
                            <p class="text-sm text-gray-500 mt-2">数据来源：中国青少年研究中心（2024）</p>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                        <!-- 统计卡片1 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <div class="flex items-center justify-between mb-4">
                                <h3 class="text-xl font-bold">犯罪年龄分布</h3>
                                <i class="fa fa-users text-accent text-2xl"></i>
                            </div>
                            <div class="space-y-4">
                                <div>
                                    <div class="flex justify-between mb-1">
                                        <span class="text-sm font-medium">14-16岁</span>
                                        <span class="text-sm font-medium">38%</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-accent h-2 rounded-full" style="width: 38%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between mb-1">
                                        <span class="text-sm font-medium">16-18岁</span>
                                        <span class="text-sm font-medium">62%</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-accent h-2 rounded-full" style="width: 62%"></div>
                                    </div>
                                </div>
                            </div>
                            <p class="text-sm text-gray-500 mt-4">数据来源：中国预防青少年犯罪研究会（2023）</p>
                        </div>

                        <!-- 统计卡片2 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <div class="flex items-center justify-between mb-4">
                                <h3 class="text-xl font-bold">城乡分布</h3>
                                <i class="fa fa-map-marker text-accent text-2xl"></i>
                            </div>
                            <div class="space-y-4">
                                <div>
                                    <div class="flex justify-between mb-1">
                                        <span class="text-sm font-medium">城市</span>
                                        <span class="text-sm font-medium">58%</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-accent h-2 rounded-full" style="width: 58%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between mb-1">
                                        <span class="text-sm font-medium">农村</span>
                                        <span class="text-sm font-medium">42%</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-accent h-2 rounded-full" style="width: 42%"></div>
                                    </div>
                                </div>
                            </div>
                            <p class="text-sm text-gray-500 mt-4">数据来源：最高人民法院（2024）</p>
                        </div>

                        <!-- 统计卡片3 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <div class="flex items-center justify-between mb-4">
                                <h3 class="text-xl font-bold">性别比例</h3>
                                <i class="fa fa-venus-mars text-accent text-2xl"></i>
                            </div>
                            <div class="space-y-4">
                                <div>
                                    <div class="flex justify-between mb-1">
                                        <span class="text-sm font-medium">男性</span>
                                        <span class="text-sm font-medium">89%</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-accent h-2 rounded-full" style="width: 89%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between mb-1">
                                        <span class="text-sm font-medium">女性</span>
                                        <span class="text-sm font-medium">11%</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-accent h-2 rounded-full" style="width: 11%"></div>
                                    </div>
                                </div>
                            </div>
                            <p class="text-sm text-gray-500 mt-4">数据来源：公安部（2023）</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 原因分析 -->
            <section id="causes" class="py-20 bg-gray-50">
                <div class="container mx-auto px-6">
                    <div class="text-center mb-16">
                        <h2 class="text-[clamp(1.75rem,3vw,2.5rem)] font-bold mb-4">未成年犯罪原因分析</h2>
                        <p class="text-gray-600 max-w-3xl mx-auto">
                            未成年犯罪是家庭、学校、社会三方责任缺失的综合体现。中国青少年研究中心2024年调研显示，73%的涉案未成年人存在家庭监管缺位，41%反映学校法治教育流于形式。以下从三大核心维度展开深度分析，揭示问题背后的深层动因。
                        </p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                        <!-- 原因卡片1 -->
                        <div class="bg-white rounded-xl shadow-lg overflow-hidden card-hover">
                            <div class="h-48 overflow-hidden">
                                <img src="jr.jpg" alt="家庭环境对未成年人的影响"
                                    class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
                            </div>
                            <div class="p-6">
                                <h3 class="text-xl font-bold mb-3 flex items-center">
                                    <i class="fa fa-home text-accent mr-2"></i>
                                    家庭环境因素
                                </h3>
                                <p class="text-gray-600 mb-4">
                                    家庭教育的缺失往往是犯罪的第一诱因：中国预防青少年犯罪研究会2023年专项调研显示，父母离异家庭的未成年人犯罪率较完整家庭高出27%；存在家庭暴力的家庭中，子女出现攻击性行为的概率是正常家庭的3.2倍。具体表现为：
                                </p>
                                <div class="space-y-2">
                                    <div class="flex items-center">
                                        <div class="w-2 h-2 rounded-full bg-accent mr-2"></div>
                                        <span class="text-sm">父母离异家庭的孩子犯罪率高出27%</span>
                                    </div>
                                    <div class="flex items-center">
                                        <div class="w-2 h-2 rounded-full bg-accent mr-2"></div>
                                        <span class="text-sm">家庭暴力环境下成长的孩子犯罪倾向更高</span>
                                    </div>
                                    <div class="flex items-center">
                                        <div class="w-2 h-2 rounded-full bg-accent mr-2"></div>
                                        <span class="text-sm">疏于管教的孩子更容易受到不良影响</span>
                                    </div>
                                </div>
                                <p class="text-sm text-gray-500 mt-4">数据来源：中国青少年研究中心（2024）</p>
                            </div>
                        </div>

                        <!-- 原因卡片2 -->
                        <div class="bg-white rounded-xl shadow-lg overflow-hidden card-hover">
                            <div class="h-48 overflow-hidden">
                                <img src="xx.jpg" alt="学校教育对未成年人的影响"
                                    class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
                            </div>
                            <div class="p-6">
                                <h3 class="text-xl font-bold mb-3 flex items-center">
                                    <i class="fa fa-graduation-cap text-accent mr-2"></i>
                                    学校教育因素
                                </h3>
                                <p class="text-gray-600 mb-4">学校教育的不足、师生关系不和谐、校园暴力等问题，对未成年人的成长和价值观形成产生负面影响。</p>
                                <div class="space-y-2">
                                    <div class="flex items-center">
                                        <div class="w-2 h-2 rounded-full bg-accent mr-2"></div>
                                        <span class="text-sm">辍学学生犯罪率是在校学生的4.5倍</span>
                                    </div>
                                    <div class="flex items-center">
                                        <div class="w-2 h-2 rounded-full bg-accent mr-2"></div>
                                        <span class="text-sm">遭受校园欺凌的学生更容易产生心理问题</span>
                                    </div>
                                    <div class="flex items-center">
                                        <div class="w-2 h-2 rounded-full bg-accent mr-2"></div>
                                        <span class="text-sm">法制教育缺失导致法律意识淡薄</span>
                                    </div>
                                </div>
                                <p class="text-sm text-gray-500 mt-4">数据来源：教育部基础教育司（2023）</p>
                            </div>
                        </div>

                        <!-- 原因卡片3 -->
                        <div class="bg-white rounded-xl shadow-lg overflow-hidden card-hover">
                            <div class="h-48 overflow-hidden">
                                <img src="sn.jpg" alt="社会环境对未成年人的影响"
                                    class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
                            </div>
                            <div class="p-6">
                                <h3 class="text-xl font-bold mb-3 flex items-center">
                                    <i class="fa fa-users text-accent mr-2"></i>
                                    社会环境因素
                                </h3>
                                <p class="text-gray-600 mb-4">社会不良文化、网络环境、社区环境等外部因素，对未成年人的行为和价值观产生潜移默化的影响。</p>
                                <div class="space-y-2">
                                    <div class="flex items-center">
                                        <div class="w-2 h-2 rounded-full bg-accent mr-2"></div>
                                        <span class="text-sm">每天上网超过4小时的青少年犯罪率增加35%</span>
                                    </div>
                                    <div class="flex items-center">
                                        <div class="w-2 h-2 rounded-full bg-accent mr-2"></div>
                                        <span class="text-sm">不良社区环境与青少年犯罪呈正相关</span>
                                    </div>
                                    <div class="flex items-center">
                                        <div class="w-2 h-2 rounded-full bg-accent mr-2"></div>
                                        <span class="text-sm">暴力、色情内容容易诱发青少年模仿犯罪</span>
                                    </div>
                                </div>
                                <p class="text-sm text-gray-500 mt-4">数据来源：中国社会科学院社会学研究所（2024）</p>
                            </div>
                        </div>
                    </div>

                    <!-- 图表3：原因影响程度分析 -->
                    <div class="mt-16 bg-white rounded-xl shadow-lg p-6 card-hover">
                        <h3 class="text-xl font-bold mb-4 flex items-center">
                            <i class="fa fa-bar-chart text-accent mr-2"></i>
                            各因素对未成年犯罪的影响程度
                        </h3>
                        <div class="h-80">
                            <canvas id="factorsChart"></canvas>
                        </div>
                        <p class="text-sm text-gray-500 mt-2">数据来源：中国青少年研究中心（2024）</p>
                    </div>
                </div>
            </section>

            <div class="container mx-auto px-6 py-8 text-center">
                <p class="text-xl text-gray-700" style="font-family: 楷体;">
                    那些冰冷的百分比背后，是课桌上未写完的作业、书包里揉皱的日记、操场边被风吹散的笑声——每个数字都曾是会疼会笑的少年。让我们轻轻推开案例的门，在具体的故事里触摸成长的裂痕：或许是一次被忽视的委屈，或许是一句没说出口的求助，或许是一道跨不过去的迷茫。这些裂痕，终将成为我们寻找修复答案的起点。
                </p>
            </div>

            <!-- 典型案例 -->
            <section id="cases" class="py-20 bg-neutral">
                <div class="container mx-auto px-6">
                    <div class="text-center mb-16">
                        <h2 class="text-[clamp(1.75rem,3vw,2.5rem)] font-bold mb-4">典型案例分析</h2>
                        <p class="text-gray-600 max-w-3xl mx-auto">通过实际案例，深入了解未成年犯罪的特点、原因及法律后果，从中吸取教训，预防类似事件的发生。</p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <!-- 案例1 -->
                        <div class="bg-white rounded-xl shadow-lg overflow-hidden card-hover">
                            <div class="p-6 border-b border-gray-100">
                                <h3 class="text-xl font-bold mb-2">案例一：校园欺凌引发的故意伤害案</h3>
                                <p class="text-gray-500 text-sm">
                                    2023年9月至2024年3月，16岁的李某（化名）在中学就读期间，因体型瘦小长期被3名同班同学辱骂、推搡，并被索要零花钱累计超2000元。2024年4月15日课间，李某再次被围堵索要财物时，情绪失控掏出随身携带的折叠刀刺伤其中1名同学，致其脾脏破裂重伤二级。
                            </div>
                            <div class="p-6">
                                <div class="flex items-start mb-4">
                                    <div class="flex-shrink-0 mr-4">
                                        <div
                                            class="w-10 h-10 rounded-full bg-accent/10 flex items-center justify-center">
                                            <i class="fa fa-gavel text-accent"></i>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="font-bold mb-1">案件结果</h4>
                                        <p class="text-gray-600 text-sm">
                                            法院审理认为，李某因长期遭受欺凌导致情绪失控，且案发后主动投案并赔偿被害人医疗费，结合其未满18周岁的法定从轻情节，以故意伤害罪判处有期徒刑3年，缓刑4年；同时发出《家庭教育指导令》，要求其父母接受专业心理辅导。
                                    </div>
                                </div>
                                <div class="flex items-start mb-4">
                                    <div class="flex-shrink-0 mr-4">
                                        <div
                                            class="w-10 h-10 rounded-full bg-accent/10 flex items-center justify-center">
                                            <i class="fa fa-lightbulb-o text-accent"></i>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="font-bold mb-1">案件启示</h4>
                                        <p class="text-gray-600 text-sm">长期遭受欺凌可能导致未成年人心理扭曲，采取极端行为。学校和家长应重视校园欺凌问题，及时干预。
                                        </p>
                                        <p class="text-red-500">警示：未成年人犯罪不仅伤害他人，更会毁掉自己的未来，需时刻自重自律！</p>
                                    </div>
                                </div>
                                <a href="javascript:void(0)"
                                    class="text-accent hover:text-accent/80 font-medium flex items-center">

                                </a>
                            </div>
                        </div>

                        <!-- 案例2 -->
                        <div class="bg-white rounded-xl shadow-lg overflow-hidden card-hover">
                            <div class="p-6 border-b border-gray-100">
                                <h3 class="text-xl font-bold mb-2">案例二：未成年人网络盗窃案</h3>
                                <p class="text-gray-500 text-sm">
                                    17岁的张某（化名）因沉迷《XX荣耀》手游，为购买皮肤和装备，2024年2月至5月期间，先后6次趁邻居外出时，通过撬窗方式盗窃手机、现金等财物，涉案金额累计1.2万元。案发时其游戏账号充值记录显示，半年内消费达8000余元。
                            </div>
                            <div class="p-6">
                                <div class="flex items-start mb-4">
                                    <div class="flex-shrink-0 mr-4">
                                        <div
                                            class="w-10 h-10 rounded-full bg-accent/10 flex items-center justify-center">
                                            <i class="fa fa-gavel text-accent"></i>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="font-bold mb-1">案件结果</h4>
                                        <p class="text-gray-600 text-sm">
                                            法院审理认为，张某虽未满18周岁，但多次实施盗窃且数额较大，依法以盗窃罪判处有期徒刑1年6个月，缓刑2年；同时责令其监护人赔偿被害人损失，并限制其电子设备使用时间。
                                    </div>
                                </div>
                                <div class="flex items-start mb-4">
                                    <div class="flex-shrink-0 mr-4">
                                        <div
                                            class="w-10 h-10 rounded-full bg-accent/10 flex items-center justify-center">
                                            <i class="fa fa-lightbulb-o text-accent"></i>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="font-bold mb-1">案件启示</h4>
                                        <p class="text-gray-600 text-sm">未成年人缺乏自制力，容易沉迷网络。家长应加强监管，引导孩子正确使用网络，树立正确消费观。
                                        </p>
                                        <p class="text-red-500">警示：网络不是法外之地，未成年人需树立正确的财产观，勿因小利触碰法律红线！</p>
                                    </div>
                                </div>
                                <a href="javascript:void(0)"
                                    class="text-accent hover:text-accent/80 font-medium flex items-center">

                                </a>
                            </div>
                        </div>

                        <!-- 案例3 -->
                        <div class="bg-white rounded-xl shadow-lg overflow-hidden card-hover">
                            <div class="p-6 border-b border-gray-100">
                                <h3 class="text-xl font-bold mb-2">案例三：未成年人结伙抢劫案</h3>
                                <p class="text-gray-500 text-sm">
                                    2024年3月至4月，15岁王某、16岁李某等4人（均辍学）在某中学附近，以“借零花钱”为名，采用言语威胁、推搡等方式，先后对7名学生实施抢劫，累计劫取现金、手机等财物价值5000余元。
                            </div>
                            <div class="p-6">
                                <div class="flex items-start mb-4">
                                    <div class="flex-shrink-0 mr-4">
                                        <div
                                            class="w-10 h-10 rounded-full bg-accent/10 flex items-center justify-center">
                                            <i class="fa fa-gavel text-accent"></i>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="font-bold mb-1">案件结果</h4>
                                        <p class="text-gray-600 text-sm">
                                            法院审理认为，4人结伙多次抢劫，社会危害性较大，但因均未满18周岁且部分具有坦白情节，分别判处有期徒刑2-4年不等，并处罚金；同时移送专门学校接受行为矫正教育。
                                    </div>
                                </div>
                                <div class="flex items-start mb-4">
                                    <div class="flex-shrink-0 mr-4">
                                        <div
                                            class="w-10 h-10 rounded-full bg-accent/10 flex items-center justify-center">
                                            <i class="fa fa-lightbulb-o text-accent"></i>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="font-bold mb-1">案件启示</h4>
                                        <p class="text-gray-600 text-sm">
                                            未成年人辨别是非能力弱，容易受不良同伴影响。家长和学校应关注孩子的社交圈子，引导建立健康的人际关系。</p>
                                        <p class="text-red-500">警示：结伙作案危害更大，未成年人应远离不良群体，遇到诱惑时需坚守法律底线！</p>
                                    </div>
                                </div>
                                <a href="javascript:void(0)"
                                    class="text-accent hover:text-accent/80 font-medium flex items-center">

                                </a>
                            </div>
                        </div>

                        <!-- 案例4 -->
                        <div class="bg-white rounded-xl shadow-lg overflow-hidden card-hover">
                            <div class="p-6 border-b border-gray-100">
                                <h3 class="text-xl font-bold mb-2">案例四：未成年人酒后寻衅滋事案</h3>
                                <p class="text-gray-500 text-sm">
                                    2024年5月20日晚，17岁的陈某（化名）与社会青年聚餐时饮用啤酒约3瓶后，在步行街无故踢踹路边共享单车，遇路人劝阻时挥拳殴打，致1名老人倒地骨折，另损坏共享单车3辆、路灯1盏。
                            </div>
                            <div class="p-6">
                                <div class="flex items-start mb-4">
                                    <div class="flex-shrink-0 mr-4">
                                        <div
                                            class="w-10 h-10 rounded-full bg-accent/10 flex items-center justify-center">
                                            <i class="fa fa-gavel text-accent"></i>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="font-bold mb-1">案件结果</h4>
                                        <p class="text-gray-600 text-sm">
                                            法院审理认为，陈某酒后实施暴力行为，破坏社会秩序，以寻衅滋事罪判处有期徒刑1年，缓刑1年6个月；同时判令其赔偿被害人医疗费、共享单车及路灯维修费共计2.3万元。
                                    </div>
                                </div>
                                <div class="flex items-start mb-4">
                                    <div class="flex-shrink-0 mr-4">
                                        <div
                                            class="w-10 h-10 rounded-full bg-accent/10 flex items-center justify-center">
                                            <i class="fa fa-lightbulb-o text-accent"></i>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="font-bold mb-1">案件启示</h4>
                                        <p class="text-gray-600 text-sm">未成年人饮酒不仅危害身体健康，还容易引发冲动行为。家长应加强对孩子的监管，禁止未成年人饮酒。
                                        </p>
                                        <p class="text-red-500">警示：饮酒滋事同样违法，未成年人需严格遵守法律对饮酒年龄的限制，避免因冲动酿成大错！</p>
                                    </div>
                                </div>
                                <a href="javascript:void(0)"
                                    class="text-accent hover:text-accent/80 font-medium flex items-center">

                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <div class="container mx-auto px-6 py-8 text-center">
                <p class="text-xl text-gray-700" style="font-family: 楷体;">
                    每个案例都是一声警钟，震醒我们对青春的守护责任。与其等到裂痕出现，不如提前筑起温暖的防线——这，正是我们接下来要探讨的「预防」的意义。</p>
            </div>

            <!-- 预防措施 -->
            <section id="prevention" class="py-20 bg-gray-50">
                <div class="container mx-auto px-6">
                    <div class="text-center mb-16">
                        <h2 class="text-[clamp(1.75rem,3vw,2.5rem)] font-bold mb-4">预防未成年犯罪措施</h2>
                        <p class="text-gray-600 max-w-3xl mx-auto">预防未成年犯罪需要家庭、学校、社会和司法部门的共同努力。以下是一些有效的预防措施和建议。</p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                        <!-- 预防措施1 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <div class="w-14 h-14 rounded-full bg-accent/10 flex items-center justify-center mb-6">
                                <i class="fa fa-home text-accent text-2xl"></i>
                            </div>
                            <h3 class="text-xl font-bold mb-3">家庭预防</h3>
                            <ul class="space-y-3">
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>建立良好的亲子关系（据2023年青少年心理健康报告，每周3次以上深度沟通的家庭，子女行为偏差率降低42%），建议每周至少安排3次30分钟以上的亲子对话</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>树立正确的家庭教育观念，避免溺爱或粗暴教育</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>关注孩子的日常行为和心理变化（2023年青少年行为监测数据显示，每月记录3次以上行为变化的家庭，问题发现率提升58%），建议家长每月建立行为观察记录</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>引导孩子正确使用网络和社交媒体</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>营造和谐的家庭氛围，避免家庭暴力</span>
                                </li>
                            </ul>
                        </div>

                        <!-- 预防措施2 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <div class="w-14 h-14 rounded-full bg-accent/10 flex items-center justify-center mb-6">
                                <i class="fa fa-graduation-cap text-accent text-2xl"></i>
                            </div>
                            <h3 class="text-xl font-bold mb-3">学校预防</h3>
                            <ul class="space-y-3">
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>加强法制教育（教育部2022年统计显示，每学期开展5次以上法制教育的学校，学生违法知晓率达91%），建议每学期开展5次以上法制教育活动</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>开展心理健康教育（2022年学校心理干预报告指出，配备专职心理教师的学校，心理问题干预成功率达85%），建议每所学校至少配备1名专职心理教师</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>加强校园安全管理，预防校园欺凌和暴力事件</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>关注学习困难学生，避免学生辍学</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>建立家校合作机制，共同关注学生成长</span>
                                </li>
                            </ul>
                        </div>

                        <!-- 预防措施3 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <div class="w-14 h-14 rounded-full bg-accent/10 flex items-center justify-center mb-6">
                                <i class="fa fa-users text-accent text-2xl"></i>
                            </div>
                            <h3 class="text-xl font-bold mb-3">社会预防</h3>
                            <ul class="space-y-3">
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>净化社会文化环境，减少不良文化对未成年人的影响</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>加强对网吧、游戏厅等场所的管理（文化和旅游部2023年检查数据，实施实名登记的场所，未成年人进入率下降72%），建议严格执行场所实名登记制度</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>建立社区青少年活动中心（2023年社区服务白皮书数据，覆盖500人以上的活动中心，青少年课余不良行为减少63%），建议社区每月组织3次公益活动并覆盖80%以上适龄青少年</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>加强对闲散青少年的管理和帮助</span>
                                </li>
                                <li class="flex items-start">
                                    <i class="fa fa-check-circle text-accent mt-1 mr-2"></i>
                                    <span>发挥社会组织作用，开展关爱未成年人活动</span>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <!-- 资源链接 -->
                    <div class="mt-16 bg-white rounded-xl shadow-lg p-8">
                        <h3 class="text-xl font-bold mb-6">相关资源链接</h3>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            <a href="https://www.12355.net/" target="_blank"
                                class="flex items-center p-4 border border-gray-200 rounded-lg hover:border-accent transition-all group">
                                <div
                                    class="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center mr-4 group-hover:bg-accent group-hover:text-white transition-all">
                                    <i class="fa fa-phone text-accent group-hover:text-white"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold">12355青少年服务台</h4>
                                    <p class="text-gray-500 text-sm">提供心理咨询、法律援助等服务</p>
                                </div>
                            </a>

                            <a href="https://www.chinacourt.org/" target="_blank"
                                class="flex items-center p-4 border border-gray-200 rounded-lg hover:border-accent transition-all group">
                                <div
                                    class="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center mr-4 group-hover:bg-accent group-hover:text-white transition-all">
                                    <i class="fa fa-gavel text-accent group-hover:text-white"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold">中国法院网</h4>
                                    <p class="text-gray-500 text-sm">提供法律法规查询和司法案例</p>
                                </div>
                            </a>

                            <a href="https://www.61child.com/" target="_blank"
                                class="flex items-center p-4 border border-gray-200 rounded-lg hover:border-accent transition-all group">
                                <div
                                    class="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center mr-4 group-hover:bg-accent group-hover:text-white transition-all">
                                    <i class="fa fa-book text-accent group-hover:text-white"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold">中国未成年人网</h4>
                                    <p class="text-gray-500 text-sm">提供未成年人保护相关资讯</p>
                                </div>
                            </a>

                            <a href="https://www.moe.gov.cn/" target="_blank"
                                class="flex items-center p-4 border border-gray-200 rounded-lg hover:border-accent transition-all group">
                                <div
                                    class="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center mr-4 group-hover:bg-accent group-hover:text-white transition-all">
                                    <i class="fa fa-graduation-cap text-accent group-hover:text-white"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold">教育部官网</h4>
                                    <p class="text-gray-500 text-sm">提供教育政策和资源</p>
                                </div>
                            </a>

                            <a href="https://www.ccps.gov.cn/" target="_blank"
                                class="flex items-center p-4 border border-gray-200 rounded-lg hover:border-accent transition-all group">
                                <div
                                    class="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center mr-4 group-hover:bg-accent group-hover:text-white transition-all">
                                    <i class="fa fa-shield text-accent group-hover:text-white"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold">中国预防青少年犯罪研究会</h4>
                                    <p class="text-gray-500 text-sm">专注于青少年犯罪预防研究</p>
                                </div>
                            </a>

                            <a href="https://www.12309.gov.cn/" target="_blank"
                                class="flex items-center p-4 border border-gray-200 rounded-lg hover:border-accent transition-all group">
                                <div
                                    class="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center mr-4 group-hover:bg-accent group-hover:text-white transition-all">
                                    <i class="fa fa-balance-scale text-accent group-hover:text-white"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold">12309中国检察网</h4>
                                    <p class="text-gray-500 text-sm">提供未成年人司法保护相关信息</p>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </section>

            <div class="container mx-auto px-6 py-8 text-center">
                <p class="text-xl text-gray-700" style="font-family: 楷体;">
                    守护青春不是一句口号，更需要具体的行动指南与支持力量。以下这些资源，愿成为你我守护路上的「工具箱」，让每一份关怀都能落到实处。</p>
            </div>

            <!-- 相关资源 -->
            <section id="resources" class="py-20 bg-neutral">
                <div class="container mx-auto px-6">
                    <div class="text-center mb-16">
                        <h2 class="text-[clamp(1.75rem,3vw,2.5rem)] font-bold mb-4">相关法律法规与资源</h2>
                        <p class="text-gray-600 max-w-3xl mx-auto">了解与未成年人保护和犯罪预防相关的法律法规，获取专业帮助和支持。</p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <!-- 法律法规 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <h3 class="text-xl font-bold mb-4 flex items-center">
                                <i class="fa fa-gavel text-accent mr-2"></i>
                                相关法律法规
                            </h3>
                            <ul class="space-y-3">
                                <li>
                                    <a href="https://www.npc.gov.cn/wxzl/wxfl/202010/t20201017_2203416.html"
                                        target="_blank"
                                        class="flex items-center p-3 border border-gray-100 rounded-lg hover:border-accent hover:bg-accent/5 transition-all">
                                        <i class="fa fa-file-text-o text-accent mr-3"></i>
                                        <div>
                                            <h4 class="font-medium">中华人民共和国未成年人保护法</h4>
                                            <p class="text-gray-500 text-sm">2020年修订，全面保障未成年人权益</p>
                                        </div>
                                    </a>
                                </li>
                                <li>
                                    <a href="https://www.npc.gov.cn/wxzl/wxfl/202012/t20201226_2209775.html"
                                        target="_blank"
                                        class="flex items-center p-3 border border-gray-100 rounded-lg hover:border-accent hover:bg-accent/5 transition-all">
                                        <i class="fa fa-file-text-o text-accent mr-3"></i>
                                        <div>
                                            <h4 class="font-medium">中华人民共和国预防未成年人犯罪法</h4>
                                            <p class="text-gray-500 text-sm">2020年修订，预防未成年人犯罪</p>
                                        </div>
                                    </a>
                                </li>
                                <li>
                                    <a href="https://www.npc.gov.cn/wxzl/wxfl/202012/t20201226_2209774.html"
                                        target="_blank"
                                        class="flex items-center p-3 border border-gray-100 rounded-lg hover:border-accent hover:bg-accent/5 transition-all">
                                        <i class="fa fa-file-text-o text-accent mr-3"></i>
                                        <div>
                                            <h4 class="font-medium">中华人民共和国刑法（未成年人相关条款）</h4>
                                            <p class="text-gray-500 text-sm">规定未成年人犯罪的刑事责任</p>
                                        </div>
                                    </a>
                                </li>
                                <li>
                                    <a href="https://www.npc.gov.cn/wxzl/wxfl/201801/t20180129_2043363.html"
                                        target="_blank"
                                        class="flex items-center p-3 border border-gray-100 rounded-lg hover:border-accent hover:bg-accent/5 transition-all">
                                        <i class="fa fa-file-text-o text-accent mr-3"></i>
                                        <div>
                                            <h4 class="font-medium">中华人民共和国义务教育法</h4>
                                            <p class="text-gray-500 text-sm">保障未成年人接受义务教育的权利</p>
                                        </div>
                                    </a>
                                </li>
                            </ul>
                        </div>

                        <!-- 求助热线 -->
                        <div class="bg-white rounded-xl shadow-lg p-6 card-hover">
                            <h3 class="text-xl font-bold mb-4 flex items-center">
                                <i class="fa fa-phone text-accent mr-2"></i>
                                求助热线
                            </h3>
                            <ul class="space-y-3">
                                <li>
                                    <a href="tel:12355"
                                        class="flex items-center p-3 border border-gray-100 rounded-lg hover:border-accent hover:bg-accent/5 transition-all">
                                        <i class="fa fa-headphones text-accent mr-3"></i>
                                        <div>
                                            <h4 class="font-medium">12355青少年服务热线</h4>
                                            <p class="text-gray-500 text-sm">提供心理咨询、法律援助、就业指导等服务</p>
                                        </div>
                                    </a>
                                </li>
                                <li>
                                    <a href="tel:12309"
                                        class="flex items-center p-3 border border-gray-100 rounded-lg hover:border-accent hover:bg-accent/5 transition-all">
                                        <i class="fa fa-balance-scale text-accent mr-3"></i>
                                        <div>
                                            <h4 class="font-medium">12309检察服务热线</h4>
                                            <p class="text-gray-500 text-sm">提供未成年人司法保护相关咨询</p>
                                        </div>
                                    </a>
                                </li>
                                <li>
                                    <a href="tel:12348"
                                        class="flex items-center p-3 border border-gray-100 rounded-lg hover:border-accent hover:bg-accent/5 transition-all">
                                        <i class="fa fa-gavel text-accent mr-3"></i>
                                        <div>
                                            <h4 class="font-medium">12348公共法律服务热线</h4>
                                            <p class="text-gray-500 text-sm">提供免费法律咨询服务</p>
                                        </div>
                                    </a>
                                </li>
                                <li>
                                    <a href="tel:12355"
                                        class="flex items-center p-3 border border-gray-100 rounded-lg hover:border-accent hover:bg-accent/5 transition-all">
                                        <i class="fa fa-heartbeat text-accent mr-3"></i>
                                        <div>
                                            <h4 class="font-medium">12355心理援助热线</h4>
                                            <p class="text-gray-500 text-sm">提供专业心理咨询服务</p>
                                        </div>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <!-- 参考书籍 -->
                    <div class="mt-12 bg-white rounded-xl shadow-lg p-6 card-hover">
                        <h3 class="text-xl font-bold mb-4 flex items-center">
                            <i class="fa fa-book text-accent mr-2"></i>
                            参考书籍与文献
                        </h3>
                        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                            <div
                                class="border border-gray-100 rounded-lg overflow-hidden hover:shadow-md transition-all">
                                <div class="h-40 bg-gray-100">
                                    <img src="https://picsum.photos/id/24/300/400" alt="《未成年人犯罪预防与矫治》封面"
                                        class="w-full h-full object-cover">
                                </div>
                                <div class="p-4">
                                    <h4 class="font-bold mb-1">未成年人犯罪预防与矫治</h4>
                                    <p class="text-gray-500 text-sm mb-2">作者：中国青少年研究中心</p>
                                    <a href="https://book.douban.com/subject/30453375/" target="_blank"
                                        class="text-accent hover:text-accent/80 text-sm">查看详情</a>
                                </div>
                            </div>

                            <div
                                class="border border-gray-100 rounded-lg overflow-hidden hover:shadow-md transition-all">
                                <div class="h-40 bg-gray-100">
                                    <img src="shu2.jpg" alt="《未成年人司法制度研究》封面" class="w-full h-full object-cover">
                                </div>
                                <div class="p-4">
                                    <h4 class="font-bold mb-1">万千心理·犯罪心理学</h4>
                                    <p class="text-gray-500 text-sm mb-2">作者：柯特·R.巴托尔</p>
                                    <a href="https://book.douban.com/subject/30453376/" target="_blank"
                                        class="text-accent hover:text-accent/80 text-sm">查看详情</a>
                                </div>
                            </div>

                            <div
                                class="border border-gray-100 rounded-lg overflow-hidden hover:shadow-md transition-all">
                                <div class="h-40 bg-gray-100">
                                    <img src="shu1.jpg" alt="《心理神探》封面" class="w-full h-full object-cover">
                                </div>
                                <div class="p-4">
                                    <h4 class="font-bold mb-1">心理神探：我与FBL心理画像术</h4>
                                    <p class="text-gray-500 text-sm mb-2">作者：约翰·道格拉斯</p>
                                    <a href="https://book.douban.com/subject/30453377/" target="_blank"
                                        class="text-accent hover:text-accent/80 text-sm">查看详情</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>



            <!-- 页脚 -->
            <footer class="bg-primary text-white py-12">
                <div class="container mx-auto px-6">
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                        <div>
                            <h3 class="text-lg font-bold mb-4">法治护航</h3>
                            <p class="text-white/70 mb-4">关注未成年人健康成长，预防和减少未成年人犯罪，营造良好的社会环境。</p>
                            <div class="flex space-x-4">
                                <a href="#" class="text-white/70 hover:text-white transition-all">
                                    <i class="fa fa-weixin"></i>
                                </a>
                                <a href="#" class="text-white/70 hover:text-white transition-all">
                                    <i class="fa fa-weibo"></i>
                                </a>
                                <a href="#" class="text-white/70 hover:text-white transition-all">
                                    <i class="fa fa-qq"></i>
                                </a>
                            </div>
                        </div>

                        <div>
                            <h3 class="text-lg font-bold mb-4">快速链接</h3>
                            <ul class="space-y-2">
                                <li><a href="#home" class="text-white/70 hover:text-white transition-all">首页</a></li>
                                <li><a href="#overview" class="text-white/70 hover:text-white transition-all">现状概览</a>
                                </li>
                                <li><a href="#causes" class="text-white/70 hover:text-white transition-all">原因分析</a>
                                </li>
                                <li><a href="#cases" class="text-white/70 hover:text-white transition-all">典型案例</a></li>
                                <li><a href="#prevention" class="text-white/70 hover:text-white transition-all">预防措施</a>
                                </li>
                            </ul>
                        </div>

                        <div>
                            <h3 class="text-lg font-bold mb-4">相关资源</h3>
                            <ul class="space-y-2">
                                <li><a href="#resources" class="text-white/70 hover:text-white transition-all">法律法规</a>
                                </li>
                                <li><a href="#resources" class="text-white/70 hover:text-white transition-all">求助热线</a>
                                </li>
                                <li><a href="#resources" class="text-white/70 hover:text-white transition-all">参考书籍</a>
                                </li>
                                <li><a href="https://www.12355.net/" target="_blank"
                                        class="text-white/70 hover:text-white transition-all">12355青少年服务台</a></li>
                                <li><a href="https://www.chinacourt.org/" target="_blank"
                                        class="text-white/70 hover:text-white transition-all">中国法院网</a></li>
                            </ul>
                        </div>

                        <div>
                            <h3 class="text-lg font-bold mb-4">联系我们</h3>
                            <ul class="space-y-2">
                                <li class="flex items-center">
                                    <i class="fa fa-map-marker mr-2 text-white/70"></i>
                                    <span class="text-white/70">xx省XX市</span>
                                </li>
                                <li class="flex items-center">
                                    <i class="fa fa-phone mr-2 text-white/70"></i>
                                    <span class="text-white/70">010-12345678</span>
                                </li>
                                <li class="flex items-center">
                                    <i class="fa fa-envelope mr-2 text-white/70"></i>
                                    <span class="text-white/70">contact@example.com</span>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="border-t border-white/10 mt-8 pt-8 text-center text-white/50 text-sm">
                        <p>© 2025 第13届未来设计设·全国高校数字艺术设计大赛 比赛专用.</p>
                    </div>
                </div>
            </footer>
        </main>

        <!-- 回到顶部按钮 -->
        <button id="backToTop"
            class="fixed bottom-6 right-6 w-12 h-12 rounded-full bg-accent text-white shadow-lg flex items-center justify-center opacity-0 invisible transition-all z-50">
            <i class="fa fa-arrow-up"></i>
        </button>

        <!-- JavaScript -->
        <script>
            // 导航栏滚动效果
            const sidebar = document.getElementById('sidebar');
            let lastScrollTop = 0;

            window.addEventListener('scroll', function () {
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

                if (scrollTop > 100) {
                    sidebar.classList.add('shadow-xl');
                    document.getElementById('backToTop').classList.remove('opacity-0', 'invisible');
                    document.getElementById('backToTop').classList.add('opacity-100', 'visible');
                } else {
                    sidebar.classList.remove('shadow-xl');
                    document.getElementById('backToTop').classList.add('opacity-0', 'invisible');
                    document.getElementById('backToTop').classList.remove('opacity-100', 'visible');
                }

                lastScrollTop = scrollTop;
            });

            // 回到顶部功能
            document.getElementById('backToTop').addEventListener('click', function () {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });

            // 平滑滚动
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();

                    const targetId = this.getAttribute('href');
                    if (targetId === '#') return;

                    const targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        targetElement.scrollIntoView({
                            behavior: 'smooth'
                        });
                    }
                });
            });

            // 图表初始化
            document.addEventListener('DOMContentLoaded', function () {
                // 图表1：未成年犯罪人数趋势
                const crimeTrendCtx = document.getElementById('crimeTrendChart').getContext('2d');
                new Chart(crimeTrendCtx, {
                    type: 'line',
                    data: {
                        labels: ['2020', '2021', '2022', '2023', '2024'],
                        datasets: [{
                            label: '未成年犯罪人数',
                            data: [3.3, 3.5, 3.8, 3.6, 3.4],
                            borderColor: '#ff3d00',
                            backgroundColor: 'rgba(255, 61, 0, 0.1)',
                            tension: 0.3,
                            fill: true
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'top',
                            },
                            tooltip: {
                                mode: 'index',
                                intersect: false,
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: false,
                                title: {
                                    display: true,
                                    text: '万人'
                                }
                            }
                        }
                    }
                });

                // 图表2：犯罪类型分布
                const crimeTypeCtx = document.getElementById('crimeTypeChart').getContext('2d');
                new Chart(crimeTypeCtx, {
                    type: 'doughnut',
                    data: {
                        labels: ['抢劫罪', '盗窃罪', '故意伤害罪', '寻衅滋事罪', '强奸罪', '其他'],
                        datasets: [{
                            data: [28, 25, 20, 15, 7, 5],
                            backgroundColor: [
                                '#ff3d00',
                                '#ff7539',
                                '#ff9a62',
                                '#ffbc8f',
                                '#ffddbd',
                                '#f5f5f5'
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'right',
                            }
                        },
                        cutout: '65%'
                    }
                });

                // 图表3：各因素对未成年犯罪的影响程度
                const factorsCtx = document.getElementById('factorsChart').getContext('2d');
                new Chart(factorsCtx, {
                    type: 'bar',
                    data: {
                        labels: ['家庭教育缺失', '学校教育不足', '社会不良影响', '心理问题', '法律意识淡薄', '经济因素'],
                        datasets: [{
                            label: '影响程度（百分比）',
                            data: [38, 25, 20, 12, 10, 5],
                            backgroundColor: '#ff3d00',
                            borderRadius: 6
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                display: false
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 50,
                                ticks: {
                                    callback: function (value) {
                                        return value + '%';
                                    }
                                }
                            }
                        }
                    }
                });
            });
        </script>

    </body>

</html>