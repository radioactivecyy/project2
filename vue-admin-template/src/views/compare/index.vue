<template>
  <div class="dashboard-editor-container">
    <h1>Pytorch VS Pandas</h1>
    <h2>社区发展速度</h2>
    <h2>贡献者活跃情况</h2>
    <h2>代码提交情况</h2>
    <h2>Companies</h2>
    <el-row :gutter="32"
      ><el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <develop/>
          </div>
        </div>
      </el-col>
    </el-row>
 <el-row :gutter="32"
      ><el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <bubble_starVue />
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
   
          <bubble_issue />
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4"></div>
          <bubble_commit />
        </div>
      </el-col>
    </el-row> 
  </div>
</template>
<script>
import bubble_starVue from './components/bubble_star.vue'
import bubble_commit from './components/bubble_commit.vue'
import bubble_issue from './components/bubble_issue.vue'
import legend_s from './components/legend_s.vue'
import develop from './components/develop.vue'
export default {
  name: 'UserProfile',
  components: {
    bubble_starVue,
    bubble_commit,
    bubble_issue,
    legend_s,
    develop
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
