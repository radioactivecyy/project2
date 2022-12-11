<template>
  <div>
    <div id="ins1" :style="{ height: height, width: width }" />
    <div id="ins2" :style="{ height: height, width: width }" />
  </div>
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
    }
  },
  data() {
    return {
      chart1: null,
      chart2: null,
      x1: [],
      y11: [],
      y12: [],
      x2: [],
      y21: [],
      y22: [],
    }
  },
  watch: {
    chartData: {
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
    if (!this.chart1) {
      return
    }
    if (!this.chart2) {
      return
    }
    this.chart1.dispose()
    this.chart2.dispose()
    this.chart1 = null
    this.chart2 = null
  },
  methods: {
    // 初始化图表
    initChart() {
      var mydata = JSON.parse(JSON.stringify(this.chartData))['chartData1']
      this.x1 = mydata.x
      this.y11 = mydata.y1
      this.y12 = mydata.y2
      mydata = JSON.parse(JSON.stringify(this.chartData))['chartData2']
      this.x2 = mydata.x
      this.y21 = mydata.y1
      this.y22 = mydata.y2
      var option1 = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        toolbox: {
          feature: {
            dataZoom: {
              xAxisIndex: 'none'
            }
          }
        },
        dataZoom: {
          show: true,
          realtime: true,
          start: 0,
          end: 100
        },
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
            data: this.x1
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Income',
            type: 'bar',
            stack: 'Total',
            label: {
              show: true
            },
            emphasis: {
              focus: 'series'
            },
            data: this.y11
          },
          {
            name: 'Expenses',
            type: 'bar',
            stack: 'Total',
            label: {
              show: true,
              position: 'left'
            },
            emphasis: {
              focus: 'series'
            },
            data: this.y12
          }
        ]
      }
      //   拷贝option1
      
      var option2 = JSON.parse(JSON.stringify(option1))
      option2.dataZoom.show = false
      option2.series[0].data = this.y21
      option2.series[1].data = this.y22
      option2.xAxis[0].data = this.x2
      console.log('option1', option1)
      console.log('option2', option2)
      this.$emit('func', { startVal: 0, endVal: this.x1.length - 1  })
      this.chart1 = echarts.init(document.getElementById('ins1'), 'macarons')
      this.chart1.setOption(option1)
      var mychart = this.chart1
      const T = this
      this.chart1.on('datazoom', function (params) {
        let endValue = mychart.getOption().dataZoom[0].endValue
        let startValue = mychart.getOption().dataZoom[0].startValue
        // 向后端发送
        T.$emit('func', { startVal: startValue, endVal: endValue })
      })
      this.chart2 = echarts.init(document.getElementById('ins2'), 'macarons')
      this.chart2.setOption(option2)
      this.chart1.group = 'group1'
      this.chart2.group = 'group1'
      echarts.connect('group1')
    }
    // 设置图表数据
  }
}
</script>
