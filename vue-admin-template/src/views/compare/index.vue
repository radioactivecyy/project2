<template>
  <div class="dashboard-editor-container" id="pdfDom">
    <h1><svg-icon icon-class="pytorch" />Pytorch VS Pandas</h1>
    <a>若需要获取最新数据请点击:<el-button @click="refresh()">刷新</el-button></a>
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
  </el-row>
    <h2>贡献者活跃情况</h2>
 

    <co_ins_delVue :chartData1="insDelData1" :chartData2="insDelData2" @func="getMsgFrominsDel"  />
    <h2>代码提交情况</h2>
    <el-row :gutter="22">
    <el-col :xs="14" :sm="24" :lg="15">
      <div class="chart-wrapper">
    <co_code_numVue :chartData="codeNumData" @func="getMsgFromcode" mytitle="commit" mytitle2="pandas commit" /></div>
  </el-col>
    <el-col :span="5">
    <el-image style="width: 400px; height: 400px" :src="contributorCloud_p" :fit="fit" />
    <el-image style="width: 400px; height: 400px" :src="contributorCloud_o" :fit="fit" /></el-col></el-row>
   
    <el-row>
    <el-col :span="22">
    <div class="chart-wrapper">
      <contrib_graphVue :chartData="contrigraphData"  Mytitle="pytorch贡献者代码提交量" />
    </div>
    </el-col>
    </el-row>
    <br></br>
    <el-row>
    <el-col :span="22">
    <div class="chart-wrapper">
      <contrib_graphVue :chartData="contrigraphData2"  Mytitle="pandas贡献者代码提交量"/>
    </div>
    </el-col>
    </el-row>
    <br></br>
    <el-row :gutter="22">
    <el-col :xs="14" :sm="24" :lg="22">
      <div class="chart-wrapper">
    <co_code_num_designVue :chartData="contriDesign" mytitle="design" mytitle2="pandas design"/></div>
  </el-col>
   
   
  </el-row>
  
   
    
    <el-row :gutter="22">
    <el-col :xs="14" :sm="24" :lg="22">
      <div class="chart-wrapper">
    <co_code_num_fileVue :chartData="contriFile" mytitle="file" mytitle2="pandas file"/></div>
  </el-col>
</el-row>
  
  <h2>Issue</h2>
  <el-row :gutter="22">
  <el-col :xs="14" :sm="24" :lg="15">
  <div class="chart-wrapper">
    <Co_Issue :chartData1="IssueUpdateP" :chartData2="IssueUpdateO" Mytitle1="pytorch" Mytitle2="pandas"/></div>
    </el-col>
    
    <el-col :span="5">
    <el-image style="width: 300px; height: 300px" :src="IssueCloudP" :fit="fit" />
    <br></br>
    <el-image style="width: 300px; height: 300px" :src="IssueCloudO" :fit="fit" />
    </el-col>
    </el-row>
    <h2>Companies</h2>

    <el-row :gutter="10">
      <el-col :xs="14" :sm="14" :lg="19" :offset="1">
        <div class="chart-wrapper">
          <div class="flex justify-space-between mb-4 flex-wrap gap-4">
            <el-button id="star" class="company-button" type="primary" @click="starBubble">star</el-button>
            <el-button id="issue" class="company-button" type="primary" @click="issueBubble"> issue </el-button>
            <el-button id="commit" class="company-button" type="primary" @click="commitBubble"> commit </el-button>
            <bubble_starVue :dataAsJson="bubbleData" />
          </div>
        </div>
      </el-col>
    </el-row>
    <h2>design</h2>
    <div class="chart-wrapper">
    <linechart2
    Mytitle="design"
                color1="rgb(149, 229, 130 )"
                color2="rgb(159, 233, 141  )"
                lineTitle1="Pytorch"
                lineTitle2="Pandas"
                :chartData="designNumdata"
    /> 
    </div>
    <el-row :gutter="30">
    <el-col :span="10" :offset="1">
    <el-image style="width: 450px; height: 450px" :src="designcloud1" :fit="fit" /></el-col>
    <el-col :span="10"></el-col><el-image style="width: 450px; height: 450px" :src="designcloud2" :fit="fit" /></el-col>
  </el-row>
  </div>
</template>
<script>
import bubble_starVue from './components/bubble_star.vue'
import linechart2 from './components/linechart2.vue'
import calender from '../pytorch/components/calender.vue'
import co_ins_delVue from './components/co_ins_del.vue'
import co_code_numVue from './components/co_code_num.vue'
import co_code_num_designVue from './components/co_code_num_design.vue'
import co_code_num_fileVue from './components/co_code_num_file.vue'
import { refreshOther } from '@/api/getdata'
import { refreshData } from '@/api/pytorch'
import contrib_graphVue from '../pytorch/components/contrib_graph.vue'
import List from '../pytorch/components/list.vue'
import * as dataapi from '@/api/getdata'
import * as d3 from 'd3'
import Co_Issue from './components/co_Issue.vue'
export default {
  name: 'UserProfile',
  components: {
    bubble_starVue,
    calender,
    linechart2,
    co_ins_delVue,
    co_code_numVue,
    co_code_num_designVue,
    co_code_num_fileVue,
    contrib_graphVue,
    Co_Issue
},
  data() {
    return {
      htmlTitle:'compare',
      issueNumdata: {},
      starNumdata: {},
      commitNumdata: {},
      threeData: {},
      insDelData1: {},
      insDelData2: {},
      startVal: -1,
      endVal: -1,
      contriData: {},
      designNumdata: {},
      contrigraphData: {},
      contrigraphData2: {},
      designcloud1: String,
      designcloud2: String,
      ListData1: Object,
      ListData2: Object,
      bubbleData: Array,
      contributorCloud_p: String,
      contributorCloud_o: String,
      IssueCloudP:String,
      IssueCloudO:String,
      TimeOfContributor: 0,
      IssueUpdateP:{},
      IssueUpdateO:{},
    
    }
  },

  mounted() {
    const msg = this.$route.query.name
    this.getCompanyStarData()
    this.getcontribCloud_p()
    this.getcontribCloud_o()
    this.getCoInsDel()
    this.getIssue()
    this.getContributionFile()
    this.getContributionDesign()
    this.getCommitLineData()
    this.getContribution()
    this.getDesignNum()
    this.getContribGraph()
    this.getContribGraph2()
    this.getIssueCloud()
    this.getDesignCloud()
    this.getIssueLineData()
    this.getStarLineData()

    this.getInsDelData()
   

  },
  watch: {
  },
  methods: {
    async getContribGraph(){
    await dataapi.getCommitGraph().then(res => {
      var data = {}
        data['x'] = res.x
        data['y'] = res.y
        this.contrigraphData = JSON.parse(JSON.stringify(data))
      
    })
  },
  async getContribGraph2(){
    await dataapi.getCommitGraphO().then(res => {
      var data = {}
        data['x'] = res.x
        data['y'] = res.y
        this.contrigraphData2 = JSON.parse(JSON.stringify(data))
      
    })},
    async   getIssue(){
      await dataapi.getPIssueUpdate().then(res => {
        var data={}
        data['x']=res.x
        data['y1']=res.y1
        data['y2']=res.y2
        this.IssueUpdateP=JSON.parse(JSON.stringify(data))
      })
      await dataapi.getOIssueUpdate().then(res => {
        var data={}
        data['x']=res.x
        data['y1']=res.y1
        data['y2']=res.y2
        this.IssueUpdateO=JSON.parse(JSON.stringify(data))
      
      })
    },
    async getIssueCloud(){
      await dataapi.getPIssueCloud().then(res => {
        this.IssueCloudP='data:image/png;base64,'+res.base64_png
      })
      await dataapi.getOIssueCloud().then(res => {
        this.IssueCloudO='data:image/png;base64,'+res.base64_png
      })
    },
    async getCoInsDel(){
   
      await  dataapi.getInsDelbyHour().then(res => {
        var data={}
        data['x']=res.x
        data['y1']=res.add
        data['y2']=res.del
        this.insDelData1=JSON.parse(JSON.stringify(data))
   
      })
      await dataapi.OgetInsDelbyHour().then(res => {
        var data={}
        data['x']=res.x
        data['y1']=res.add
        data['y2']=res.del
        this.insDelData2=JSON.parse(JSON.stringify(data))
        console.log('insDelData2',this.insDelData2)
      
      })
      
    },
    
    async getDesignNum(){
      await dataapi.OgetDesign().then(res => {
       var data={}
       data['x']=res.pytorch
       data['pytorch']=res.pytorch
       data['pandas']=res.pandas
        this.designNumdata=JSON.parse(JSON.stringify(data))
      })
    },
    
    async getcontribCloud_p() {
    
      await dataapi.getContributionCloud().then(res => {
        this.contributorCloud_p = 'data:image/png;base64,' + res.base64_png
     
      })
    },
    async getcontribCloud_o() {
    
      await dataapi.getContribCloudO().then(res => {
     
        this.contributorCloud_o = 'data:image/png;base64,' + res.base64_png
      })
    },
    starBubble: function (data) {
      // console.log('starBubble')
      this.getCompanyStarData().then(res => {
        //  刷新该组件
        this.companyDataType = 'star'
        document.getElementById("star").className="company-button1"
        // document.getElementById("star").className="company-button"
        document.getElementById("commit").className="company-button"
        document.getElementById("issue").className="company-button"
      })
    },
    issueBubble: function (data) {
  
      this.getCompanyIssueData().then(res => {
        //  刷新该组件
        this.companyDataType = 'issue'
      })
      document.getElementById("star").className="company-button"
        // document.getElementById("star").className="company-button"
        document.getElementById("commit").className="company-button"
        document.getElementById("issue").className="company-button1"
    },
    commitBubble: function (data) {
    
      this.getCompanyCommitData().then(res => {
        //  刷新该组件
        this.companyDataType = 'commit'
      })
      document.getElementById("star").className="company-button"
        // document.getElementById("star").className="company-button"
        document.getElementById("commit").className="company-button1"
        document.getElementById("issue").className="company-button"
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
      
      await dataapi.getDesignCloud().then(res => {
        this.designcloud1 = 'data:image/png;base64,' + res.base64_png})
      await dataapi.OgetDesignCloud().then(res => {
        
        this.designcloud2 = 'data:image/png;base64,' + res.base64_png
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
  
    async getCommitLineData() {
      await dataapi.OgetCommitDevelop().then(res => {
        // 把数组中的每个元素都push到data中
        var data = {}
        data['x'] = res.x
        data['pytorch'] = res.pytorch
        data['pandas'] = res.pandas
        this.commitNumdata = JSON.parse(JSON.stringify(data))
    
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
        data['chartData2']['y1'] = res.o_core
        data['chartData2']['y2'] = res.o_else
        // data['y2'] = res.y2
      
        data=JSON.parse(JSON.stringify(data))
        this.codeNumData = JSON.parse(JSON.stringify(data))
       
    
      })
    },
    async getContributionDesign() {
    
await dataapi.OgetContributionDesign().then(res => {
  // 把数组中的每个元素都push到data中

  var data = { chartData1: {}, chartData2: {} }
  data['chartData1']['x'] = res.x
  data['chartData2']['x'] = res.x
  data['chartData1']['y1'] = res.pytorch_core
  data['chartData1']['y2'] = res.pytorch_else
  data['chartData2']['y1'] = res.o_core
  data['chartData2']['y2'] = res.o_else
  // data['y2'] = res.y2

  data=JSON.parse(JSON.stringify(data))

  this.contriDesign = JSON.parse(JSON.stringify(data))

})
},
async getContributionFile() {

await dataapi.OgetContributionFile().then(res => {
  // 把数组中的每个元素都push到data中

  var data = { chartData1: {}, chartData2: {} }
  data['chartData1']['x'] = res.x
  data['chartData2']['x'] = res.x
  data['chartData1']['y1'] = res.pytorch_core
  data['chartData1']['y2'] = res.pytorch_else
  data['chartData2']['y1'] = res.o_core
  data['chartData2']['y2'] = res.o_else
  // data['y2'] = res.y2

  data=JSON.parse(JSON.stringify(data))

  this.contriFile = JSON.parse(JSON.stringify(data))
 
  // console.log('this.contriData', this.contriData)
})
},
    async refresh() {
     await  refreshData().then(
        // 刷新数据后重新渲染
        // 消息提示
        this.$message({
          message: '刷新成功',
          type: 'success'
        }),
        this.getCompanyStarData(),
    this.getcontribCloud_p(),

    this.getCoInsDel(),
    this.getIssue(),
    this.getContributionFile(),
    this.getContributionDesign(),
    this.getContribution(),
    this.getDesignNum(),
    this.getContribGraph(),
   
    this.getIssueCloud(),
    this.getDesignCloud(),
    this.getIssueLineData(),
    this.getStarLineData(),
    this.getCommitLineData(),
    this.getInsDelData(),
    
      )
      await ORefreshData().then(
        this.$message({
          message: '刷新成功',
          type: 'success'
        }),
        this.getCompanyStarData(),

    this.getcontribCloud_o(),
    this.getCoInsDel(),
    this.getIssue(),
    this.getContributionFile(),
    this.getContributionDesign(),
    this.getContribution(),
    this.getDesignNum(),

    this.getContribGraph2(),
    this.getIssueCloud(),
    this.getDesignCloud(),
    this.getIssueLineData(),
    this.getStarLineData(),
    this.getCommitLineData(),
    this.getInsDelData(),
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
  .svg-icon {
  width: 1.2em;
  height: 1.2em;
  vertical-align: -0.15em;
  // 229, 74, 37
  fill: rgb(229, 74, 37);
  overflow: hidden;
}

  .bt-style {
  background-repeat: no-repeat;
  background-image: url('./images/download.png');
  width: 6em;
  height: 3em;
  background-color: transparent;
  border-style: none;
}
.company-button1 {
  background-color: #aaccff; /* Green */
  border: none;
  color: rgb(238, 245, 255);
  padding: 15px 92px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 15px;
}

}

@media (max-width: 1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
