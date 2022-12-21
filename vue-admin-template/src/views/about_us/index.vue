<template>
    <div class="dashboard-editor-container" >
    
    <div class="text-center">
    <h1>项目简介</h1>
    <p> 这是Pytorch 项目分析平台, 一个旨在帮助开发者和代码分析者对Pytorch项⽬进⾏分析、⽐较, 以更好地从更多维度了解Pytorch项目的各个方面的平台</p>
    </div>

    <div class="text-center">
    <h1>Developers</h1>
    </div>
    <div class="text-center">
    <el-row>
    <el-col :span="11" :offset="1"> <el-card class="box-card">
  <div slot="header" class="clearfix">
    <span> <div>
      <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
    </div></el-item>陈奕宇</span>
     </div>
<p>组长，后端开发</p>
</el-card>
    </el-col>
    <el-col :span="10">      
<el-card class="box-card">
  <div slot="header" class="clearfix">
    <span> <div>
      <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
    </div></el-item>黄亦霄</span>
     </div>
<p>后端开发</p>
</el-card></el-col>    
    </el-row>
 </div>
 <div class="text-center">
    <el-row>
    <el-col :span="11" :offset="1">
<el-card class="box-card">
  <div slot="header" class="clearfix">
    <span> <div>
      <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
    </div></el-item>江小小</span>
     </div>
<p>前端开发</p>
</el-card>
</el-col>
</el-row>
</div>

    <div class="text-center">
    <h1>Our repo</h1>
    <el-link href="https://github.com/radioactivecyy/project2" target="_blank">这是我们的github仓库    </el-link><svg-icon  icon-class="link" /><a>, 这里有我们的代码和项目使用安装说明</a>
    
    </div>
    </div>
</template>
<script>

</script>


<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;
    .text-center{
        text-align: center;
        // 行间距
        line-height: 2;
    }
  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }
  .el-row {
  margin-bottom: 30px;
}
  .box-card {
    width: 460px;
  }
  .chart-wrapper {
    background: #fff;
    padding: 0px 10px 1;
    margin-bottom: 20px;
  }
 
  .grid-content {
    border-radius: 2px;
    min-height: 20px;
  }
  .company-button {
    background-color: #fff; /* Green */
    border: none;
    color: rgb(75, 140, 220);
    padding: 15px 92px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 15px;

    // 设置字和底部的距离
  }


}

@media (max-width: 1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
