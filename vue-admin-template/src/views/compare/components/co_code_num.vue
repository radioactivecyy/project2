<template>
  <div>
    <div id="co1" :style="{ height: height, width: width }" />

    <div id="co2" :style="{ height: height, width: width }" />
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
      default: '400px'
    },
    chartData: {
      type: Object,
      required: true
    },

  },
  data() {
    return {
      chart1: null,
      chart2: null,
      msg: null
    }
  },
  watch: {
    chartData1: {
      handler() {
        this.initChart()
      },
      deep: true
    },
    chartData2: {
      handler() {
        this.initChart()
      },
      deep: true
    }
  },
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
    initChart() {
      this.chart1 = echarts.init(document.getElementById('co1'), 'macarons')
      this.chart2 = echarts.init(document.getElementById('co2'), 'macarons')
      var mydata1 = JSON.parse(JSON.stringify(this.chartData)).charData1
      var mydata2 = JSON.parse(JSON.stringify(this.chartData)).charData2
      var mysource1 = mydata1.x
      var mysource2 = mydata1.y1
      var mysource3 = mydata1.y2
      // 将mysource1添加到mysource中
      mysource1.push(mysource1)
      // 将mysource2添加到mysource中
      mysource1.push(mysource2)
      // 将mysource3添加到mysource中
      mysource1.push(mysource3)
      mysource1= mydata2.x
      mysource2 = mydata2.y1
       mysource3 = mydata2.y2
      // 将mysource1添加到mysource中
      mysource2.push(mysource1)
      // 将mysource2添加到mysource中
      mysource2.push(mysource2)
      // 将mysource3添加到mysource中
      mysource2.push(mysource3)
      setTimeout(() => {
        var option1 = {
          legend: {
            orient: 'vertical',
            right: 10,
            top: 20,
            bottom: 20
          },
          tooltip: {
            trigger: 'axis',
            showContent: false,
            dataZoom: {
              type: 'inside'
            }
          },
          dataset: {
            source: mysource1
          },
          title: {
            // 位置设置为底部

            left: 'center',
            text: '贡献者'
          },
          dataZoom: {
            type: 'slider',
            start: 0,
            end: 100
          },
          xAxis: { type: 'category' },
          yAxis: { gridIndex: 0 },
          grid: { top: '55%' },
          series: [
            {
              type: 'line',
              smooth: true,
              seriesLayoutBy: 'row',
              emphasis: { focus: 'series' }
            },
            {
              type: 'line',
              smooth: true,
              seriesLayoutBy: 'row',
              emphasis: { focus: 'series' }
            },

            {
              type: 'pie',
              id: 'pie',
              radius: '30%',
              center: ['50%', '25%'],
              emphasis: {
                focus: 'self'
              },
              label: {
                formatter: '{b}: {@'+1+'} ({d}%)'
              },
              encode: {
                itemName: 0,
                value: 1,
                tooltip: 1
              }
            }
          ]
        }
        var option2 = JSON.parse(JSON.stringify(option1))
        option2.dataZoom.show = false
        option2.dataset.source = mysource2
        var C = this.chart1
        var T = this
        this.chart1.on('updateAxisPointer', function (event) {
          const xAxisInfo = event.axesInfo[0]
          
          if (xAxisInfo) {
            T.msg = xAxisInfo.value
            T.$emit('func', T.msg)
            const dimension = xAxisInfo.value + 1
            C.setOption({
              series: {
                id: 'pie',
                label: {
                  formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                },
                encode: {
                  value: dimension,
                  tooltip: dimension
                }
              }
            })
          }
        })
        this.chart1.setOption(option1)
        this.chart2.on('updateAxisPointer', function (event) {
          const xAxisInfo = event.axesInfo[0]

          if (xAxisInfo) {
            T.msg = xAxisInfo.value
            T.$emit('func', T.msg)
            const dimension = xAxisInfo.value + 1
            C.setOption({
              series: {
                id: 'pie',
                label: {
                  formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                },
                encode: {
                  value: dimension,
                  tooltip: dimension
                }
              }
            })
          }
        })
        this.chart2.setOption(option2)
      }, 1000)
    }
  }
}
</script>
