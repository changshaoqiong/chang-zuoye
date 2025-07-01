import Navbar from "@/components/Navbar";
import ExerciseCard from "@/components/ExerciseCard";
import exercises from "@/data/exercises.json";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-slate-50">
      <Navbar />
      <main className="flex-grow container mx-auto px-4 py-8">
        <header className="text-center mb-12">
          <h1 className="text-4xl font-bold text-slate-800 mb-2">
            《Web前端开发》课程练习
          </h1>
          <p className="text-lg text-slate-600">
            欢迎来到课程练习展示平台，这里汇集了各个阶段的学习成果。
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {exercises.map((exercise) => (
            <ExerciseCard
              key={exercise.id}
              title={exercise.title}
              description={exercise.description}
              imageUrl={exercise.imageUrl}
              link={exercise.link}
              tags={exercise.tags}
            />
          ))}
        </div>
      </main>

      {/* 嵌入QAnything聊天机器人脚本 */}
      <script
        src="https://ai.youdao.com/saas/qanything/js/agent-iframe-min.js"
        id="qanything-iframe"
        data-agent-src="https://ai.youdao.com/saas/qanything/#/bots/89B2BD821E714E83/share"
        data-default-open="false"
        data-drag="false"
        data-open-icon="https://download.ydstatic.com/ead/icon-qanything-iframe-btn.png"
        data-close-icon="https://download.ydstatic.com/ead/icon-qanything-iframe-btn.png"
        defer
      />
    </div>
  );
}
