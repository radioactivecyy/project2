<template>
  <div class="dashboard-editor-container" id="pdfDom">
    <h1>Companies</h1>
    <p>
      company information about Stargazers, Issue creators, and Pull Request. Click here to download report
      <el-button class="bt-style" @click="getPdf(htmlTitle)"></el-button>
    </p>
  
    <!-- 按钮 -->
    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <ins_del  />
          </div>
        </div>
      </el-col>
      <el-row>
    <el-col :span="4"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple-light" /></el-col>
    <el-col :span="5"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="2"><div class="grid-content ep-bg-purple-light" />
      <el-select v-model="year" class="m-2" placeholder="Select" size="small" @change="$forceUpdate()">
    <el-option 
    
      v-for="item in this.yearoption"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    />
  </el-select></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple" />
    </el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple-light" />
   </el-col>
  </el-row>
   
    </el-row>
    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
         <calender :Year="year" />
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <linechart  />
          </div>
        </div>
      </el-col>
    </el-row>



    <el-row :gutter="32">
      <el-col :xs="14" :sm="24" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <piechart  />
          </div>
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <h2>Stargazers</h2>
          </div>

          <sBubble />
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="8">
        <List DataSource="dev-api/api/pytorch_star" />
      </el-col>
    </el-row>
    
    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4"></div>
          <iBubble />
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="8">
        <List DataSource="dev-api/api/pytorch_issue" />
      </el-col>
    </el-row>

    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4"></div>
          <cBubble />
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="8">
        <List DataSource="dev-api/api/pytorch_committer" />
      </el-col>
    </el-row>
    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <designVue  />
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import iBubble from './components/company_issue.vue'
import sBubble from './components/company_star.vue'
import cBubble from './components/company_committer.vue'
import List from './components/list.vue'
import linechart from './components/linechart.vue'
import piechart from './components/code_num.vue'
import designVue  from './components/design.vue'
import ins_del from './components/ins_del.vue'
import calender from './components/calender.vue'

export default {
  name: 'Pytorch',
  data() {
    return {
      htmlTitle: 'Pytorch',
      yearoption:[],
      year:'2019',
    }
  },
  components: {
    iBubble,
    sBubble,
    cBubble,
    List,
    linechart,
    piechart,
    designVue,
    ins_del,
    calender,

    
  },
  watch: {
    year: function (val) {
      // 重新渲染calender
      this.$forceUpdate()
      // console.log(val)
    }
  },

  mounted() {
    const msg = this.$route.query.name
    console.log(msg)
    this.yearoption = [{
    value: '2015',
    label: '2015',
  },
  {
    value: '2016',
    label: '2016',
  },
  {
    value: '2017',
    label: '2017',
  },
  {
    value: '2018',
    label: '2018',
  },
  {
    value: '2019',
    label: '2019',
  },
]
  
  },
  methods: {
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
.bt-style {
  background-repeat: no-repeat;
  background-image: url('./images/download.png');
  width: 6em;
  height: 3em;
  background-color: transparent;
  border-style: none;
}
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>
