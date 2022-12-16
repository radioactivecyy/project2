<template>
  <div :class="className" :style="{ height: height, width:width }" />
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
      mydata:{},
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
     
      this.data = mydata.y
      this.chart.setOption({
        tooltip: {
          trigger: 'axis',
          position: function (pt) {
            return [pt[0], '100%']
          }
        },
        title: {
          left: 'center',
          text: this.Mytitle
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
          data: this.date
        },
        yAxis: {
        
          // 取整  
          
          
          // max: Math.ceil(this.data[this.data.length-1]/1000)*1000,
          type: 'value',
          // boundaryGap: [0, '100%']
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
        series: [
          {
            name: this.Mytitle,
            type: 'line',
            symbol: 'none',
            sampling: 'lttb',

            data: this.data
                 // itemStyle: {
            //   color: this.color1
            // },
            // areaStyle: {
            //   color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            //     {
            //       offset: 0,
            //       color: this.color2
            //     },
            //     {
            //       offset: 1,
            //       color: this.color2
            //     }
            //   ])
            // },
          }
        ]
      })
    }
  }
}
</script>
