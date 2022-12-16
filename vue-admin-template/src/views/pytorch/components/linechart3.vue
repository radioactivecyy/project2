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
    chartData1: {
      type: Object,
      required: true
    },
    chartData2: {
      type: Object,
      required: true
    },
    chartData3: {
      type: Object,
      required: true
    },
    myTitle: {
      type: String,
      required: true
    },
    dataSource: {
      type: String,
      required: true
    },
    color1_1: {
      type: String,
      required: true
    },
    color2_1: {
      type: String,
      required: true
    },
    color3_1: {
      type: String,
      required: true
    },
    color1_2: {
      type: String,
      required: true
    },
    color2_2: {
      type: String,
      required: true
    },
    color3_2: {
      type: String,
      required: true
    },
    color1_3: {
      type: String,
      required: true
    },
    color2_3: {
      type: String,
      required: true
    },
    color3_3: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      chart: null,
      data1: [],
      data2: [],
      data3: [],
    }
  },
  watch: {
    chartData1: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    },
    chartData2: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    },
    chartData3: {
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
      this.setOptions(this.chartData1)
    },
    // 设置图表数据
    setOptions({ expectedData, actualData } = {}) {
     
      var mydata1 = JSON.parse(JSON.stringify(this.chartData1))
      var mydata2 = JSON.parse(JSON.stringify(this.chartData2))
      var mydata3 = JSON.parse(JSON.stringify(this.chartData3))
     
      this.date = mydata1.x
      this.data1 = mydata1.y
      this.data2 = mydata2.y
      this.data3 = mydata3.y
  
     
     
      this.chart.setOption({
        tooltip: {
          trigger: 'axis',
          position: function (pt) {
            return [pt[0], '10%']
          }
        },
        title: {
          left: 'center',
          text: this.myTitle
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.date
        },
        yAxis: {
          type: 'value',
          boundaryGap: [0, '100%']
        },
        dataZoom: [
         
          {
            start: 0,
            end: 100
          }
        ],
        series: [
          {
            name: 'issue Data',
            type: 'line',
            symbol: 'none',
            sampling: 'lttb',
            itemStyle: {
              color: this.color1_1
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: this.color2_1
                },
                {
                  offset: 1,
                  color: this.color2_1
                }
              ])
            },
            data: this.data1
          },
          {
            name: 'issue Data',
            type: 'line',
            symbol: 'none',
            sampling: 'lttb',
            itemStyle: {
              color: this.color1_2
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: this.color2_2
                },
                {
                  offset: 1,
                  color: this.color3_2
                }
              ])
            },
            data: this.data2
          },
          {
            name: 'commit Data',
            type: 'line',
            symbol: 'none',
            sampling: 'lttb',
            itemStyle: {
              color: this.color1_3
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: this.color2_3
                },
                {
                  offset: 1,
                  color: this.color3_3
                }
              ])
            },
            data: this.data3
          }
        ]
      })
    }
  }
}
</script>
