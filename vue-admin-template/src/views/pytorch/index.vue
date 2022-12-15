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
      <el-row>
        <el-col :xs="10" :sm="10" :lg="12">
          <div class="chart-wrapper">
            <div>
              <linechart
                Mytitle="issue"
                color1="rgb(50, 144, 212 )"
                color2="rgb(50, 144, 212 )"
                color3="rgb(50, 144, 212 )"
                :chartData="issueNumdata"
              />
            </div>
          </div>
        </el-col>
        <el-col :xs="14" :sm="14" :lg="12">
          <div class="chart-wrapper">
            <div class="flex justify-space-between mb-4 flex-wrap gap-4">
              <linechart
                Mytitle="committer"
                color1="rgb(252, 93, 78 )"
                color2="rgb(244, 118, 105 )"
                color3="rgb(241, 79, 63 )"
                :chartData="commitNumdata"
              />
            </div>
          </div>
        </el-col>
      </el-row>

      <el-row>
        <el-col :xs="14" :sm="14" :lg="12">
          <div class="chart-wrapper">
            <div class="flex justify-space-between mb-4 flex-wrap gap-4">
              <linechart
                Mytitle="star"
                color1="rgb(149, 229, 130 )"
                color2="rgb(159, 233, 141  )"
                color3="rgb(50, 144, 212 )"
                :chartData="starNumdata"
              />
            </div>
          </div>
        </el-col>
        <el-col :xs="14" :sm="14" :lg="12">
          <div class="chart-wrapper">
            <div class="flex justify-space-between mb-4 flex-wrap gap-4">
              <linechart3
                myTitle="社区发展速度"
                color1_3="rgb(149, 229, 130 )"
                color2_3="rgb(159, 233, 141  )"
                color3_3="rgb(50, 144, 212 )"
                color1_2="rgb(252, 93, 78 )"
                color2_2="rgb(244, 118, 105 )"
                color3_2="rgb(241, 79, 63 )"
                color1_1="rgb(50, 144, 212 )"
                color2_1="rgb(50, 144, 212 )"
                color3_1="rgb(50, 144, 212 )"
                :chartData1="issueNumdata"
                :chartData2="starNumdata"
                :chartData3="commitNumdata"
              />
            </div>
          </div>
        </el-col>
      </el-row>
    </el-row>
    <h2>贡献者活跃情况</h2>
    <el-row>
      <el-col :span="20">
        <calender :Year="year" MyTitle="star" />
      </el-col>
      <!-- <el-col :span="12">
        <calender :Year="year" MyTitle="issue" />
      </el-col> -->
    </el-row>
    <el-row>
      <!-- <el-col :xs="14" :sm="14" :lg="12">
        <calender :Year="year" MyTitle="commit" />
      </el-col> -->
      <el-col :xs="14" :sm="14" :lg="23">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <ins_del :chartData="insDelData" lineTitle1="add" lineTitle2="delete" @func="getMsgFrominsDel" />
          </div>
        </div>
      </el-col>
    </el-row>

    <h2>代码提交情况</h2>
    <el-row :gutter="32">
      <el-col :xs="14" :sm="24" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <code_num :chartData="contriData" @func="getMsgFromcode" />
          </div>
        </div>
      </el-col>
      <el-image style="width: 600px; height: 600px" :src="contirbcloud" :fit="fit" />
    </el-row>

    <h2>Companies</h2>

    <el-row :gutter="32">
      <el-col :xs="14" :sm="14" :lg="15">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4"></div>

          <el-button class="company-button" type="primary" @click="starBubble">star</el-button>
          <el-button class="company-button" type="primary" @click="issueBubble"> issue </el-button>
          <el-button class="company-button" type="primary" @click="commitBubble"> commit </el-button>

          <sBubble :dataAsJson="bubble_data" :testData="ttt" dataType="companyDataType" />
        </div>
      </el-col>
      <el-col :xs="14" :sm="14" :lg="8">
        <List :DataSource="ListData" />
      </el-col>
    </el-row>

    <h2>设计讨论</h2>
    <el-row :gutter="32">
      <el-col :span="22">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <linechart
              Mytitle="design"
              color1="rgb(50, 144, 212 )"
              color2="rgb(50, 144, 212 )"
              color3="rgb(50, 144, 212 )"
              :chartData="designData"
            />
          </div>
        </div>
      </el-col>
    </el-row>
    <h2>cloud</h2>
    
    <el-image style="width: 600px; height: 600px" :src="designcloud" :fit="fit" />
  </div>
</template>

<script>
import sBubble from './components/company_star.vue'

import List from './components/list.vue'
import linechart from './components/linechart.vue'
import code_num from './components/code_num.vue'

import linechart3 from './components/linechart3.vue'

import ins_del from './components/ins_del.vue'
import calender from './components/calender.vue'

import * as dataapi from '@/api/getdata'
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
      Issue_bubble_data: Array,
      Commit_bubble_data: Array,
      bubble_data: Array,
      ttt: 0,
      issueNumdata: {},
      starNumdata: {},
      commitNumdata: {},
      threeData: {},
      insDelData: {},
      startVal: -1,
      endVal: -1,
      contriData: {},
      designData: {},
      designcloud: String,
      contirbcloud: String,

      companyDataType: 'star',
      ListData: 'dev-api/api/pytorch_star'
    }
  },
  components: {
    // iBubble,
    sBubble,
    // cBubble,
    List,
    linechart,
    code_num,

    ins_del,
    calender,
    // contributor_cloudVue,

    linechart3
  },
  watch: {
    year: function (val) {
      // 重新渲染calender
      this.$forceUpdate()
      // console.log(val)
    },

  },

  mounted() {
    const msg = this.$route.query.name
    this.getCompanyStarData()
    this.getCompanyIssueData()
    this.getCompanyCommitData()
    this.getDesignCloud()
    this.getContribCloud()
    this.getIssueLineData()
    this.getStarLineData()
    this.getCommitLineData()
    // this.getThreeData()
    this.getInsDelData()
    this.getContribution()
    this.getDesignData()
  },
  methods: {
    starBubble: function (data) {
      // console.log('starBubble')
      this.getCompanyStarData().then(res => {
        //  刷新该组件
        console.log('starBubble')
        this.companyDataType = 'star'
      })
    },
    issueBubble: function (data) {
      // console.log('issueBubble')
      this.getCompanyIssueData().then(res => {
        //  刷新该组件
        this.companyDataType = 'issue'
    })},
    commitBubble: function (data) {
      this.getCompanyCommitData().then(res => {
        //  刷新该组件
        this.companyDataType = 'commit'
      })
    },
    async getDesignCloud() {
     
      dataapi.getDesignCloud().then(res => {
        this.designcloud = 'data:image/png;base64,' + res.base64_png
     
      })
    },
    async getContribCloud() {
     console.log('getContribCloud')
     dataapi.getContributionCloud().then(res => {
       this.contirbcloud = 'data:image/png;base64,' + res.base64_png
       
     })
   },
    async getCompanyStarData() {
      const res = await d3.csv('dev-api/api/pytorch_star')
      this.bubble_data = res
      this.ListData = JSON.parse(JSON.stringify(res))
    },
    async getCompanyIssueData() {
      const res = await d3.csv('dev-api/api/pytorch_issue')
      this.bubble_data = res
      this.ListData = JSON.parse(JSON.stringify(res))
    },
    async getCompanyCommitData() {
      const res = await d3.csv('dev-api/api/pytorch_committer')
      this.bubble_data = res
      this.ListData = JSON.parse(JSON.stringify(res))
    },
    async getIssueLineData() {
      await dataapi.getIssueDevelop().then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['y'] = res.y
        this.issueNumdata = JSON.parse(JSON.stringify(data))
        this.threeData['x'] = this.issueNumdata.x
        this.threeData['y1'] = this.issueNumdata.y
      })
    },
    async getStarLineData() {
      await dataapi.getStarDevelop().then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['y'] = res.y
        this.starNumdata = JSON.parse(JSON.stringify(data))
        this.threeData['y2'] = this.starNumdata.y
      })
    },
    async getCommitLineData() {
      await dataapi.getCommitDevelop().then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['y'] = res.y
        this.commitNumdata = JSON.parse(JSON.stringify(data))
        this.threeData['y3'] = this.commitNumdata.y
      })
    },
    async getInsDelData() {
      await dataapi.getInsDel(this.startVal, this.endVal).then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['y1'] = res.y1
        data['y2'] = res.y2
        this.insDelData = JSON.parse(JSON.stringify(data))
      })
    },
    async getContribution() {
      await dataapi.getContribution().then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['y1'] = res.y1
        data['y2'] = res.y2
        this.contriData = JSON.parse(JSON.stringify(data))
      })
    },
    async getDesign() {
      await dataapi.getDesign().then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['y'] = res.y

        this.designData = JSON.parse(JSON.stringify(data))
      })
    },
    // async getThreeData() {

    //   console.log('there')
    //   console.log(this.threeData)
    // },
    getMsgFromcode(msg) {
      // 把msg传递给父组件中的TimeOfContributor
      this.TimeOfContributor = msg
    },
    getMsgFrominsDel(msg) {
      var d = JSON.parse(JSON.stringify(msg))
      console.log('ddddddddddddddddd', d)
      this.startVal = d.startVal
      this.endVal = d.endVal
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
.company-button {
  background-color: #fff; /* Green */
  border: none;
  color: rgb(75, 140, 220);
  padding: 15px 72px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 15px;

  // 设置字和底部的距离
}
</style>
