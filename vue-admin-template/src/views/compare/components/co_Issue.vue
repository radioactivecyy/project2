<template>
  <div>
    <div id="is1" :style="{ height: height, width: width }" />
    <div id="is2" :style="{ height: height, width: width }" />
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
    chartData1: {
      type: Object,
      required: true
    },
    Mytitle1: {
      type: String,
      required: true
    },
    Mytitle2: {
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
    },
    chartData2: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      chart1: null,
        chart2: null,
      mydata: {}
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
        this.setOptions()
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
        this.chart1 = echarts.init(document.getElementById('is1'), 'macarons')
        this.chart2 = echarts.init(document.getElementById('is2'), 'macarons')

      this.setOptions(this.chartData)
    },
    // 设置图表数据
    setOptions({ expectedData, actualData } = {}) {
      var mydata = JSON.parse(JSON.stringify(this.chartData1))
      var mydata2=JSON.parse(JSON.stringify(this.chartData2))
   
      this.date = mydata.x

      this.data1 = mydata.y1
      this.data2 = mydata.y2
   
      var option={
        title: {
          text: this.Mytitle1
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
            data: mydata.x
          }
        ],
        yAxis: [
          {
            type: 'value'
          },
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Email',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
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
          
            emphasis: {
              focus: 'series'
            },
            yAxisIndex: 0,
            data: mydata.y1
          }
        ]
      }
     
      this.chart1.setOption(option)
      var option2=JSON.parse(JSON.stringify(option))
  
  
        option2.series[0].data=mydata2.y2
        option2.series[1].data=mydata2.y1
        option2.xAxis[0].data=mydata2.x
        option2.title.text=this.Mytitle2
        this.chart2.setOption(option2)
        this.chart1.group = 'group1'
      this.chart2.group = 'group1'
      echarts.connect('group1')
    }
  }
}
</script>
