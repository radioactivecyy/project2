<template>
  <div class="dashboard-editor-container">
    <h1>Companies</h1>
    <p>company information about Stargazers, Issue creators, and Pull Request</p>
    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
        </div>
        <h2>Stargazers</h2>
          <sBubble  />
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="8">
        <List  DataSource='dev-api/api/star_gazer'/>
      </el-col>
    </el-row>
    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">

        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
        </div>
          <iBubble />
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="8">
        <List DataSource='dev-api/api/issue' />
      </el-col>
    </el-row>

    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">

        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
  </div>
          <cBubble/>
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="8">
        <List  DataSource='dev-api/api/committer' />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import iBubble from './components/company_issue.vue'
import sBubble from './components/company_star.vue'
import cBubble from './components/company_committer.vue'
import List from './components/list.vue'
export default {
  name: 'Pytorch',
  data() {
    return {
    }
  },
  components: {
    iBubble,
    sBubble,
    cBubble,
    List
  },
  mounted() {
    const msg = this.$route.query.name
    console.log(msg)
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
