<template>
  <div class="dashboard-editor-container">
  <div class="text-center">
  <h1>Pytorch 项目分析平台</h1>
</div>
   
    <el-row :gutter="20">
    
      <el-col :span="6" >
        <tcards name="pytorch" stars="60.2k" forks="16.8k" ppp="/pytorch"/> <tcards name="vs pandas" stars="36.3k" forks="15.5k" ppp="/compare"/>
      </el-col>
      <el-col :span="8" >
    <el-card :body-style="{ padding: '0px' }">
      <el-image :src="cloudData"   />
      <div style="padding: 14px;">
        <a>Pytorch设计相关Issue词云</a>
        <div class="bottom clearfix">
          <time class="time">{{ currentDate }}</time>
          <!-- <el-button type="text" class="button">操作按钮</el-button> -->
        </div>
      </div>
    </el-card>
  </el-col>
  <el-col :span="8" >
    <el-card :body-style="{ padding: '0px' }">
      <el-image :src="commitCloud"  />
      <div style="padding: 14px;">
        <a>Pytorch贡献者词云</a>
        <div class="bottom clearfix">
          <time class="time">{{ currentDate }}</time>
          <!-- <el-button type="text" class="button">操作按钮</el-button> -->
        </div>
      </div>
    </el-card></el-col>
    </el-row>
    
   
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>

    <!-- 图表 -->
  </div>
</template>
<script>
import search from './components/search'
import tcards from './components/repocard.vue' // github repo展示卡片
import linechart from './components/linechart.vue' // 绘图
import * as dataapi from '@/api/getdata'
import linechartVue from '../pytorch/components/linechart.vue'
export default {
  name: 'Dashboard',
  components: {
    search,
    tcards,
    linechart,
    linechartVue
    // piechart
  },
  data() {
    return {
      cloudData:String,
      commitCloud:String
    }
  },
  mounted() {
    this.getCloudData()
    this.getCommit()
  },
  // watch: {
  //   cloudData() {
  //     this.getCloudData()
  //   }
  // },
  methods: {
    async getCloudData() {
      await dataapi.getDesignCloud().then(res => {
        this.cloudData = 'data:image/png;base64,' + res.base64_png
       
      })
      
    },
  async getCommit() {
        await dataapi.getContributionCloud().then(res => {
          this.commitCloud = 'data:image/png;base64,' + res.base64_png
       
      })
   
    },
  
}
  }
</script>

<style lang="scss" scoped>
 .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
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
  .text-center{
        text-align: center;
        // 行间距
        line-height: 3;
    }
  .grid-content {
  border-radius: 4px;
  min-height: 36px;
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
