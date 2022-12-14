<template>
  <div class="dashboard-editor-container">
    <h1>Pytorch VS Pandas</h1>
    <a>数据获取时间为:若需要获取最新数据请点击:<el-button @click="refresh()">刷新</el-button></a>

    <h2>社区发展速度</h2>
    <el-row>
      <el-row>
        <el-col :xs="10" :sm="10" :lg="12">
          <div class="chart-wrapper">
            <div>
              <linechart2
                Mytitle="issue"
                color1="rgb(50, 144, 212 )"
                color2="rgb(50, 144, 212 )"
                lineTitle1="Pytorch"
                lineTitle2="Pandas"
                :chartData="issueNumdata"
              />
            </div>
          </div>
        </el-col>
        <el-col :xs="14" :sm="14" :lg="12">
          <div class="chart-wrapper">
            <div class="flex justify-space-between mb-4 flex-wrap gap-4">
              <linechart2
                Mytitle="committer"
                color1="rgb(252, 93, 78 )"
                color2="rgb(244, 118, 105 )"
                lineTitle1="Pytorch"
                lineTitle2="Pandas"
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
              <linechart2
                Mytitle="star"
                color1="rgb(149, 229, 130 )"
                color2="rgb(159, 233, 141  )"
                lineTitle1="Pytorch"
                lineTitle2="Pandas"
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
              />
            </div>
          </div>
        </el-col>
      </el-row>
    </el-row>
    <h2>贡献者活跃情况</h2>
    <el-row>
      <el-col span="12">
        <calender :Year="year" MyTitle="star" />
      </el-col>
      <el-col span="12">
        <calender :Year="year" MyTitle="star" />
      </el-col>
    </el-row>
    <el-row>
      <el-col span="12">
        <calender :Year="year" MyTitle="issue" />
      </el-col>
      <el-col span="12">
        <calender :Year="year" MyTitle="issue" />
      </el-col>
    </el-row>

    <el-row>
      <el-col span="12">
        <calender :Year="year" MyTitle="commit" />
      </el-col>
      <el-col span="12">
        <calender :Year="year" MyTitle="commit" />
      </el-col>
    </el-row>

    <co_ins_delVue :chartData="insDelData" @func="getMsgFrominsDel" />
    <h2>代码提交情况</h2>
    <co_code_numVue :chartData="codeNumData" @func="getMsgFromcode" />
    <el-image style="width: 100px; height: 100px" :src="contributorCloud_p" :fit="fit" />
    <el-image style="width: 100px; height: 100px" :src="contributorCloud_o" :fit="fit" />
    <h2>Companies</h2>

    <el-row :gutter="10">
      <el-col :xs="14" :sm="14" :lg="19" :offset="1">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <el-button class="company-button" type="primary" @click="starBubble">star</el-button>
            <el-button class="company-button" type="primary" @click="issueBubble"> issue </el-button>
            <el-button class="company-button" type="primary" @click="commitBubble"> commit </el-button>
            <bubble_starVue :dataAsJson="bubbleData" />
          </div>
        </div>
      </el-col>
    </el-row>
    <h2>design</h2>
    <linechart2> </linechart2>
    <el-image style="width: 100px; height: 100px" :src="designcloud1" :fit="fit" />
    <el-image style="width: 100px; height: 100px" :src="designcloud2" :fit="fit" />
  </div>
</template>
<script>
import bubble_starVue from './components/bubble_star.vue'
import linechart2 from './components/linechart2.vue'
import calender from '../pytorch/components/calender.vue'
import co_ins_delVue from './components/co_ins_del.vue'
import co_code_numVue from './components/co_code_num.vue'
import { refreshOther } from '@/api/getdata'
import { refreshData } from '@/api/pytorch'
import List from '../pytorch/components/list.vue'
import * as dataapi from '@/api/getdata'
import * as d3 from 'd3'
export default {
  name: 'UserProfile',
  components: {
    bubble_starVue,
    calender,
    linechart2,
    co_ins_delVue,
    co_code_numVue
  },
  data() {
    return {
      issueNumdata: {},
      starNumdata: {},
      commitNumdata: {},
      threeData: {},
      insDelData: {},
      startVal: -1,
      endVal: -1,
      contriData: {},
      designcloud1: String,
      designcloud2: String,
      ListData1: Object,
      ListData2: Object,
      bubbleData: Array,
      contributorCloud_p: String,
      contributorCloud_o: String,
      TimeOfContributor: 0
    }
  },

  mounted() {
    const msg = this.$route.query.name
    this.getCompanyStarData()
    this.getDesignCloud()
    this.getIssueLineData()
    this.getStarLineData()
    this.getCommitLineData()
    this.getInsDelData()
    this.getContribution()
  },
  methods: {
    async getcontribCloud_p() {
      dataapi.getContribCloudP(this.TimeOfContributor).then(res => {
        this.contributorCloud_p = 'data:image/png;base64,' + res.data
      })
    },
    async getcontribCloud_o() {
      dataapi.getContribCloudO(this.TimeOfContributor).then(res => {
        this.contributorCloud_o = 'data:image/png;base64,' + res.data
      })
    },
    starBubble: function (data) {
      // console.log('starBubble')
      this.getCompanyStarData().then(res => {
        //  刷新该组件
        this.companyDataType = 'star'
      })
    },
    issueBubble: function (data) {
      // console.log('issueBubble')
      this.getCompanyIssueData().then(res => {
        //  刷新该组件
        this.companyDataType = 'issue'
      })
    },
    commitBubble: function (data) {
      // console.log('commitBubble')
      this.getCompanyCommitData().then(res => {
        //  刷新该组件
        this.companyDataType = 'commit'
      })
    },
    async getCompanyStarData() {
      const res = await d3.csv('dev-api/api/star_gazer')
      this.bubbleData = res
      var data = JSON.parse(JSON.stringify(res))
      // 遍历数组，如果元素的data.flag为0,加到ListData1中，否则加到ListData2中
      this.ListData1 = data.filter(item => item.flag === '0')
      this.ListData2 = data.filter(item => item.flag === '1')
    },
    async getCompanyIssueData() {
      const res = await d3.csv('dev-api/api/issue')
      this.bubbleData = res
      var data = JSON.parse(JSON.stringify(res))
      // 遍历数组，如果元素的data.flag为0,加到ListData1中，否则加到ListData2中
      this.ListData1 = data.filter(item => item.flag === '0')
      this.ListData2 = data.filter(item => item.flag === '1')
    },
    async getCompanyCommitData() {
      const res = await d3.csv('dev-api/api/committer')
      this.bubbleData = res
      var data = JSON.parse(JSON.stringify(res))
      // 遍历数组，如果元素的data.flag为0,加到ListData1中，否则加到ListData2中
      this.ListData1 = data.filter(item => item.flag === '0')
      this.ListData2 = data.filter(item => item.flag === '1')
    },
    async getDesignCloud() {
      await dataapi.OgetDesignCloud().then(res => {
        this.designcloud1 = 'data:image/png;base64,' + res.cloud1
        this.designcloud2 = 'data:image/png;base64,' + res.cloud2
      })
    },

    async getIssueLineData() {
      await dataapi.OgetIssueDevelop().then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['pytorch'] = res.pytorch
        data['pandas'] = res.pandas
        this.issueNumdata = JSON.parse(JSON.stringify(data))
        this.threeData['x'] = this.issueNumdata.x
        this.threeData['pytorch_y1'] = this.issueNumdata.pytorch
        this.threeData['pandas_y1'] = this.issueNumdata.pandas
      })
    },
    async getStarLineData() {
      await dataapi.OgetStarDevelop().then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['pytorch'] = res.pytorch
        data['pandas'] = res.pandas
        this.starNumdata = JSON.parse(JSON.stringify(data))
        this.threeData['pytorch_y2'] = this.starNumdata.pytorch
        this.threeData['pandas_y2'] = this.starNumdata.pandas
      })
    },
    async getCommitLineData() {
      await dataapi.OgetCommitDevelop().then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['pytorch'] = res.pytorch
        data['pandas'] = res.pandas
        this.commitNumdata = JSON.parse(JSON.stringify(data))
        this.threeData['pytorch_y3'] = this.commitNumdata.pytorch
        this.threeData['pandas_y3'] = this.commitNumdata.pandas
      })
    },
    async getInsDelData() {
      await dataapi.OgetInsDel(this.startVal, this.endVal).then(res => {
        // 把数组中的每个元素都push到data中

        // data['y2'] = res.y2
        var data = { chartData1: {}, chartData2: {} }
        data['chartData1']['x'] = res.x
        data['chartData1']['y1'] = res.pytorch_add
        data['chartData1']['y2'] = res.pytorch_del
        data['chartData2']['x'] = res.x
        data['chartData2']['y1'] = res.pandas_add
        data['chartData2']['y2'] = res.pandas_del
        this.insDelData = JSON.parse(JSON.stringify(data))
      })
    },
    async getContribution() {
      await dataapi.OgetContribution().then(res => {
        // 把数组中的每个元素都push到data中
        var data = { chartData1: {}, chartData2: {} }
        data['chartData1']['x'] = res.x
        data['chartData2']['x'] = res.x
        data['chartData1']['y1'] = res.pytorch_core
        data['chartData1']['y2'] = res.pytorch_else
        data['chartData2']['y1'] = res.pandas_core
        data['chartData1']['y2'] = res.pandas_else
        // data['y2'] = res.y2
        this.contriData = JSON.parse(JSON.stringify(data))
        // console.log('this.contriData', this.contriData)
      })
    },
    async refresh() {
      refreshData().then(
        // 刷新数据后重新渲染
        // 消息提示
        this.$message({
          message: '刷新成功',
          type: 'success'
        }),
        this.getCompanyStarData(),

        this.getDesignCloud(),
        this.getIssueLineData(),
        this.getStarLineData(),
        this.getCommitLineData(),
        // this.getThreeData()
        this.getInsDelData(),
        this.getContribution()
      )
      refreshOther().then(
        this.$message({
          message: '刷新成功',
          type: 'success'
        }),
        this.getCompanyStarData(),

        this.getDesignCloud(),
        this.getIssueLineData(),
        this.getStarLineData(),
        this.getCommitLineData(),
        // this.getThreeData()
        this.getInsDelData(),
        this.getContribution()
      )
    },
    getMsgFromcode(msg) {
      // 把msg传递给父组件中的TimeOfContributor
   
      this.TimeOfContributor = msg
     
    },
    getMsgFrominsDel(msg) {
      var d = JSON.parse(JSON.stringify(msg))

      this.startVal = d.startVal
      this.endVal = d.endVal
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
    padding: 0px 10px 0;
    margin-bottom: 0px;
  }
  // .el-row {
  //   margin-bottom: 20px;
  //   display: flex;

  // }
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
