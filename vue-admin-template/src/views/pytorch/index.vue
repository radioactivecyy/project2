<template>
  
  <div class="dashboard-editor-container">
  <h1>Companies
  </h1>
  <p>company information about Stargazers, Issue creators, and Pull Request</p>
    <el-row :gutter="32">
      <el-col :xs="44" :sm="44" :lg="88">
        <div class="chart-wrapper">
          <Bubble />
        </div>
      </el-col>
      </el-row>
  </div>
</template>

<script>
import Bubble from './components/company.vue'
export default {
  name: 'Pytorch',
  components: {
    Bubble
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