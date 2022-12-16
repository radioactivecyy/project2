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
      y1: [],
      y2: [],
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
      var mychart = this.chart
      const T = this

      this.chart.on('datazoom', function (params) {
        this.endVal = mychart.getOption().dataZoom[0].endValue
        this.startVal = mychart.getOption().dataZoom[0].startValue
        
        // 向后端发送
        T.$emit('func', { startVal: this.startVal, endVal: this.endVal })
      })
    },
    // 设置图表数据
    setOptions({ expectedData, actualData } = {}) {
      var mydata = JSON.parse(JSON.stringify(this.chartData))

      this.x = mydata.x

      this.y1 = mydata.y1
      this.y2 = mydata.y2
      this.$emit('func', { startVal: 0, endVal: this.x.length - 1 })
      this.chart.setOption({
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none',
              // 是否显示数据缩放视图
            
            }
          }
        },
        dataZoom: [
          {
            type: 'inside',
            start: 0,
            end: 100
          },
          {
            start: 0,
            end: 100
          }
        ],
        legend: {
          data: ['add', 'delete']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            axisTick: {
              show: false
            },
            data: this.x
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'add',
            type: 'bar',
            stack: 'Total',
            label: {
              show: true
            },
            emphasis: {
              focus: 'series'
            },
            data: this.y1
          },
          {
            name: 'delete',
            type: 'bar',
            stack: 'Total',
            label: {
              show: true,
              position: 'left'
            },
            emphasis: {
              focus: 'series'
            },
            data: this.y2
          }
        ]
      })
    }
  }
}
</script>
