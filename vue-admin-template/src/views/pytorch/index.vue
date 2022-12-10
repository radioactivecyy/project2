<template>
  <div class="dashboard-editor-container" id="pdfDom">
    <h1><svg-icon icon-class="pytorch" /> Pytorch</h1>
    <a>数据获取时间为:若需要获取最新数据请点击:<el-button @click="refresh()">刷新</el-button></a>
    <p>
      company information about Stargazers, Issue creators, and Pull Request. Click here to download report
      <el-button class="bt-style" @click="getPdf(htmlTitle)"></el-button>
    </p>
    <h2>社区发展速度</h2>
    <el-row>
    <el-row >
      <el-col :xs="10" :sm="10" :lg="12">
        <div class="chart-wrapper">
          <div>
            <linechart Mytitle="issue" color1="rgb(50, 144, 212 )" color2="rgb(50, 144, 212 )" color3="rgb(50, 144, 212 )"/>
          </div>
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="12">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <linechart Mytitle="committer" color1="rgb(252, 93, 78 )" color2="rgb(244, 118, 105 )" color3="rgb(241, 79, 63 )"/>
          </div>
        </div>
      </el-col>
    </el-row>
   
    <el-row >
      <el-col :xs="14" :sm="14" :lg="12">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <linechart Mytitle="star" color1="rgb(149, 229, 130 )" color2="rgb(159, 233, 141  )" color3="rgb(50, 144, 212 )"/>
          </div>
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="12">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <linechart Mytitle="社区发展速度" color1="rgb(149, 229, 130 )" color2="rgb(159, 233, 141  )" color3="rgb(50, 144, 212 )"/>
          </div>
        </div>
      </el-col>
    </el-row>
  </el-row>
    <h2>贡献者活跃情况</h2>
    <el-row >
      <el-col :span="12">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <calender :Year="year" />
          </div>
        </div>
      </el-col>
      <el-col :span="12">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <calender :Year="year" />
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row >
      <el-col :xs="14" :sm="14" :lg="12">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <calender :Year="year" />
          </div>
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="12">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <ins_del />
          </div>
        </div>
      </el-col>
    </el-row>
   
      <h2>代码提交情况</h2>
      <el-row :gutter="32">
      <el-col :xs="14" :sm="24" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <code_num @func="getMsgFromcode" />
          </div>
        </div>
      </el-col>
   
    <h2>Companies</h2>
   

    <!-- 按钮 -->
  </el-row>
        <el-col :span="4">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="4">
          <div class="grid-content ep-bg-purple-light" />
        </el-col>
        <el-col :span="5">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="2">
          <div class="grid-content ep-bg-purple-light" />
          <el-select v-model="year" class="m-2" placeholder="Select" size="small" @change="$forceUpdate()">
            <el-option v-for="item in this.yearoption" :key="item.value" :label="item.label" :value="item.value" />
          </el-select>
        </el-col>
        <el-col :span="4">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="4">
          <div class="grid-content ep-bg-purple-light" />
        </el-col>
      </el-row>
    </el-row>
   
   

   
    <el-row :gutter="32">
      <el-col :xs="14" :sm="24" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <contributor_cloudVue :msg="TimeOfContributor" />
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
          <sBubble :dataAsJson="Star_bubble_data" :testData="ttt" />
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
    <h2>设计讨论</h2>
    <el-row :gutter="32">
      <el-col :span="22">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <designVue />
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
import code_num from './components/code_num.vue'
import designVue from './components/design.vue'

import ins_del from './components/ins_del.vue'
import calender from './components/calender.vue'
import contributor_cloudVue from './components/contributor_cloud.vue'
import { refreshData } from '@/api/pytorch'
import * as d3 from 'd3'
export default {
  name: 'Pytorch',
  
  data() {
    return {
      htmlTitle: 'Pytorch',
      yearoption: [],
      year: '2019',
      TimeOfContributor: null,
      Star_bubble_data: Array,
      ttt:0
    }
  },
  components: {
    iBubble,
    sBubble,
    cBubble,
    List,
    linechart,
    code_num,
    designVue,
    ins_del,
    calender,
    contributor_cloudVue
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
    this.getCompanyStarData()
    this.yearoption = [
      {
        value: '2015',
        label: '2015'
      },
      {
        value: '2016',
        label: '2016'
      },
      {
        value: '2017',
        label: '2017'
      },
      {
        value: '2018',
        label: '2018'
      },
      {
        value: '2019',
        label: '2019'
      }
    ]
  },
  methods: {
    async getCompanyStarData() {
      console.log('getCompanyStarData')
      const res = await d3.csv('dev-api/api/pytorch_star')
      this.Star_bubble_data = res
      this.ttt=this.ttt+1
      
      return res
    },

    getMsgFromcode(msg) {
      // 把msg传递给父组件中的TimeOfContributor
      this.TimeOfContributor = msg
    },
    async refresh() {
      refreshData().then(
        // 刷新数据后重新渲染
        // 消息提示
        this.$message({
          message: '刷新成功',
          type: 'success'
        }),
        this.getCompanyStarData()

      )
      
    }
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

.svg-icon {
  width: 1.2em;
  height: 1.2em;
  vertical-align: -0.15em;
  // 229, 74, 37
  fill: rgb(229, 74, 37);
  overflow: hidden;
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
