<template>
  <div class="dashboard-editor-container">
    <search />
    <!-- <cards /> -->
    <el-row :gutter="20">
      <el-col :span="1"><div class="grid-content ep-bg-purple" /></el-col>
      <el-col :span="7">
        <tcards name="pytorch" stars="60.2k" forks="16.8k" />
      </el-col>
      <!-- <el-col :span="10">
        <tcards />
      </el-col> -->
    </el-row>
    <!-- <linechart /> -->
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>

    <!-- 图表 -->
  </div>
</template>
<script>
import search from './components/search'
import tcards from './components/repocard.vue' // github repo展示卡片
import linechart from './components/linechart.vue' // 绘图

export default {
  name: 'Dashboard',
  components: {
    search,
    tcards,
    linechart,
    // piechart
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }
  .grid-content {
  border-radius: 4px;
  min-height: 36px;
}
  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width: 1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
