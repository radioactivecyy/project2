<template>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>Top 10 Companies</span>
        <el-button class="bt-style" @click="getPdf(htmlTitle)"></el-button>
      </div>
    </template>
    <div v-for="o in this.company" :key="o">
      <pre>{{ o.name }}{{ o.count }}</pre>
    </div>
  </el-card>
</template>
<script>
export default {
  props: {
    DataSource: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      company: []
    }
  },
  watch: {
    DataSource: function (val) {
      this.getList()
    }
  },
  mounted() {
    this.getList()
  },
  methods: {
    async getList() {
      const blank = '                                                      '

      const data = this.DataSource
      var del
      var dels
      var co
      this.company = []
      // 遍历data，将每一行的company字段push到list中
      for (let i = 0; i < 10; i++) {
        del = 24 - data[i].company.length
        co = data[i].company
        // console.log('ccccccccccccc',co)
        for (let j = 0; j < del; j++) {
          co = co.concat(' ')
        }
        // console.log('del',del,'ccccccccc',co,'hhh')
        this.company.push({ name: co, count: data[i].count })
      }
      // 遍历list，统计每个公司出现的次数
    }
  }
}
</script>
<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: 'Arial';
  line-height: 200%;
}
.text {
  font-size: 8px;
  line-height: 200%;
}
.textItem {
  white-space: pre;
  /* 字体设置为微软雅黑 */
  font-family: 'Microsoft YaHei';
  font-size: 13px;
  line-height: 300%;
  /* 对齐方式:两端对齐 */
  text-align: justify;
}
.item {
  margin-bottom: 13px;
}
.p {
  font-size: 11px;
  font-family: 'Microsoft YaHei';
}
.box-card {
  width: 300px;
}

.bt-style {
  background-repeat: no-repeat;
  background-image: url('../images/down1.png');
  width: 6em;
  height: 3em;
  background-color: transparent;
  border-style: none;
}
ul li {
  padding: 0;
  margin: 0;
  overflow: hidden;
  /* 字号 */
  font-size: 12px;
  width: 145px;
  height: 40px;
  line-height: 40px;
  text-align: justify;
  text-align-last: justify;
}
ul li:after {
  padding: 0;
  margin: 0;
  content: '';
  display: inline-block;
  width: 100%;
}
</style>
