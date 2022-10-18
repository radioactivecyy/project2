<template>
  <div class="dashboard-editor-container">
    <h1>{{ this.$route.query.name }}</h1>
    <!-- 图表信息 -->
    <el-row :gutter="32">
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <linechart />
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <piechart />
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import linechart from './components/linechart'
import piechart from './components/piechart'
export default {
  name: 'RepoDetail',
  components: {
    linechart,
    piechart
  },
  mounted() {
    const msg = this.$route.query.name
    console.log(msg)
  }
  // 接收路由router参数
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
