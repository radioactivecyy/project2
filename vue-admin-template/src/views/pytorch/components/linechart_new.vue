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
    Mytitle: {
      type: String,
      required: true
    },
    dataSource: {
      type: String,
      required: true
    },
    color1: {
      type: String,
      required: true
    },
    color2: {
      type: String,
      required: true
    },
    color3: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      chart: null,
      mydata: {},
      
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
      
      this.date = mydata.x

      this.data1 = mydata.y1
      this.data2 = mydata.y2
      this.chart.setOption({
        title: {
          text:this.Mytitle
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },

        legend: {
          data: ['total created', 'new updated']
        },
        toolbox: {
          feature: {
            saveAsImage: {},
              dataZoom: {
              yAxisIndex: 'none'
            },
          },
        
        },
        dataZoom: [
        {
            type: 'inside',
            start: 0,
            end: 100},
          {
            start: 0,
            end: 100
          }
        ],
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data:  this.date
          }
        ],
        yAxis: [
          {
            type: 'value'
          },{
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Email',
            type: 'line',
            stack: 'Total',
            areaStyle: {
              
            },
            emphasis: {
              focus: 'series'
            },
            yAxisIndex: 1,
            data: mydata.y2
          },
          {
            name: 'Union Ads',
            type: 'line',
            stack: 'Total',
            // areaStyle: {},
            emphasis: {
              focus: 'series'
            },
            yAxisIndex:0,
            data: mydata.y1
          }
        ]
      })
    }
  }
}
</script>
