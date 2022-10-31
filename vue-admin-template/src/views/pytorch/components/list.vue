<template>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>Top 10 Companies</span>
      </div>
    </template>
    <!-- <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div> -->
    <!-- 遍历company_name -->
    <div v-for="o in this.company" :key = "o" class="text item"  ><pre>{{o.name}}                 {{o.count}}</pre></div>
  </el-card>
</template>
<script>
import * as d3 from 'd3'
export default {
  data() {
    return {
      company:[]
      
    }
  },
  mounted() {
    this.getList()
  },
  methods: {
    async getList() {
      const data = await d3.csv('/dev-api/api/issue')
      console.log('dddddddddddddddddddddddddddd',data)
      // 遍历data，将每一行的company字段push到list中
      for (let i = 0; i < data.length; i++) {
        this.company.push({ name: data[i].company, count: data[i].count })
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
}

.text {
  font-size: 15px;
}
.text-item {
  white-space: pre;
}
.item {
  margin-bottom: 18px;
}

.box-card {
  width: 280px;
}
</style>