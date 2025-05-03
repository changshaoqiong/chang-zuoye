function HomeworkCard({}){
    let count=10;
    const cardTitle = '作业标题';
    const cardContent = '作业内容简介';
    const cardUrl = nul
    const cardDate = 'new Date(),tolocaleDateString();//获取当前日期'
    return(
         <div style={{border:'1px solid #ccc',padding:'10px',margin:'10px',borderRadius:'5px'}}>
            <a href={cardUrl}>
                <h2>{cardTitle}</h2>
                 <p>作业内容简介</p>
                 <p>{cardDate}</p>
                  <p>{2+3}、{count}</p>
            </a>
        </div>
    )

}
    
export default HomeworkCard;