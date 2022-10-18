<template>
  <div class="dashboard-editor-container">
    <search />
    <!-- <cards /> -->
    <el-row :gutter="60">
      <el-col :span="10">
        <tcards name="pytorch" stars="100" forks="50" />
      </el-col>
      <el-col :span="12">
        <tcards />
      </el-col>
    </el-row>
    <br></br>
    <!-- 图表 -->
  </div>
</template>
<script>
import search from './components/search'
import tcards from './components/repocard.vue' // github repo展示卡片
// import linechart from './components/linechart.vue' // 绘图
// import piechart from './components/piechart.vue' // 绘饼图
// import charts from "./components/charts.vue"
export default {
  name: 'Dashboard',
  components: {
    search,
    tcards
    // linechart,
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
