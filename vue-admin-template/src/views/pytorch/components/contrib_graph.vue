<template>
  <div :class="className" :style="{ height: height, width: width }" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from '../mixins/resize'

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '350px'
    },
    autoResize: {
      type: Boolean,
      default: true
    },
    Mytitle:{
        type: String,
        required: true
        },
    
    chartData: {
      type: Object,
      required: true
    },
    lineTitle1: {
      type: String,
      required: true
    },
    lineTitle2: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      chart: null,
      x: [],
      y: [],
      
      startVal: null,
      endVal: null
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    },
    lineTitle1: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    },
    lineTitle2: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    }
  },
  // 新建mounted 否则会出现init没有定义
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    // 初始化图表
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      this.setOptions(this.chartData)
     

    
    },
    // 设置图表数据
    setOptions({ expectedData, actualData } = {}) {
      var mydata = JSON.parse(JSON.stringify(this.chartData))

      this.x = mydata.x

      this.y = mydata.y
    

      this.chart.setOption({
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        title:{
            text:this.Mytitle,
            left:'center',
            top:'top'
        },
     
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: 
            {
            type: 'value',
                position:'top',
                splitline:{
                    lineStyle:{
                        type:'dashed'
                    }
                }
          }
        ,
        yAxis: 
          
          {
            type: 'category',
            axisTick: {
              show: false
            },
            data: this.x
          }
        ,
        series: [
          {
            name: 'commit code ',
            type: 'bar',
            stack: 'Total',
            label: {
              show: true
            },
            emphasis: {
              focus: 'series'
            },
            data: this.y
          },
       
        ]
      })
    }
  }
}
</script>
